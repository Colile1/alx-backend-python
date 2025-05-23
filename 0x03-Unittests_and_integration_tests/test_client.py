#!/usr/bin/env python3
"""
Unit and integration tests for client.py
"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns correct
        value and get_json is called once.
        """
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the
        correct URL from org payload.
        """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://some_url"}
            client = GithubOrgClient("test")
            self.assertEqual(client._public_repos_url, "http://some_url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the list of repo names."""
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        with patch.object(
                GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
                ) as mock_url:
            mock_url.return_value = "http://some_url"
            client = GithubOrgClient("test")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://some_url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns True only for matching license key."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""
    @classmethod
    def setUpClass(cls):
        """Set up class by patching requests.get to return fixtures."""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith('/orgs/google'):
                mock = unittest.mock.Mock()
                mock.json.return_value = cls.org_payload
                return mock
            elif url.endswith('/orgs/google/repos'):
                mock = unittest.mock.Mock()
                mock.json.return_value = cls.repos_payload
                return mock
            return unittest.mock.Mock()
        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repos from fixture."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos with license filter returns expected repos.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
