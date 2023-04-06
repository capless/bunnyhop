import datetime
import re

import requests


def pascal_to_snake(s: str):
    """
    Convert a string from PascalCase to snake_case.
    Args:
        s (str): A string in PascalCase.
    """
    s = s.replace(' ', '_')
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    snake_case = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s).lower()
    return snake_case


def convert_datetime_str(d: str):
    """
    Convert a datetime string to a datetime object.
    Args:
        d (str): A datetime string.
    """
    try:
        return datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        try:
            return datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            return d


def convert_dict_keys(d: dict):
    """
    Convert the keys of a dictionary from PascalCase to snake_case.
    Args:
        d (dict): A dictionary with keys in PascalCase.
    """

    cd = {pascal_to_snake(k): v for k, v in d.items()}
    if 'last_modified' in cd:
        cd['last_modified'] = convert_datetime_str(cd['last_modified'])
    return cd


class Record(object):
    """Base class for all Bunnyhop records."""

    def __init__(self, data: dict):
        """
        Record constructor.
        Attributes:
            id (str): The record id.
            last_modified (datetime): The last modified time.
        """
        self.__dict__.update(convert_dict_keys(data))

    def __repr__(self):
        if hasattr(self, 'id'):
            return f'<{self.__class__.__name__}({self.id})>'
        else:
            return f'<{self.__class__.__name__}>'

    def __iter__(self):
        return iter(self.__dict__.get('objects', []))

    def __len__(self):
        return len(self.__dict__.get('objects', []))

    def __getitem__(self, key):
        return self.__dict__.get('objects', [])[key]

class APIKeyRecord(Record):
    """Base class for all Bunnyhop API key records."""

    API_BASE_URL = 'https://api.bunny.net'

    def __init__(self, api_key: str, data: dict = {}):
        """
        APIKeyRecord constructor.
        Args:
            api_key (str): BunnyCDN's API key.
            data (dict): A dict representation of a record.
        Attributes:
            api_key (str): BunnyCDN's API key.
        """
        super().__init__(data)
        self.api_key = api_key

    def _make_request(self, method, path, headers={}, **kwargs):
        """Make an API request to BunnyCDN.
        Args:
            method (str): The API method (GET, POST, etc.).
            path (str): The API endpoint.
            **kwargs: Additional keyword arguments to pass to the request.
        Returns:
            The response object from the API request.
        """
        headers.update({'AccessKey': self.api_key})
        url = f'{self.API_BASE_URL}{path}'
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()
