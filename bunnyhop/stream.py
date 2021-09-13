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


class Video(base.BaseStreamBunny):

    def create(self, title, collection_id):
        """ Creates a video in Stream API
            NOTE: Must be done before using 'upload()'

        Payload
        -------
        title: str, required
            title of the video
        collection_id: str, required
            ID of the collection where the video will be stored

        Returns
        -------
        status_code:
            200: 'The video was successfuly created and returned as the response.'
        """
        METHOD = 'POST'
        PATH = F'/library/{self.library_id}/videos'

        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
        )

        if response.get('guid', None):
            return Video(
                api_key=self.api_key, library_id=self.library_id, **response)
        return response

    def get(self, video_id):
        """ Acquires a video  

        Payload
        -------
        video_id, str, required

        Returns
        -------

        """
        METHOD = 'GET'
        PATH = F'/library/{self.library_id}/videos/{video_id}'

        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
        )

        try:
            if response.get('guid', None):
                return Video(
                    api_key=self.api_key, library_id=self.library_id, **response)
            else:
                return "Stream Collection not found."
        except Exception as err:
            return str(err)

    def all(self, page=1, items_per_page=10, search="", orderBy="date"):
        """ Lists all of video 

        Payload
        -------
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
        METHOD = 'GET'
        PATH = f'/library/{self.library_id}/videos'
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

    def fetch(self, video_id, url, headers={}):
        """ Fetches a video 
        POST -> /library/{libraryId}/videos/{videoId}/fetch

        Payload
        -------
        video_id: str, required
        url: str, required
            URL where the video will be fetched
        headers: dict, optional

        Returns
        -------

        """
        pass

    def update(self, video_id, title, collection_id):
        """ Updates a video

        Payload
        -------
        video_id: str, required
        title: str, required
            The title of the video
        collection_id: str, required
            ID of the collection where the video belongs

        Returns
        -------

        """
        if not video_id:
            video_id = self.guid
        METHOD = 'POST'
        PATH = f'/library/{self.library_id}/videos/{video_id}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
            json_data={
                'title': title,
                'collection_id': collection_id
            }
        )

        return response

    def delete(self, video_id):
        """ Deletes a video

        Payload
        -------
        video_id: int, required

        Returns
        -------


        """
        if not video_id:
            video_id = self.guid
        METHOD = 'DELETE'
        PATH = F'/library/{self.library_id}/videos/{video_id}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
        )

        return response

    def upload(self,  video_id):
        """ Uploads a video
            NOTE: Requires you to create the video first via
            the API Create Video endpoint 'create()'

        Payload
        -------
        video_id: int, required
            the video_id created through 'Create Video` endpoint

        Returns
        -------

        """
        if not video_id:
            video_id = self.guid
        METHOD = 'PUT'
        PATH = F'/library/{self.library_id}/videos/{video_id}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
        )

        return response

    def create_and_upload(self):
        """ Utilizes BunnyNet's `Create` and `Upload` video to
            create and post a video in one function
        """
        pass

    def set_thumbnail(self, video_id, thumbnail_url):
        """ Sets a thumbnail for a specific video

        Payload
        -------
        video_id: str, required
        thumbnail_url: str, required
            url of the thumbnail for the video

        Returns
        -------
        """
        if not video_id:
            video_id = self.guid
        METHOD = 'POST'
        PATH = f'/library/{self.library_id}/videos/{video_id}/thumbnail'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
            params={
                'thumbnailUrl': thumbnail_url
            }
        )

        return response

    def add_caption(self, video_id, srclang, label, captions_file):
        """ Adds caption to a video 
        POST -> /library/libraryId/videos/videoId/captions/srclang

        Payload
        -------
        video_id: str, required
        srclang: str, required
        label: str, required
            text description label for the caption
        captions_file: string, required
            Base64 encoded captions file

        Returns
        -------
        """
        if not video_id:
            video_id = self.guid
        METHOD = 'POST'
        PATH = F'/library/{self.library_id}/videos/{video_id}/captions/{srclang}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH,
            json_data={
                'srclang': srclang,
                'label': label,
                'captionsFile': captions_file
            }
        )

        return response

    def delete_caption(self, video_id, srclang):
        """ Delete captions in a video 
        DELETE -> /library/libraryId/videos/videoId/captions/srclang

        Payload
        -------
        video_id: str, required
        srclang: str, required

        Returns
        -------

        """
        if not video_id:
            video_id = self.guid
        METHOD = 'DELETE'
        PATH = F'/library/{self.library_id}/videos/{video_id}/captions/{srclang}'
        response = self.call_api(
            api_method=METHOD,
            api_url=PATH
        )

        return response
