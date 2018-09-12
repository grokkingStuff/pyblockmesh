from collections.abc import Mapping

from enum import Enum     # for enum34, or the stdlib version
# from aenum import Enum  # for the aenum version



class Edge(Mapping):
    edgeTypes = Enum('edgeType', 'arc spline polyLine BSpline line')

    def __init__(self,
                 vertex1,
                 vertex2,
                 expansionRatio = None,
                 keyword = None,
                 interpolationPoints = None,
                 *args,**kwargs):
        self._storage = dict(vertex1 = vertex1,
                             vertex2 = vertex2,
                             *args,**kwargs)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        if expansionRatio is None:
            self.expansionRatio = 1
        else:
            self.expansionRatio = expansionRatio
        if keyword is None:
            self.keyword = Edge.edgeTypes.line
        elif keyword not in Edge.edgeTypes._member_names_:
            raise ValueError("keyword must be a valid edge type")
        else:
            self.keyword = Edge.edgeTypes[keyword]
            self.interpolationPoints = interpolationPoints



    def __getitem__(self, key):
        return self._storage[key]
    def __iter__(self):
        return iter(self._storage)
    def __len__(self):
        return len(self._storage)
    def __repr__(self):
        edgeType = self.keyword.name
        v1Name = str(self.vertex1["name"])
        v2Name = str(self.vertex2["name"])
        points = str(self.interpolationPoints)
        return " ".join[edgeType,v1Name,v2Name,points]
