import json
import os
from io import BytesIO

from envs import env

from bunnyhop import base


class StreamCollection(base.BaseStreamBunny):

    def create(self, name):
        """ Creates a collection in Stream API
        POST -> /library/{libraryId}/collections

        Payload
        -------
        name: str, required
            name of the new collection for Stream API
        """
        pass

    def get(self, library_id, collection_id):
        """ Acquires a single collection in Stream API
        GET -> /library/{libraryId}/collections/{collectionId}

        Payload
        -------
        library_id: int, required
        collection_id: str, required

        Returns
        -------
        """
        pass

    def all(self, library_id, page=1, items_per_page=10, search="", orderBy="date"):
        """ Acquires a list of all collections
        GET -> /library/{library_id}/collections

        Payload
        -------
        library_id: int, required
        page: int, optional, default: 1
        items_per_page: int, optional, default: 10
        search: str, optional
            search using the given param in the list of collection
        orderBy: str, optional, default: 'date'
            fields to order from ['date', ]

        Returns
        -------
        """
        pass

    def update(self, library_id, collection_id):
        """ Updates a collection
        POST -> /library/{libraryId}/collections/{collectionId}

        Payload
        -------
        library_id: int, required
        collection_id: str, required

        Returns
        -------

        """
        pass

    def delete(self, library_id, collection_id):
        """ Deletes a collection
        DELETE -> /library/{libraryId}/collections/{collectionId}

        Payload
        -------
        library_id: int, required
        collection_id: str, required

        Returns
        -------

        """
        pass


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