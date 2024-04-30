import logging
from collections import namedtuple
from typing import NamedTuple

logger = logging.getLogger(__name__)


class Coordinate:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


Coordinate1 = namedtuple("Coordinate1", 'lat lon')
Coordinate2 = NamedTuple("Coordinate2", [('lat', float), ('lon', float)])


class Coordinate3(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'


# namedtuple accepts the defaults keyword-only argument providing an iterable of N default
# values for each of the N rightmost fields of the class.
# so the defaults specify reference default value.
Coordinate5 = namedtuple("Coordinate5", 'lat long reference', defaults=['WGS84'])

City = namedtuple('City', 'name country population coordinates')
