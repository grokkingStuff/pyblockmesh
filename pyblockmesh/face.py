from collections.abc import MutableMapping
from enum import Enum




class Face(MutableMapping):
    patchTypes = Enum('patchType', 'patch wall symmetryPlane symmetry empty wedge cyclic cyclicAMI processor')

    def __init__(self,
                 vertices=[],
                 name=None,
                 patchType=None,
                 *args, **kw):

        if vertices == []:
            raise ValueError("In order to define a face, you must provide vertices")
        if isinstance(vertices,list):
            assert len(vertices) == 4, "Four vertices must be provided to instantiate a face"
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

    def __getitem__(self, key):
        return self._storage[key]
    def __setitem__(self, key, value):
        self._storage[key] = value
    def __delitem__(self, key):
        del self._storage[key]
    def __len__(self):
        return 4
    def __iter__(self):
        return iter([self._storage["vertices"][0],
                     self._storage["vertices"][1],
                     self._storage["vertices"][2],
                     self._storage["vertices"][3]])
    def __eq__(self, other):
        if not isinstance(other,Face):
            return False
        else:
            for vertex in self:
                if vertex not in other['vertices'].values():
                    return False
            if self["patchType"] != other["patchType"]:
                return False
            return True

    def __repr__(self):
        faceName = self["name"]
        patchString = self["patchType"]
        verticesNumberString = "( " + " ".join([str(vertex["name"]) for vertex in [self["vertices"][i] for i in range(0,4)]]) + " )"
        string = faceName + "\n{\n    type " + patchString + ";\n    faces\n    (\n        " + verticesNumberString + " \n    );\n}"
        return string

