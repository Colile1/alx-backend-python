#!/usr/bin/env python3
"""
Client for interacting with GitHub organizations and their repositories.
"""
from typing import List, Dict, Optional, Any
from utils import get_json, memoize


class GithubOrgClient:
    """
    GithubOrgClient interacts with the GitHub API for organization data.
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize with organization name."""
        self.org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Return the organization data from GitHub API."""
        return get_json(self.ORG_URL.format(org=self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the organization's public repos."""
        return self.org.get("repos_url")

    def public_repos(self, license: Optional[str] = None) -> List[str]:
        """
        Returns list of public repository names. Optionally filter by license
        Args:
            license: Optional license key to filter repos.
        Returns:
            List of repository names.
        """
        repos = get_json(self._public_repos_url)
        names = []
        for repo in repos:
            if license is None or self.has_license(repo, license):
                names.append(repo["name"])
        return names

    @staticmethod
    def has_license(repo: Dict[str, Any], license_key: str) -> bool:
        """
        Check if a repo has a specific license key.
        Args:
            repo: The repository dictionary.
            license_key: The license key to check for.
        Returns:
            True if the repo has the license, False otherwise.
        """
        return repo.get("license", {}).get("key") == license_key
