

import hexahedron as h
import vertex as v
import face as f
import edge as e


def buildBlockMeshDict():
    v_string = v.Vertex.list_all()
    h_string = h.Hexahedron.list_all()
    e_string = e.Edge.list_all()
    f_string = f.Face.list_all()
    string = "\n".join([v_string,h_string,e_string,f_string])
    return string
