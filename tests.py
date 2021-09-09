import argparse
from bunnyhop.core import BunnyStream
import unittest
from unittest import mock
from envs import env
from bunnyhop import Bunny, BunnyStream

BUNNYCDN_API_KEY = env('BUNNYCDN_API_KEY')
BUNNYCDN_TEST_STORAGE_ZONE = env('BUNNYCDN_TEST_STORAGE_ZONE')
BUNNYCDN_TEST_STORAGE_ZONE_NAME = env('BUNNYCDN_TEST_STORAGE_ZONE_NAME')
BUNNYCDN_TEST_PULL_ZONE = env('BUNNYCDN_TEST_PULL_ZONE')
BUNNYCDN_STREAM_API_KEY = env('BUNNY_STREAM_API_KEY')
BUNNYCDN_STREAM_LIBRARY_KEY = env('BUNNYCDN_STREAM_LIBRARY_KEY')


# class TestBilling(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.b = Bunny(BUNNYCDN_API_KEY)

#     @classmethod
#     def tearDownClass(cls):
#         cls.b = None

#     def test_get(self):
#         from bunnyhop.billing import BillingSummary
#         response = self.b.Billing.get()
#         self.assertIsInstance(response, BillingSummary)

#     def test_apply_code(self):
#         response = self.b.Billing.apply_code('dummy-code')
#         self.assertEqual(response['ErrorKey'], 'code.invalid')


# class TestStats(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.b = Bunny(BUNNYCDN_API_KEY)

#     @classmethod
#     def tearDownClass(cls):
#         cls.b = None

#     def test_get(self):
#         from bunnyhop.stats import Stats
#         response = self.b.Stats.get()
#         self.assertIsInstance(response, Stats)


# class TestPurge(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.b = Bunny(BUNNYCDN_API_KEY)

#     @classmethod
#     def tearDownClass(cls):
#         cls.b = None

#     def test_create(self):
#         response = self.b.Purge.create("http://non-existentmyzone.b-cdn.net/")
#         self.assertEqual(response['ErrorKey'], 'purge.hostname_not_found')


# class TestStorageZone(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.b = Bunny(BUNNYCDN_API_KEY)

#     @classmethod
#     def tearDownClass(cls):
#         cls.b = None

#     def test_get(self):
#         response = self.b.Storage.get(BUNNYCDN_TEST_STORAGE_ZONE)
#         self.assertEqual(BUNNYCDN_TEST_STORAGE_ZONE_NAME, response.Name)

#     def test_delete(self):
#         response = self.b.Storage.delete(1111)
#         self.assertEqual(response['ErrorKey'], 'storageZone.not_found')

#     def test_create(self):
#         response = self.b.Storage.create(1)
#         self.assertTrue(response['ErrorKey'] == 'storagezone.validation' or response['ErrorKey'] == 'user.insufficient_balance')

#     def test_all(self):
#         response = self.b.Storage.all()
#         self.assertIsInstance(response, list)


# class TestZone(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.b = Bunny(BUNNYCDN_API_KEY)

#     @classmethod
#     def tearDownClass(cls):
#         cls.b = None

#     def test_get(self):
#         response = self.b.Zone.get("")
#         self.assertEqual(response, 'Zone not found.')

#     def test_list(self):
#         response = self.b.Zone.list()
#         self.assertIsInstance(response, list)

#     def test_delete(self):
#         response = self.b.Zone.delete('test')
#         self.assertEqual(response['Message'], 'The request is invalid.')

#     def test_purge(self):
#         response = self.b.Zone.purge('test')
#         self.assertEqual(response['Message'], 'The request is invalid.')


class TestStreamCollection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = BunnyStream('BUNNYCDN_STREAM_API_KEY', 'BUNNYCDN_STREAM_LIBRARY_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_create(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
                    "videoLibraryId": 1,  "guid": 'asdf',
                    "name": 'unittest-bunnyhop', "videoCount": 123,
                    "totalSize": 1, "previewVideoIds": 'asdf'
                }

        name = 'unittest-bunnyhop'
        response = self.b.StreamCollection.create(name)
        self.assertEqual(response.name, name)

    def test_get(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
                    "videoLibraryId": 1,  "guid": 'asdf',
                    "name": 'unittest', "videoCount": 123,
                    "totalSize": 1, "previewVideoIds": 'asdf'
                }

        name = 'unittest'
        response = self.b.StreamCollection.get('asdas')
        self.assertEqual(response.name, name)

    def test_list(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'totalItems': 1,
            'currentPage': 1,
            'itemsPerPage': 10,
            'items': [{'videoLibraryId': 111,
                       'guid': 'aa',
                       'name': 'test',
                       'videoCount': 1,
                       'totalSize': 1,
                       'previewVideoIds': 'aa'}]}

        response = self.b.StreamCollection.all()
        self.assertEqual(response.get('currentPage'), 1)

    def test_update(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "success": bool,
            "message": str,
            "statusCode": int
        }

        updated_name = 'updated-unittest-bunnyhop'
        response = self.b.StreamCollection.update(updated_name, 'collection-id')
        self.assertTrue(response.get('success'))

    def test_delete(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "success": bool,
            "message": str,
            "statusCode": int
        }

        response = self.b.StreamCollection.delete('guid-test')
        self.assertTrue(response.get('success'))


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
