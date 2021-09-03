import json
import os
from io import BytesIO

from envs import env

from bunnyhop import base


class StreamCollection(base.BaseStreamBunny):
    videoLibraryId = base.IntegerProperty()
    guid = base.CharProperty()
    name = base.CharProperty()
    videoCount = base.IntegerProperty()
    totalSize = base.IntegerProperty()
    previewVideoIds = base.CharProperty()

    def create(self, name):
        """ Creates a collection in Stream API

        Payload
        -------
        name: str, required
            name of the new collection for Stream API

        Returns
        -------
        response: dict, required
            {
                "videoLibraryId": int,
                "guid": str,
                "name": str,
                "videoCount": int,
                "totalSize": int,
                "previewVideoIds": str
            }
        """
        METHOD = 'POST'
        PATH = f'/library/{self.library_id}/collections'
        response = self.call_api(
            api_url=PATH,
            api_method=METHOD,
            json_data={'name': name}
        )

        if response.get('guid', None):
            return StreamCollection(
                api_key=self.api_key, library_id=self.library_id, **response)
        return response

    def get(self, collection_id):
        """ Acquires a single collection in Stream API

        Payload
        -------
        collection_id: str, required
            guid of a collection which can be acquired by 'all()'

        Returns
        -------
        response: dict, required
            {
                "videoLibraryId": int,
                "guid": str,
                "name": str,
                "videoCount": int,
                "totalSize": int,
                "previewVideoIds": str
            }
        """
        METHOD = 'GET'
        PATH = f'/library/{self.library_id}/collections/{collection_id}'
        response = self.call_api(
            api_url=PATH,
            api_method=METHOD,
        )
        try:
            if response.get('guid', None):
                return StreamCollection(
                    api_key=self.api_key, library_id=self.library_id, **response)
            else:
                return "Stream Collection not found."
        except Exception as err:
            return str(err)

    def all(self, page=1, items_per_page=10, search="", orderBy="date"):
        """ Acquires a list of all collections

        Payload
        -------
        page: int, optional, default: 1
        items_per_page: int, optional, default: 10
        search: str, optional
            search using the given param in the list of collection
        orderBy: str, optional, default: 'date'
            fields to order from ['date', ]

        Returns
        -------
        response: dict, required
            200: { 
                totalItems: int,
                currentPage: int,
                itemsPerPage: int,
                items: arr, dict
                    {
                        "videoLibraryId": int,
                        "guid": str
                        "name": str
                        "videoCount": int
                        "totalSize": int
                        "previewVideoIds": str
                    }
            }
        """
        METHOD = 'GET'
        PATH = f'/library/{self.library_id}/collections'
        response = self.call_api(
            api_url=PATH,
            api_method=METHOD,
            params={
                'page': page,
                'itemsPerPage': items_per_page,
                'search': search,
                'orderBy': orderBy
            }
        )

        return response

    def update(self, name, collection_id=None):
        """ Updates a collection
        
        Payload
        -------
        name: str, required
            updated name of the collection
        collection_id: str, required, default=self.guid

        Returns
        -------
        response: dict, required
            {
                "success": bool,
                "message": str,
                "statusCode": int
            }
        """
        if not collection_id:
            collection_id = self.guid
        METHOD = 'POST'
        PATH = f'/library/{self.library_id}/collections/{collection_id}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
            json_data={
                'name': name
            }
        )

        return response

    def delete(self, collection_id=None):
        """ Deletes a collection

        Payload
        -------
        collection_id: str, optional, default=self.guid
            guid of the collection

        Returns
        -------
        response: dict, required
            {
                "success": bool,
                "message": str,
                "statusCode": int
            }
        """
        if not collection_id:
            collection_id = self.guid
        METHOD = 'DELETE'
        PATH = F'/library/{self.library_id}/collections/{collection_id}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
        )

        return response


class Stream(base.BaseStreamBunny):

    def create(self, library_id, title, collection_id):
        """ Creates a video in Stream API
            NOTE: Must be done before using 'upload()'
        POST -> /library/{library_id}/videos

        Payload
        -------
        library_id: int, required
        title: str, required
            title of the video
        collection_id: str, required
            ID of the collection where the video will be stored

        Returns
        -------
        status_code:
            200: 'The video was successfuly created and returned as the response.'
        """
        pass

    def get(self, library_id, video_id):
        """ Acquires a video  
        GET -> /library/{libraryId}/videos/{videoId}

        Payload
        -------
        library_id: int, required
        video_id, str, required

        Returns
        -------

        """
        pass

    def all(self, library_id, page=1, items_per_page=10, search="", orderBy="date"):
        """ Lists all of video 
        GET -> /library/{libraryId}/videos
        
        Payload
        -------
        library_id: int, required
        page: int, optional, default: 1
        items_per_page: int, optional, default: 10
        search: str, optional
            search using the given param in the list of collection
        collection: str, optional
            collection from which the video originated from
        orderBy: str, optional, default: 'date'
            fields to order from ['date', ]

        Returns
        -------
        """
        pass

    def fetch(self, library_id, video_id, url, headers={}):
        """ Fetches a video 
        POST -> /library/{libraryId}/videos/{videoId}/fetch

        Payload
        -------
        library_id: int, required
        video_id: str, required
        url: str, required
            URL where the video will be fetched
        headers: dict, optional

        Returns
        -------

        """
        pass

    def update(self, library_id, video_id, title, collection_id):
        """ Updates a video 
        POST -> /library/{libraryId}/videos/{videoId}

        Payload
        -------
        library_id: int, required
        video_id: str, required
        title: str, required
            The title of the video
        collection_id: str, required
            ID of the collection where the video belongs

        Returns
        -------

        """
        pass

    def delete(self, library_id, video_id):
        """ Deletes a video
        DELETE -> /library/{libraryId}/videos/{videoId}

        Payload
        -------
        library_id: int, required
        video_id: int, required

        Returns
        -------


        """
        pass

    def upload(self, library_id, video_id):
        """ Uploads a video
            NOTE: Requires you to create the video first via
            the API Create Video endpoint 'create()'

        Payload
        -------
        library_id: int, required
        video_id: int, required
            the video_id created through 'Create Video` endpoint
        
        Returns
        -------

        """
        pass

    def create_and_upload(self):
        """ Utilizes BunnyNet's `Create` and `Upload` video to
            create and post a video in one function
        """
        pass

    def set_thumbnail(self):
        """ Sets a thumbnail for a specific video
        POST -> /library/libraryId/videos/videoId/thumbnail

        Payload
        -------
        library_id: int, required
        video_id: str, required

        Returns
        -------
        """
        pass

    def add_caption(self):
        """ Adds caption to a video 
        POST -> /library/libraryId/videos/videoId/captions/srclang

        Payload
        -------
        library_id: int, required
        video_id: str, required
        srclang: str, required
        label: str, required
            text description label for the caption
        captions_file: string, required
            Base64 encoded captions file

        Returns
        -------
        """
        pass

    def delete_caption(self):
        """ Delete captions in a video 
        DELETE -> /library/libraryId/videos/videoId/captions/srclang

        Payload
        -------
        library_id: int, required
        video_id: str, required
        srclang: str, required

        Returns
        -------

        """
        pass


# TODO: Create a 'Video' object that houses video endpoints (thumbnail, upload, caption)
class Video(object):
    pass
