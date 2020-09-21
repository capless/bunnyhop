import argparse
import unittest
import json
from unittest.mock import patch, mock_open
from bunnyhop import Bunny


class TestBilling(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.b = Bunny(args.api_key)

    @classmethod
    def tearDownClass(self):
        self.b = None

    def test_get(self):
        from bunnyhop.billing import BillingSummary
        response = self.b.Billing.get()
        self.assertIsInstance(response, BillingSummary)

    def test_apply_code(self):
        response = self.b.Billing.apply_code('dummy-code')
        self.assertEqual(response['ErrorKey'], 'code.invalid')


class TestStats(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.b = Bunny(args.api_key)

    @classmethod
    def tearDownClass(self):
        self.b = None

    def test_get(self):
        from bunnyhop.stats import Stats
        response = self.b.Stats.get()
        self.assertIsInstance(response, Stats)


class TestPurge(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.b = Bunny(args.api_key)

    @classmethod
    def tearDownClass(self):
        self.b = None

    def test_create(self):
        response = self.b.Purge.create("http://non-existentmyzone.b-cdn.net/")
        self.assertEqual(response['ErrorKey'], 'purge.hostname_not_found')


class TestStorageZone(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.b = Bunny(args.api_key)

    @classmethod
    def tearDownClass(self):
        self.b = None

    def test_get(self):
        response = self.b.Storage.get("string")
        self.assertIsNone(response)

    def test_delete(self):
        response = self.b.Storage.delete(1111)
        self.assertEqual(response['ErrorKey'], 'storageZone.not_found')

    def test_create(self):
        response = self.b.Storage.create(1)
        self.assertTrue(response['ErrorKey'] == 'storagezone.validation' or response['ErrorKey'] == 'user.insufficient_balance')

    def test_all(self):
        response = self.b.Storage.all()
        self.assertIsInstance(response, list)


class TestZone(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.b = Bunny(args.api_key)

    @classmethod
    def tearDownClass(self):
        self.b = None

    def test_get(self):
        response = self.b.Zone.get("")
        self.assertEqual(response, 'Zone not found.')

    def test_list(self):
        response = self.b.Zone.list()
        self.assertIsInstance(response, list)

    def test_delete(self):
        response = self.b.Zone.delete('test')
        self.assertEqual(response['Message'], 'The request is invalid.')

    def test_purge(self):
        response = self.b.Zone.purge('test')
        self.assertEqual(response['Message'], 'The request is invalid.')


def parse_args():
    parser = argparse.ArgumentParser(description='Bunnyhop Unit Test')
    parser.add_argument('api_key', help='valid api_key to run the functions',
                        metavar="api_key", type=str)
    # other arguments here ...
    ns, args = parser.parse_known_args(namespace=unittest)
    return ns, sys.argv[:1] + args


if __name__ == '__main__':
    import sys
    args, argv = parse_args()
    sys.argv[:] = argv
    unittest.main()
