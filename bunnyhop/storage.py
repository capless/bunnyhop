import requests


class File:
    """
    Represents a file in a BunnyCDN storage zone.
    {'Guid': 'f33f3c52-1899-412b-8ac3-ae4b09edeb09', 'StorageZoneName': 'test-storage-qwigo-a', 'Path': '/test-storage-qwigo-a/', 'ObjectName': 'pfunk-screenshot-2.png', 'Length': 141610, 'LastChanged': '2023-03-30T21:50:15.582', 'ServerId': 426, 'ArrayNumber': 0, 'IsDirectory': False, 'UserId': '82dde7ba-797c-47e0-bbba-28c7243741d8', 'ContentType': '', 'DateCreated': '2023-03-30T21:50:15.582', 'StorageZoneId': 255866, 'Checksum': '6B402E879C5EE7A6B3C818372E61D3B4B8103A4D4B7F4CE7DD8AB4395EE0BE43', 'ReplicatedZones': 'LA,SE,DE,UK,SYD,BR,SG,JH'}
    """

    def __init__(self, Guid: str = "", StorageZoneName: str = "", Path: str = "", ObjectName: str = "", Length: int = 0,
                 LastChanged: str = "", ServerId: int = 0, ArrayNumber: int = 0, IsDirectory: bool = False,
                 UserId: str = "", ContentType: str = "", DateCreated: str = "", StorageZoneId: int = 0,
                 Checksum: str = "", ReplicatedZones: str = "", access_key: str = "", storage_zone_name: str = "",
                 region: str = ""):
        self.name = StorageZoneName
        self.path = Path
        self.is_dir = IsDirectory
        self.length = Length
        self.last_changed = LastChanged
        self.server_id = ServerId
        self.array_number = ArrayNumber
        self.user_id = UserId
        self.content_type = ContentType
        self.date_created = DateCreated
        self.storage_zone_id = StorageZoneId
        self.checksum = Checksum
        self.replicated_zones = ReplicatedZones
        self.guid = Guid
        self.object_name = ObjectName
        self.access_key = access_key
        self.storage_zone_name = storage_zone_name
        self.region = region

    def download(self, dest_path: str) -> bool:
        """
        Download the file to the specified destination path.

        :param dest_path: The path to save the downloaded file.
        :return: True if the file was downloaded successfully, False otherwise.
        """
        url = self._get_url()
        response = requests.get(url, headers={"AccessKey": self.access_key})

        if response.status_code != 200:
            raise Exception(response.content)

        with open(dest_path, "wb+") as file:
            file.write(response.content)

        return True

    def delete(self) -> bool:
        """
        Delete the file from the storage zone.

        :return: True if the file was deleted successfully, False otherwise.
        """
        url = self._get_url()
        response = requests.delete(url, headers={"AccessKey": self.access_key})

        if response.status_code != 200:
            return False

        return True

    def _get_url(self) -> str:
        """
        Get the URL for the file in the storage zone.

        :return: The URL for the file.
        """
        url = f"https://{self.region}storage.bunnycdn.com/{self.storage_zone_name}/{self.object_name}"
        return url
    
    def __repr__(self):
        return f"<File {self.object_name}>"


class Storage:
    """
    A Python library for interacting with the BunnyCDN Storage API.
    """

    def __init__(self, access_key: str, storage_zone_name: str, region: str = ""):
        self.access_key = access_key
        self.storage_zone_name = storage_zone_name
        if region not in ["", "CZ", "UK", "ES", "SE", "NY", "MI", "SG", "HK", "LA", "BR", "SYD", "WA", "JP"]:
            raise ValueError("Invalid region.")
        if region != "":
            region = f"{region}."
        self.region = region

    def list_files(self, path: str = "") -> list[File]:
        """
        List the files and directories in the specified directory.

        :param path: The path to list. Defaults to the root directory.
        :return: A list of File objects.
        """
        if path == "":
            url = f"https://{self.region}storage.bunnycdn.com/{self.storage_zone_name}/"
        else:
            url = f"https://{self.region}storage.bunnycdn.com/{self.storage_zone_name}/{path}/"
        response = requests.get(url, headers={"AccessKey": self.access_key})

        if response.status_code != 200:
            raise Exception(response.content)

        files = []
        for item in response.json():
            file = File(access_key=self.access_key, storage_zone_name=self.storage_zone_name, region=self.region,
                        **item)
            files.append(file)

        return files


class StorageZone:
    pass
