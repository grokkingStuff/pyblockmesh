from pyblockmesh.vertex import Vertex
from pyblockmesh.hexahedron import Hexahedron
from pyblockmesh.edge import Edge
from pyblockmesh.face import Face

def buildBlockMesh():
    v = Vertex.list_all()
    b = Hexahedron.list_all()
    e = Edge.list_all()
    f = Face.list_all
    return "\n".join([v,b,e,f])
