import unittest
from bunnyhop import Bunny
import os
import json

class Test_GettingStarted(unittest.TestCase):
    def setUp(self):
        briansApiKey= '9dab205f-dfcc-4209-880e-6c29fbc7a074ec051656-894c-4617-8c64-79770aa1f4b1'
        b = Bunny(briansApiKey)
        self.b = b

    def tearDown(self):
        self.b = None

    def test_ListPullZone(self):
        # Arrange
        from bunnyhop.zone import Zone

        # Act
        l = self.b.Zone.list()

        # Assert
        self.assertIsInstance(l,list)
        self.assertIsInstance(l[0], Zone)

    def test_GetAPullZone(self):
        # Arrange
        from bunnyhop.zone import Zone
        goodwebsiteAId = 164657

        # Act
        zone = self.b.Zone.get(id=goodwebsiteAId)
        
        # Assert
        self.assertIsInstance(zone, Zone)
        self.assertEqual(zone.Id, goodwebsiteAId)

    def test_CreateAPullZone(self):
        # Arrange
        name = 'testZone'
        testType = 0
        originUrl = 'https://testZone.org'
        storageZoneId = 'testStorageZoneId' 

        # Act
        self.b.Zone.create(
                Name=name,
                Type=testType, # 0 = Standard and 1 = High Volume
                OriginUrl=originUrl,
                StorageZoneId=storageZoneId)
        testList = self.b.Zone.list()
        testId = testList[-1].Id
        
        # Assert
        testzone = self.b.Zone.get(id=testId)
        self.assertEqual(testzone.Name, name)
        self.assertEqual(testzone.Type, type)
        self.assertEqual(testzone.OriginUrl, originUrl)
        self.assertEqual(testzone.StorageZoneId, storageZoneId)
        testzone.delete()

    def test_UploadAndGetWithBrotli(self):
        # Arrange
        DEST_PATH = ""
        FILE_NAME = "test123.json"
        LOCAL_PATH = ""
        storage = b.Storage.all()[0]

        with open(os.path.join(LOCAL_PATH, FILE_NAME)) as json_file:
                DATA = json_file

        # Act
        storage.upload_file(DEST_PATH,FILE_NAME,LOCAL_PATH,use_brotli=True)
        result = storage.get("test123.brotli")
        
        # Assert
        self.assertEqual(result, DATA)


    def test_CreateJsonWithBrotli(self):
        # Arrange
        TEST_DICT= {"Hello":"World", "first-name":"Ronald", "last-name":"Mcdonald"}
        KEY= "test"
        storage = b.Storage.all()[0]

        # Act
        storage.create_json(KEY, TEST_DICT, use_brotli=True)
        result = storage.get(f"{KEY}.brotli")
        
        # Assert
        self.assertEqual(result, json.dumps(TEST_DICT))


if __name__ == "__main__":
    unittest.main()
