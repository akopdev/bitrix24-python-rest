import unittest
import os
from bitrix24 import Bitrix24, BitrixError


class Bitrix24Test(unittest.TestCase):

    def setUp(self):
        self.b24 = Bitrix24(os.environ.get('TEST_DOMAIN'))

    def test_call_post_method(self):
        r = self.b24.callMethod('crm.deal.add', fields={
                                'TITLE': 'Hello World'})
        self.assertIs(type(r), int)

    def test_call_get_method(self):
        r = self.b24.callMethod('crm.deal.list', filter={
                                'TITLE': 'Hello World'})
        self.assertIs(type(r), list)

    def test_call_with_empty_method(self):
        with self.assertRaises(BitrixError):
            self.b24.callMethod('')

    def test_call_non_exists_method(self):
        with self.assertRaises(BitrixError):
            self.b24.callMethod('hello.world')


if __name__ == '__main__':
    unittest.main()
