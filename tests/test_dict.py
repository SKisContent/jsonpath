import unittest
import json
from jsonpath import traverse


class TestSimpleDict(unittest.TestCase):
    def setUp(self):
        self.json_obj = json.loads('{"foo":"bar"}')

    def test_one_level(self):
        value = traverse(self.json_obj, '/foo')
        self.assertEqual('bar', value)

    def test_one_level_no_slash(self):
        value = traverse(self.json_obj, 'foo')
        self.assertEqual('bar', value)

    def test_one_level_trailing_slash(self):
        value = traverse(self.json_obj, '/foo/')
        self.assertEqual('bar', value)

    def test_one_level_no_slash_trailing_slash(self):
        value = traverse(self.json_obj, 'foo/')
        self.assertEqual('bar', value)

    def test_one_level_empty_path(self):
        value = traverse(self.json_obj, '')
        self.assertEqual(self.json_obj, value)

    def test_one_level_none(self):
        value = traverse(self.json_obj, None)
        self.assertEqual(self.json_obj, value)

    def test_one_level_no_path(self):
        value = traverse(self.json_obj, '/')
        self.assertEqual(self.json_obj, value)


class TestNestedDict(unittest.TestCase):
    def setUp(self):
        self.json_obj = json.loads('{"foo": {"bar": "baz"}}')

    def test_one_level(self):
        value = traverse(self.json_obj, '/foo')
        self.assertEqual(self.json_obj['foo'], value)

    def test_one_level_no_slash(self):
        value = traverse(self.json_obj, 'foo')
        self.assertEqual(self.json_obj['foo'], value)

    def test_two_levels(self):
        value = traverse(self.json_obj, '/foo/bar')
        self.assertEqual('baz', value)

    def test_two_levels_no_leading_slash(self):
        value = traverse(self.json_obj, 'foo/bar')
        self.assertEqual('baz', value)

    def test_one_level_empty_path(self):
        value = traverse(self.json_obj, '')
        self.assertEqual(self.json_obj, value)

    def test_one_level_none(self):
        value = traverse(self.json_obj, None)
        self.assertEqual(self.json_obj, value)

    def test_one_level_no_path(self):
        value = traverse(self.json_obj, '/')
        self.assertEqual(self.json_obj, value)

    def test_two_levels_trailing_slash(self):
        value = traverse(self.json_obj, '/foo/bar/')
        self.assertEqual('baz', value)

    def test_two_levels_no_leading_slash_trailing_slash(self):
        value = traverse(self.json_obj, 'foo/bar/')
        self.assertEqual('baz', value)
