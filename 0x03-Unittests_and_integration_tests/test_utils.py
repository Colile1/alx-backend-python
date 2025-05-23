#!/usr/bin/env python3
"""
Unit tests for utils.py
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ("{'a': 1}", {"a": 1}, ("a",), 1),
        ("{'a': {'b': 2}} path ('a',)", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("{'a': {'b': 2}} path ('a', 'b')", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, _, nested_map, path, expected):
        """Test that access_nested_map returns expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("{} path ('a',)", {}, ("a",)),
        ("{'a': 1} path ('a', 'b')", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, _, nested_map, path):
        """Test that access_nested_map raises KeyError for invalid path."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test cases for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns expected payload from mocked requests.get.
        """
        mock_get.return_value = Mock(**{"json.return_value": test_payload})
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches method result."""
        class TestClass:
            def a_method(self) -> int:
                """Returns 42."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Memoized property calling a_method."""
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
