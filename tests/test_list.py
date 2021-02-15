import unittest
import json
from jsonpath import traverse


class TestSimpleList(unittest.TestCase):
    def setUp(self):
        self.json_obj = json.loads('["a", "b", "c"]')

    def test_one_level(self):
        value = traverse(self.json_obj, '/0')
        self.assertEqual('a', value)
        value = traverse(self.json_obj, '/1')
        self.assertEqual('b', value)

    def test_one_level_no_slash(self):
        value = traverse(self.json_obj, '0')
        self.assertEqual('a', value)
        value = traverse(self.json_obj, '1')
        self.assertEqual('b', value)

    def test_one_level_trailing_slash(self):
        value = traverse(self.json_obj, '/0/')
        self.assertEqual('a', value)
        value = traverse(self.json_obj, '/1/')
        self.assertEqual('b', value)

    def test_one_level_no_slash_trailing_slash(self):
        value = traverse(self.json_obj, '0/')
        self.assertEqual('a', value)
        value = traverse(self.json_obj, '1/')
        self.assertEqual('b', value)

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
        self.json_obj = json.loads('["a", "b", ["c", "d"]]')

    def test_one_level(self):
        value = traverse(self.json_obj, '/2')
        self.assertEqual(self.json_obj[2], value)

    def test_one_level_no_slash(self):
        value = traverse(self.json_obj, '2')
        self.assertEqual(self.json_obj[2], value)

    def test_two_levels(self):
        value = traverse(self.json_obj, '/2/0')
        self.assertEqual('c', value)
        value = traverse(self.json_obj, '/2/1')
        self.assertEqual('d', value)

    def test_two_levels_no_leading_slash(self):
        value = traverse(self.json_obj, '2/0')
        self.assertEqual('c', value)
        value = traverse(self.json_obj, '2/1')
        self.assertEqual('d', value)

    def test_two_levels_trailing_slash(self):
        value = traverse(self.json_obj, '/2/0/')
        self.assertEqual('c', value)
        value = traverse(self.json_obj, '/2/1/')
        self.assertEqual('d', value)

    def test_two_levels_no_leading_slash_trailing_slash(self):
        value = traverse(self.json_obj, '2/0/')
        self.assertEqual('c', value)
        value = traverse(self.json_obj, '2/1/')
        self.assertEqual('d', value)

    def test_one_level_empty_path(self):
        value = traverse(self.json_obj, '')
        self.assertEqual(self.json_obj, value)

    def test_one_level_none(self):
        value = traverse(self.json_obj, None)
        self.assertEqual(self.json_obj, value)

    def test_one_level_no_path(self):
        value = traverse(self.json_obj, '/')
        self.assertEqual(self.json_obj, value)
