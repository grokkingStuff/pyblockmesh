from collections.abc import MutableMapping
class Vertex(MutableMapping):
    def __init__(self, x=None, y=None, z=None, name=None, *args, **kw):
        if x is None or y is None or z is None:
            raise ValueError("(x,y,z) cannot contain null values")
        self._storage = dict(x=x,y=y,z=z,name=name,*args, **kw)
        self.x = self._storage["x"]
        self.y = self._storage["y"]
        self.z = self._storage["z"]
        self.name = self._storage["name"]

    def __getitem__(self, key):
        return self._storage[key]
    def __setitem__(self, key, value):
        self._storage[key] = value
    def __delitem__(self, key):
        del self._storage[key]
    def __len__(self):
        return len(self._storage)
    def __iter__(self):
        return iter(self._storage)
    def __len__(self):
        return len(self._storage)
    def __repr__(self):
        string = "("+str(self["x"])+" "+str(self["y"])+" "+str(self["z"])+")"
        return string
    def __eq__(self, other):
        if type(other) is type(self):
            if self["x"] is other["x"] and self["y"] is other["y"] and self["z"] is other["z"]:
               return True
        else:
            return False
    def __add__(self, other):
        return Vertex(self["x"] + other["x"],
                      self["y"] + other["y"],
                      self["z"] + other["z"])

    def __sub__(self, other):
        return Vertex(self["x"] - other["x"],
                      self["y"] - other["y"],
                      self["z"] - other["z"])

