import unittest
from bunnyhop import Bunny
import os
import json
import random
import string


def generate_random_string(k=8):
    return ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=k))


class Test_GettingStarted(unittest.TestCase):
    def setUp(self):
        API_KEY = '03a364a5-f9e0-4eb1-b124-5e665be4edc3a8fa433f-e896-4de6-bad6-05582aff37c0'
        b = Bunny(API_KEY)
        self.b = b

    def tearDown(self):
        self.b = None

    def test_a_CreateStorageZone(self):
        # Arrange
        STORAGE_NAME = generate_random_string()
        MAIN_REGION = "NY"
        # Act
        response = self.b.Storage.create(
            name=STORAGE_NAME, main_storage_region=MAIN_REGION)
        # Assert
        self.assertEqual(response.Name, STORAGE_NAME)
        self.assertEqual(response.Region, MAIN_REGION)

    def test_b_ListStorageZone(self):
        # Arrange
        from bunnyhop.storage import StorageZone
        # Act
        response = self.b.Storage.all()
        # Assert
        self.assertIsInstance(response, list)
        if response:
            self.assertIsInstance(response[0], StorageZone)

    def test_c_GetStorageZone(self):
        # Arrange
        TEST_STORAGE_ZONES = self.b.Storage.all()
        TEST_STORAGE_ZONE = TEST_STORAGE_ZONES[0]
        TEST_STORAGE_ZONE_ID = TEST_STORAGE_ZONE.Id

        # Act
        response = self.b.Storage.get(TEST_STORAGE_ZONE_ID)
        # Assert
        self.assertEqual(response.Id, TEST_STORAGE_ZONE_ID)

    def test_d_CreateAPullZone(self):
        # Arrange
        NAME = generate_random_string()
        TEST_TYPE = 1
        ORIGIN_URL = 'https://testZone.org'
        STORAGEZONE_ID = self.b.Storage.all()[0].Id

        # Act
        response = self.b.Zone.create(
            Name=NAME,
            Type=TEST_TYPE,  # 0 = Standard and 1 = High Volume
            OriginUrl=ORIGIN_URL,
            StorageZoneId=STORAGEZONE_ID)

        # Assert
        testzone = self.b.Zone.get(id=response.Id)
        self.assertEqual(testzone.Name, NAME)
        self.assertEqual(testzone.Type, TEST_TYPE)
        self.assertEqual(testzone.OriginUrl, None)
        self.assertEqual(testzone.StorageZoneId, STORAGEZONE_ID)

    def test_e_ListPullZone(self):
        # Arrange
        from bunnyhop.zone import Zone

        # Act
        l = self.b.Zone.list()

        # Assert
        self.assertIsInstance(l, list)
        if l:
            self.assertIsInstance(l[0], Zone)

    def test_f_GetAPullZone(self):
        # Arrange
        TEST_PULLZONES = self.b.Zone.list()
        TEST_PULLZONE = TEST_PULLZONES[0]

        # Act
        response = self.b.Zone.get(TEST_PULLZONE.Id)
        # Assert
        if type(response) is not dict:
            self.assertEqual(response.Id, TEST_PULLZONE.Id)

    def test_g_UploadAndGetWithBrotli(self):
        # Arrange
        DEST_PATH = "test_dest"
        FILE_NAME = "test123.json"
        LOCAL_PATH = "test"
        TEST_STORAGE_ZONES = self.b.Storage.all()
        TEST_STORAGE_ZONE_ID = TEST_STORAGE_ZONES[0].Id
        STORAGE = self.b.Storage.get(TEST_STORAGE_ZONE_ID)

        with open(os.path.join(LOCAL_PATH, FILE_NAME)) as json_file:
            DATA = json.dumps(json.loads(json_file.read()))

        # Act
        response = STORAGE.upload_file(
            DEST_PATH, FILE_NAME, LOCAL_PATH, use_brotli=True)
        result = STORAGE.get(f"{DEST_PATH}/test123.brotli")

        # Assert
        self.assertEqual(result, DATA)

    def test_h_CreateJsonWithBrotli(self):
        # Arrange
        TEST_DICT = {"Hello": "World",
                     "first-name": "Ronald", "last-name": "Mcdonald"}
        KEY = "test"
        TEST_STORAGE_ZONES = self.b.Storage.all()
        TEST_STORAGE_ZONE_ID = TEST_STORAGE_ZONES[0].Id
        STORAGE = self.b.Storage.get(TEST_STORAGE_ZONE_ID)

        # Act
        STORAGE.create_json(KEY, TEST_DICT, use_brotli=True)
        result = STORAGE.get(f"{KEY}.brotli")

        # Assert
        self.assertEqual(result, json.dumps(TEST_DICT))

    def test_i_PurgeEntirePullzone(self):
        # Arrange
        TEST_PULLZONE = self.b.Zone.list()[0]
        # Act
        self.b.Zone.purge(TEST_PULLZONE.Id)
        TEST_PULLZONE.purge(TEST_PULLZONE.Id)
        # Assert

    def test_j_DeleteAPullZone(self):
        # Arrange
        TEST_PULLZONES = self.b.Zone.list()
        TEST_PULLZONE = TEST_PULLZONES[0]

        # Act
        response = self.b.Zone.get(str(TEST_PULLZONE.Id))
        self.b.Zone.delete(str(TEST_PULLZONE.Id))
        # Assert
        self.assertEqual(self.b.Zone.get(
            str(TEST_PULLZONE.Id)), "Zone not found.")

    def test_k_DeleteStorageZone(self):
        # Arrange
        TEST_STORAGEZONES = self.b.Storage.all()
        TEST_STORAGEZONE = TEST_STORAGEZONES[0]
        # Act
        response = self.b.Storage.delete(TEST_STORAGEZONE.Id)
        # Assert
        self.assertEqual(self.b.Storage.get(TEST_STORAGEZONE.Id), b"")


if __name__ == "__main__":
    unittest.main()
