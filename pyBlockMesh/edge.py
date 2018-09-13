from collections.abc import Mapping, MutableMapping

from enum import Enum     # for enum34, or the stdlib version
# from aenum import Enum  # for the aenum version



class Edge(MutableMapping):
    instances = []
    edgeTypes = Enum('edgeType', 'arc spline polyLine BSpline line')

    def __init__(self,
                 vertex1,
                 vertex2,
                 expansionRatio = None,
                 keyword = None,
                 interpolationPoints = [],
                 *args,**kwargs):

        self._storage = dict(vertex1 = vertex1,
                             vertex2 = vertex2,
                             expansionRatio = expansionRatio
                             keyword = keyword
                             *args,**kwargs)

        # Assign expansionRatio
        if expansionRatio is None:
            self["expansionRatio"] = 1
        else:
            self.["expansionRatio"] = expansionRatio

        # Default keyword is 'line'
        # The interpolation points are vertices
        if keyword is None:
            self["keyword"] = Edge.edgeTypes.line.name
            self.["interpolationPoints"] = []
        elif keyword not in Edge.edgeTypes._member_names_:
            raise ValueError("keyword must be a valid edge type")
        else:
            self["keyword"] = Edge.edgeTypes[keyword].name
            self["interpolationPoints"] = interpolationPoints

        Edge.instances.append(self)

    def __getitem__(self, key):
        return self._storage[key]
    def __iter__(self):
        return iter(self._storage)
    def __setitem__(self, key, value):
        self._storage[key] = value
    def __delitem__(self, key):
        del self._storage[key]
    def __len__(self):
        return len(self._storage)
    def __repr__(self):
        edgeType = self["keyword"]
        v1Name = str(self["vertex1"]["name"])
        v2Name = str(self["vertex2"]["name"])

        if type(self["interpolationPoints"]) is type([]):
            if self["interpolationPoints"] is not []:
                # Multiple interpolation points
                points = "( " + " ".join([str(point) for point in self["interpolationPoints"]]) + " )"
            else:
                # No interpolation points
                points = ""
        else:
            # Single interpolationPoint
            points = str(self.interpolationPoints)

        return " ".join[edgeType,v1Name,v2Name,points]


    @classmethod
    def list_all(cls):
        string = "\nedges\n(" + "\n    " + "\n    ".join([str(edge) for edge in cls.instances]) + "\n)"
        return string
