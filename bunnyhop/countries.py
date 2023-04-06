import requests
from datetime import datetime

from bunnyhop.base import convert_dict_keys, Record, APIKeyRecord


class Country(Record):
    """An API for managing countries and tax rates in BunnyCDN.

    Attributes:
        id (int): The ID of the country.
        name (str): The name of the country.
        last_modified (datetime): The date and time the country was last modified.
        script_type (int): The script type of the country.
        current_release_id (int): The current release ID of the country.
        edge_script_variables (list): A list of edge script variables for the country.
    """

    def __repr__(self):
        """Return a string representation of the Country object.

        Returns:
            A string representation of the Country object.
        """
        return f"<Country {self.name}>"

class CountryAPI(APIKeyRecord):
    """An API for managing countries and tax rates in BunnyCDN.
    """

    def __init__(self, api_key):
        """Initialize the Country API.

        Args:
            api_key (str): BunnyCDN's API key.
        """
        self.api_key = api_key

    def list_countries(self):
        """List all countries and tax rates.

        Returns:
            A list of Country objects.
        """
        path = '/country'
        headers = {'AccessKey': self.api_key}
        data = self._make_request('GET', path, headers=headers)
        return [Country(country_dict) for country_dict in data]
