import requests

from bunnyhop.base import convert_dict_keys, APIKeyRecord, Record


class AbuseSet(Record):
    pass


class Abuse(APIKeyRecord):
    """An API for managing abuse cases in BunnyCDN.

    Attributes:
        api_key (str): BunnyCDN's API key.
    """

    def list_cases(self, page: int = 1, per_page: int = 100):
        """List all abuse cases.

        Args:
            page (int, optional): The page number to get. Defaults to 1.
            per_page (int, optional): The number of cases to get per page. Defaults to 100.

        Returns:
            A list of AbuseCase objects.
        """
        path = f'/abusecase?page={page}&perPage={per_page}'
        data = self._make_request('GET', path)
        data['objects'] = [AbuseCase(self.api_key, case) for case in data['Items']]
        data.pop('Items')
        return AbuseSet(data)


class AbuseCase(APIKeyRecord):
    """An API for managing an individual abuse case in BunnyCDN.

    Attributes:
        api_key (str): BunnyCDN's API key.
    """

    def resolve(self, kind: str):
        """Resolve an abuse case.

        Args:
            kind (str): The type of case to resolve.
        """
        path = f'/abusecase/{self.id}/resolve'
        if kind == 'dmca':
            path = f'/dmca/{self.id}/resolve'
        data = self._make_request('POST', path)
        self.__dict__.update(convert_dict_keys(data))

    def check(self):
        """Check an abuse case.
        """
        path = f'/abusecase/{self.id}/check'
        data = self._make_request('POST', path)
        self.__dict__.update(convert_dict_keys(data))

    def __repr__(self):
        """Return a string representation of the AbuseCase object.

        Returns:
            A string representation of the AbuseCase object.
        """
        return f'<AbuseCase {self.id} - {self.pull_zone_id}>'