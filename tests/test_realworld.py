import unittest
import json
from jsonpath import traverse
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))


class TestSimpleList(unittest.TestCase):
    def setUp(self):
        with open('{0}/fixtures/webhook.json'.format(BASE_PATH), 'r') as fp:
            self.json_obj = json.load(fp)

    def test_dict_only(self):
        value = traverse(self.json_obj, '/hook/events/0')
        self.assertEqual('push', value)

    def test_dict_list_value(self):
        items_list = traverse(self.json_obj, '/hook/events')
        value = items_list[0]
        self.assertEqual('push', value)

    def test_dict_dict_value(self):
        dict_value = traverse(self.json_obj, '/hook/last_response')
        value = dict_value['status']
        self.assertEqual('unused', value)

    def test_dict_and_list(self):
        value = traverse(self.json_obj, '/hook/last_response/status')
        self.assertEqual('unused', value)
