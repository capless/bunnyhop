import argparse
from bunnyhop.core import BunnyStream
import unittest
from unittest import mock
from envs import env
from bunnyhop import Bunny, BunnyStream
import base64

BUNNYCDN_STREAM_API_KEY = env('BUNNY_STREAM_API_KEY')
BUNNYCDN_STREAM_LIBRARY_KEY = env('BUNNYCDN_STREAM_LIBRARY_KEY')


class TestStreamCollection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = BunnyStream('BUNNYCDN_STREAM_API_KEY',
                            'BUNNYCDN_STREAM_LIBRARY_KEY')
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
        response = self.b.StreamCollection.update(
            updated_name, 'collection-id')
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


class TestVideo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.b = BunnyStream('BUNNYCDN_STREAM_API_KEY',
                            'BUNNYCDN_STREAM_LIBRARY_KEY')
        cls.mock = mock.patch('bunnyhop.base.requests.request', autospec=True)
        cls.patcher = cls.mock.start()

    @classmethod
    def tearDownClass(cls):
        cls.b = None
        cls.mock.stop()

    def test_create(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "videoLibraryId": 000, "guid": "0000",
            "title": "unittest-video",
            "dateUploaded": "2021-09-17T06:43:56.0437666Z",
            "views": 0, "isPublic": False,
            "length": 0, "status": 0,
            "framerate": 0, "width": 0,
            "height": 0, "availableResolutions": None,
            "thumbnailCount": 0, "encodeProgress": 0,
            "storageSize": 0, "captions": [],
            "hasMP4Fallback": False, "collectionId": "0000",
            "thumbnailFileName": "thumbnail.jpg"
        }

        name = 'unittest-video'
        collection_id = '0000'
        response = self.b.Video.create(name, collection_id)
        self.assertEqual(response.title, name)

    @mock.patch("builtins.open", create=True)
    def test_upload(self, mock):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        with open('test.mp4', 'rb') as file:
            response = self.b.Video.upload(file, 'VIDEO_GUID')
        self.assertTrue(response.get('success'))

    def test_get(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            "videoLibraryId": 000, "guid": "0000",
            "title": "unittest-video",
            "dateUploaded": "2021-09-17T06:43:56.0437666Z",
            "views": 0, "isPublic": False,
            "length": 0, "status": 0,
            "framerate": 0, "width": 0,
            "height": 0, "availableResolutions": None,
            "thumbnailCount": 0, "encodeProgress": 0,
            "storageSize": 0, "captions": [],
            "hasMP4Fallback": False, "collectionId": "0000",
            "thumbnailFileName": "thumbnail.jpg"
        }

        guid = '0000'
        response = self.b.Video.get(guid)
        self.assertEqual(response.guid, guid)

    def test_list(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'totalItems': 18,
            'currentPage': 1,
            'itemsPerPage': 10,
            'items': []}

        response = self.b.Video.all()
        self.assertEqual(response.get('currentPage'), 1)

    def test_fetch(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        url = 'https://not-a-real-domain.com/video.mp4'
        response = self.b.Video.fetch(url=url, headers={}, video_id='0000')
        self.assertTrue(response.get('success'))

    def test_update(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        title = 'updated_title'
        collection_id = '0000'
        video_id = '0000'
        response = self.b.Video.update(title, collection_id, video_id)
        self.assertTrue(response.get('success'))

    def test_delete(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        video_id = '0000'
        response = self.b.Video.delete(video_id)
        self.assertTrue(response.get('success'))

    def test_set_thumbnail(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        thumbnail_url = 'https://not-a-real-domain.com/thumbnail.jpg'
        video_id = '0000'
        response = self.b.Video.set_thumbnail(thumbnail_url, video_id)
        self.assertTrue(response.get('success'))

    @mock.patch("builtins.open", create=True)
    def test_add_captions(self, mock):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        srclang = 'en'
        label = 'test'
        video_id = '0000'
        cc_to_upload = base64.b64encode('1. A captions file'.encode('ascii'))
        response = self.b.Video.add_caption(srclang, label, cc_to_upload, video_id)
        self.assertTrue(response.get('success'))

    def test_delete_captions(self):
        self.patcher.return_value.status_code.return_value = 200
        self.patcher.return_value.json.return_value = {
            'success': True, 'message': 'OK', 'statusCode': 200}

        srclang = 'en'
        video_id = '0000'
        response = self.b.Video.delete_caption(srclang, video_id)
        self.assertTrue(response.get('success'))
