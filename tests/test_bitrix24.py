import unittest
import os
from bitrix24 import Bitrix24, BitrixError


class Bitrix24Test(unittest.TestCase):

    def setUp(self):
        self.b24 = Bitrix24('https://example.bitrix24.com/rest/1/123456789')

    def test_init_with_empty_domain(self):
        with self.assertRaises(Exception):
            Bitrix24('')

    def test_call_with_empty_method(self):
        with self.assertRaises(BitrixError):
            self.b24.callMethod('')

    def test_call_non_exists_method(self):
        with self.assertRaises(BitrixError):
            self.b24.callMethod('hello.world')

    def test_call_wrong_method(self):
        with self.assertRaises(BitrixError):
            self.b24.callMethod('helloworld')

class ParamsPreparationTest(unittest.TestCase):

    def setUp(self):
        self.b24 = Bitrix24('https://example.bitrix24.com/rest/1/123456789')

    def test_one_level(self):
        params = {"fruit": "apple"}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit=apple&")

    def test_one_level_several_items(self):
        params = {"fruit": "apple", "vegetable": "broccoli"}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit=apple&vegetable=broccoli&")

    def test_multi_level(self):
        params = {"fruit": {"citrus": "lemon"}}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit[citrus]=lemon&")

    def test_multi_level_deep(self):
        params = {"root": {"level 1": {"level 2": {"level 3": "value"}}}}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(
            param_string, "root[level 1][level 2][level 3]=value&")

    def test_list_dict_mixed(self):
        params = {"root": {"level 1": [
            {"list_dict 1": "value 1"}, {"list_dict 2": "value 2"}]}}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(
            param_string, "root[level 1][0][list_dict 1]=value 1&root[level 1][1][list_dict 2]=value 2&")

    def test_multi_level_several_items(self):
        params = {"fruit": {"citrus": "lemon", "sweet": "apple"}}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(
            param_string, "fruit[citrus]=lemon&fruit[sweet]=apple&")

    def test_list(self):
        params = {"fruit": ["lemon", "apple"]}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit[0]=lemon&fruit[1]=apple&")

    def test_tuple(self):
        params = {"fruit": ("lemon", "apple")}
        param_string = self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit[0]=lemon&fruit[1]=apple&")

    def test_string(self):
        param_string = self.b24._prepare_params('')
        self.assertEqual(param_string, "")


if __name__ == '__main__':
    unittest.main()
