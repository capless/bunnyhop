from bunnyhop.billing import Billing
from bunnyhop.purge import Purge
from bunnyhop.stats import Stats
from bunnyhop.storage import Storage, StorageZone
from bunnyhop.zone import Zone
from bunnyhop.stream import StreamCollection, Stream


class Bunny(object):

    def __init__(self, api_key):
        self.Zone = Zone(api_key)
        self.Purge = Purge(api_key)
        self.Storage = Storage(api_key)
        self.StorageZone = StorageZone(api_key)
        self.Stats = Stats(api_key)
        self.Billing = Billing(api_key)


class BunnyStream(object):
    """  """

    def __init__(self, api_key, library_id):
        self.StreamCollection = StreamCollection(api_key, library_id)
        self.Stream = Stream(api_key, library_id)
