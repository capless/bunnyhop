import argparse
from bunnyhop.core import BunnyStream
import unittest
from envs import env
from bunnyhop import Bunny

BUNNYCDN_API_KEY = env('BUNNYCDN_API_KEY')
BUNNYCDN_TEST_STORAGE_ZONE = env('BUNNYCDN_TEST_STORAGE_ZONE')
BUNNYCDN_TEST_STORAGE_ZONE_NAME = env('BUNNYCDN_TEST_STORAGE_ZONE_NAME')
BUNNYCDN_TEST_PULL_ZONE = env('BUNNYCDN_TEST_PULL_ZONE')
BUNNYCDN_STREAM_API_KEY = env('BUNNY_STREAM_API_KEY')


class TestBilling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = Bunny(BUNNYCDN_API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.b = None

    def test_get(self):
        from bunnyhop.billing import BillingSummary
        response = self.b.Billing.get()
        self.assertIsInstance(response, BillingSummary)

    def test_apply_code(self):
        response = self.b.Billing.apply_code('dummy-code')
        self.assertEqual(response['ErrorKey'], 'code.invalid')


class TestStats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny(BUNNYCDN_API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.b = None

    def test_get(self):
        from bunnyhop.stats import Stats
        response = self.b.Stats.get()
        self.assertIsInstance(response, Stats)


class TestPurge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny(BUNNYCDN_API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.b = None

    def test_create(self):
        response = self.b.Purge.create("http://non-existentmyzone.b-cdn.net/")
        self.assertEqual(response['ErrorKey'], 'purge.hostname_not_found')


class TestStorageZone(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny(BUNNYCDN_API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.b = None

    def test_get(self):
        response = self.b.Storage.get(BUNNYCDN_TEST_STORAGE_ZONE)
        self.assertEqual(BUNNYCDN_TEST_STORAGE_ZONE_NAME, response.Name)

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
    def setUpClass(cls):
        cls.b = Bunny(BUNNYCDN_API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.b = None

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


class TestStreamCollection(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.b = BunnyStream(BUNNYCDN_STREAM_API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.b = None

    def test_create(self):
        response = self.b.StreamCollection.create('test')
        expected =  {
                "videoLibraryId": int,
                "guid": str,
                "name": str,
                "videoCount": int,
                "totalSize": int,
                "previewVideoIds": str
            }
        self.assertEqual('')

    def test_get(self):
        response = self.b.StreamCollection.get()

    def test_list(self):
        response = self.b.StreamCollection.all()

    def test_update(self):
        response = self.b.StreamCollection.update()

    def test_delete(self):
        response = self.b.StreamCollection.delete()


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
