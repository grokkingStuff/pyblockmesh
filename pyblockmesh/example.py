import hexahedron as h
import vertex as v
import edge as e
import face as f

vertices = [v.Vertex(x,y,z) for x in [-1,1]
                            for y in [-1,1]
                            for z in [-1,1]]


block = h.Hexahedron(vertices,numberOfCells=[1,1,1])
block.add_edge(block['vertices'][0],block['vertices'][1])
block.add_face([block['vertices'][0],
                block['vertices'][1],
                block['vertices'][2],
                block['vertices'][3]]
               ,name="name")

print(h.buildBlockMeshDict())
