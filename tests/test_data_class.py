import json
import typing

from fluent_python.data_class import Coordinate, Coordinate1, Coordinate2, Coordinate3, City


class Test:

    def test_coordinate(self):
        moscow = Coordinate(55.76, 37.62)
        location = Coordinate(55.76, 37.62)
        assert moscow != location
        assert (moscow.lat, moscow.lon) == (location.lat, location.lon)

    def test_coordinate1(self):
        moscow = Coordinate1(55.76, 37.62)
        print(moscow)
        print(moscow._asdict())
        print(moscow._fields)
        assert moscow == Coordinate1(55.76, 37.62)

    def test_coordinate2(self):
        moscow = Coordinate2(55.76, 37.62)
        print(typing.get_type_hints(Coordinate2))
        assert moscow == Coordinate2(55.76, 37.62)
        print(moscow._asdict())
        print(moscow._fields)
        print(moscow._replace(lat=1)._asdict())
        print(Coordinate2.__annotations__)

    def test_coordinate3(self):
        trash = Coordinate3("Ni", None)
        print(trash)
        print(Coordinate3.__annotations__)

        print(Coordinate3._field_defaults)

    def test_city(self):
        tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
        print(tokyo.population)
        print(tokyo.coordinates)

        delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate1(28.613889, 77.208889))
        delhi = City._make(delhi_data)
        print(delhi._asdict())
        print(json.dumps(delhi._asdict()))



