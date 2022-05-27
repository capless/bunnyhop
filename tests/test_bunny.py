import argparse
import datetime
import unittest
from unittest import mock
from envs import env
from bunnyhop import Bunny
import base64

BUNNYCDN_API_KEY = env('BUNNYCDN_API_KEY')
BUNNYCDN_TEST_STORAGE_ZONE = env('BUNNYCDN_TEST_STORAGE_ZONE')
BUNNYCDN_TEST_STORAGE_ZONE_NAME = env('BUNNYCDN_TEST_STORAGE_ZONE_NAME')
BUNNYCDN_TEST_PULL_ZONE = env('BUNNYCDN_TEST_PULL_ZONE')


class TestBilling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = Bunny('BUNNYCDN_STREAM_API_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_get(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "Balance": 100.10,
            "ThisMonthCharges": 100.10,
            "BillingRecords": ['asdf'],
            "MonthlyChargesStorage": 100.10,
            "MonthlyChargesEUTraffic": 10.10,
            "MonthlyChargesUSTraffic": 10.10,
            "MonthlyChargesASIATraffic": 10.10,
            "MonthlyChargesSATraffic":10.10,
        }

        response = self.b.Billing.get()
        self.assertEqual(response.Balance, 100.10)

    def test_apply_code(self):
        self.patcher.return_value.status_code.return_value = 404
        self.patcher.return_value.json.return_value = {
            'ErrorKey': 'code.invalid'
        }
        
        response = self.b.Billing.apply_code('dummy-code')
        self.assertEqual(response['ErrorKey'], 'code.invalid')


class TestStats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny('BUNNYCDN_STREAM_API_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_get(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "TotalBandwidthUsed": 100,
            "TotalRequestsServed": 100,
            "CacheHitRate": 100.10,
            "BandwidthUsedChart": {'test-obj': 'obj'},
            "BandwidthCachedChart": {'test-obj': 'obj'},
            "CacheHitRateChart": {'test-obj': 'obj'},
            "RequestsServedChart": {'test-obj': 'obj'},
            "PullRequestsPulledChart": {'test-obj': 'obj'},
            "OriginShieldBandwidthUsedChart": {'test-obj': 'obj'},
            "OriginShieldInternalBandwidthUsedChart": {'test-obj': 'obj'},
            "UserBalanceHistoryChart":{'test-obj': 'obj'},
            "GeoTrafficDistribution": {'test-obj': 'obj'},
            "Error3xxChart": {'test-obj': 'obj'},
            "Error4xxChart": {'test-obj': 'obj'},
            "Error5xxChart": {'test-obj': 'obj'},
        }

        response = self.b.Stats.get()
        self.assertEqual(response.TotalBandwidthUsed, 100)


class TestPurge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny('BUNNYCDN_STREAM_API_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_create(self):
        self.patcher.return_value.status_code.return_value = 404
        self.patcher.return_value.json.return_value = {
            "ErrorKey": "purge.hostname_not_found",
            "Field": "Hostname",
            "Message": "The requested hostname was not found"
        }

        response = self.b.Purge.create("http://non-existentmyzone.b-cdn.net/")
        self.assertEqual(response['ErrorKey'], 'purge.hostname_not_found')


class TestStorageZone(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny('BUNNYCDN_STREAM_API_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_get(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "Id": 1,
            "UserId": "string",
            "Name": BUNNYCDN_TEST_STORAGE_ZONE,
            "Password": "string",
            "DateModified": datetime.datetime.now(),
            "Deleted": False,
            "StorageUsed": 1,
            "FilesStored": 1,
            "Region": "string",
            "ReplicationRegions": [],
            "PullZones": [],
            "ReadOnlyPassword": "string"
        }
        response = self.b.Storage.get(BUNNYCDN_TEST_STORAGE_ZONE)
        self.assertEqual(BUNNYCDN_TEST_STORAGE_ZONE_NAME, response.Name)

    def test_delete(self):
        self.patcher.return_value.status_code.return_value = 404
        self.patcher.return_value.json.return_value = {
            "ErrorKey": "storageZone.not_found",
            "Field": "StorageZone",
            "Message": "The requested storage zone was not found"
        }

        response = self.b.Storage.delete(1111)
        self.assertEqual(response['ErrorKey'], 'storageZone.not_found')

    def test_create(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "Id": 1111,
            "UserId": "user_id",
            "Name": BUNNYCDN_TEST_STORAGE_ZONE_NAME,
            "Password": "password",
            "DateModified": "2020-04-14T20:21:45",
            "Deleted": False,
            "StorageUsed": 851993,
            "FilesStored": 9,
            "Region": "DE",
            "ReplicationRegions": [],
            "PullZones": [],
            "ReadOnlyPassword": "password"
        }

        response = self.b.Storage.create(1)
        self.assertEqual(response.Name, BUNNYCDN_TEST_STORAGE_ZONE_NAME)

    def test_all(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = [{
            "Id": 1111,
            "UserId": "user_id",
            "Name": BUNNYCDN_TEST_STORAGE_ZONE_NAME,
            "Password": "password",
            "DateModified": "2020-04-14T20:21:45",
            "Deleted": False,
            "StorageUsed": 851993,
            "FilesStored": 9,
            "Region": "DE",
            "ReplicationRegions": [],
            "PullZones": [],
            "ReadOnlyPassword": "password"
        }]
        response = self.b.Storage.all()
        self.assertIsInstance(response, list)


class TestZone(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = Bunny('BUNNYCDN_STREAM_API_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_get(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "Id": 1111,
            "Name": "pullzone",
            "OriginUrl": "https://dummy-url",
            "Enabled": True
        }
        response = self.b.Zone.get(1111)
        self.assertEqual(response.Id, 1111)

    def test_list(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = [{
            "Id": 1111,
            "Name": "pullzone",
            "OriginUrl": "https://dummy-url",
            "Enabled": True
        }]
        response = self.b.Zone.list()
        self.assertIsInstance(response, list)

    def test_delete(self):
        self.patcher.return_value.status_code.return_value = 404
        self.patcher.return_value.json.return_value = {
            "ErrorKey": "pullzone.not_found",
            "Field": "PullZone",
            "Message": "The requested pull zone was not found"
        }
        response = self.b.Zone.delete('test')
        self.assertEqual(response['ErrorKey'], 'pullzone.not_found')

    def test_purge(self):
        self.patcher.return_value.status_code.return_value = 404
        self.patcher.return_value.json.return_value = {
            "ErrorKey": "pullzone.not_found",
            "Field": "PullZone",
            "Message": "The requested pull zone was not found"
        }
        response = self.b.Zone.purge('test')
        self.assertEqual(response['ErrorKey'], 'pullzone.not_found')

