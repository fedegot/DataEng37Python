class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(Latitude={self.latitude}, longitude={self.longitude})"
    # alternative to <__main__.Location object at 0x0000020BD0EB1A50>

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"
    # alternative to <__main__.Location object at 0x0000020BD0EB1A50>


bham_academy = Location(latitude=52.488647, longitude=-1.887249)
print(bham_academy)
print(repr(bham_academy))
