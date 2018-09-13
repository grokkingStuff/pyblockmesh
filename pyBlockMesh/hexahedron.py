import vertex as v
import edge as e

from collections.abc import MutableMapping
class Hexahedron(MutableMapping):
    instances = []

    def __init__(self,vertices,numberOfCells,*args,**kw):

        # Tests or Assertions here to ensure that everything makes sense.
        # Will do later
        self._storage = dict(numberOfCells=numberOfCells,
                             *args,**kw)

        self._storage["vertices"]={}
        self._storage["vertices"][0] = vertices[0]
        self._storage["vertices"][1] = vertices[1]
        self._storage["vertices"][2] = vertices[2]
        self._storage["vertices"][3] = vertices[3]
        self._storage["vertices"][4] = vertices[4]
        self._storage["vertices"][5] = vertices[5]
        self._storage["vertices"][6] = vertices[6]
        self._storage["vertices"][7] = vertices[7]

        self._storage["edges"] = {}
        Hexahedron.instances.append(self)

    def __getitem__(self, key):
        return self._storage[key]
    def __iter__(self):
        return iter(self._storage)
    def __len__(self):
        return len(self._storage)
    def __setitem__(self, key, value):
        self._storage[key] = value
    def __delitem__(self, key):
        del self._storage[key]
    def __repr__(self):
        list_of_vertices = [self["vertices"][0],self["vertices"][1],self["vertices"][2],self["vertices"][3],
                            self["vertices"][4],self["vertices"][5],self["vertices"][6],self["vertices"][7]]

        v.Vertex.assign_names()
        prefix_string = "hex"
        vertex_string = " ".join([vertex["name"] for vertex in list_of_vertices])
        numberCells_string = "( " + " ".join(str(i) for i in self["numberOfCells"]) + " )"
        return " ".join([prefix_string,vertex_string,numberCells_string])

    def add_edge(self,*args,**kwargs):
        edge = e.Edge(*args,**kwargs)
        list_of_vertices = [self["vertices"][0],self["vertices"][1],self["vertices"][2],self["vertices"][3],
                            self["vertices"][4],self["vertices"][5],self["vertices"][6],self["vertices"][7]]

        # Ensure that the vertices are actually part of the hexahedron. This is important enough for us to throw an error.
        try:
            indexv1 = list_of_vertices.index(edge["vertex1"])
            indexv2 = list_of_vertices.index(edge["vertex2"])

            assert -1 < indexv1 < 8
            assert -1 < indexv2 < 8
        except ValueError:
            raise ValueError("The vertices given are not part of the hexahedron. Please check your vertices")

        # Now that we know the edge is actually part of the hexahedron, it is time to check if it is a valid edge

        edgeDict = {}     # This is a poor approximation of a directed graph but it works
        edgeDict[0] = {}
        edgeDict[1] = {}
        edgeDict[2] = {}
        edgeDict[3] = {}
        edgeDict[4] = {}
        edgeDict[5] = {}
        edgeDict[6] = {}
        edgeDict[7] = {}
        edgeDict[0][1] = 0
        edgeDict[3][2] = 1
        edgeDict[7][6] = 2
        edgeDict[4][5] = 3
        edgeDict[0][3] = 4
        edgeDict[1][2] = 5
        edgeDict[5][6] = 6
        edgeDict[4][7] = 7
        edgeDict[0][4] = 8
        edgeDict[1][5] = 9
        edgeDict[2][6] = 10
        edgeDict[3][7] = 11

        temp = edgeDict.get(indexv1,None)
        if temp is not None:
            edgeNumber = temp.get(indexv2,None)
        else:
            temp = edgeDict.get(indexv2,None)
            if temp is not None:
                edgeNumber = temp.get(indexv1,None)

        if edgeNumber is None:
            raise ValueError("The vertices given are not adjacent, ie they cannot form an edge.")


        self["edges"][edgeNumber] = edge

    @classmethod
    def list_all(cls):
        string = "\nblocks\n(" + "\n    " + "\n    ".join([str(hexahedron) for hexahedron in cls.instances]) + "\n)"
        return string
