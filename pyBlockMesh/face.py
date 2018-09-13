from collections.abc import MutableMapping
from enum import Enum




class Face(MutableMapping):
    instances = []
    patchTypes = Enum('patchType', 'patch wall symmetryPlane symmetry empty wedge cyclic cyclicAMI processor')

    def __init__(self,vertices=[],
                 name=None,
                 patchType=None,
                 *args, **kw):

        if vertices is []:
            raise ValueError("In order to define a face, you must provide vertices")
        if name is None:
            raise ValueError("A face must have a name")
        if patchType is None:
            patchType = 'patch'

        self._storage = dict(patchType=patchType,
                             name=name,
                             *args, **kw)
        self._storage["vertices"] = {}
        self._storage["vertices"][0] = vertices[0]
        self._storage["vertices"][1] = vertices[1]
        self._storage["vertices"][2] = vertices[2]
        self._storage["vertices"][3] = vertices[3]

        Face.instances.append(self)

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
    def __repr__(self):
        faceName = self["name"]
        patchString = self["patchType"]
        verticesNumberString = "( " + " ".join([str(vertex["name"]) for vertex in [self["vertices"][i] for i in range(0,4)]]) + " )"
        string = faceName + "\n{\n    type " + patchString + ";\n    faces\n    (\n        " + verticesNumberString + " \n    );\n}"
        return string

    @classmethod
    def list_all(cls):
        string = "\nboundary\n(" + "\n" + "\n".join([str(face) for face in cls.instances]) + "\n)"
        return string

