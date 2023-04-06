from bunnyhop.abuse import Abuse
from bunnyhop.billing import Billing
from bunnyhop.compute import Compute
from bunnyhop.countries import CountryAPI
from bunnyhop.pull_zone import PullZone


class Bunny:
    def __init__(self, api_key):
        self.api_key = api_key
        self.Abuse = Abuse(self.api_key)
        self.Country = CountryAPI(self.api_key)
        self.Billing = Billing(self.api_key)
        self.PullZone = PullZone(self.api_key)
        self.Compute = Compute(self.api_key)
