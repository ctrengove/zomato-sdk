from core.modules.base_module import BaseModule
from core.modules.Fundamentals.location_details import LocationDetails
from core.modules.Fundamentals.locations import Locations


class Location(BaseModule):
    def __init__(self, API_KEY="", requester=None):
        super().__init__(API_KEY, requester)

    def get_location_details(self, entity_id, entity_type, raw=False):
        data, headers = self.r.request('location_details', payload=locals())
        if raw:
            return data
        return LocationDetails(data, headers, self.r)

    def get_cities(self, query="", lat=None, lon=None, count=None, raw=False):
        data, headers = self.r.request('cities', payload=locals())
        if raw:
            return data
        return Locations(data, headers, self.r)
