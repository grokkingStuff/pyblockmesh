import pyblockmesh as pbm

from tests import *
from tests.helpers import *

# Unit tests are great but what about property tests?

class TestHexahedron(unittest.TestCase):

    def test_initialization(self):
        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,4,1)
        v3 = pbm.Vertex(1,2,3)
        v4 = pbm.Vertex(1,2,4)
        v5 = pbm.Vertex(2,3,1)
        v6 = pbm.Vertex(2,4,1)
        v7 = pbm.Vertex(2,2,3)
        v8 = pbm.Vertex(2,2,4)

        h1 = pbm.Hexahedron([v1,v2,v3,v4,v5,v6,v7,v8],numberOfCells=[1,2,3])


        # __iter__
        for vertex in h1:
            self.assertEqual(vertex in h1['vertices'],True)

        # __len__
        self.assertEqual(len(h1),8)

        # __setitem__
        h1.__setitem__("nameFake","Elizabeth")
        self.assertEqual(h1["nameFake"],"Elizabeth")

        # __delitem__
        h1.__delitem__("nameFake")
        with pytest.raises(KeyError):
            self.assertEqual(h1["nameFake"],"Elizabeth")

        # __repr__
        v1['name'] = 0
        v2['name'] = 1
        v3['name'] = 2
        v4['name'] = 3
        v5['name'] = 4
        v6['name'] = 5
        v7['name'] = 6
        v8['name'] = 7

        string = "hex (0 1 2 3 4 5 6 7) (1 2 3) edgeGrading (1 1 1 1 1 1 1 1 1 1 1 1)"
        self.assertEqual(str(h1),string)

        h1.add_edge([v1,v2],expansionRatio = 2)

        string = "hex (0 1 2 3 4 5 6 7) (1 2 3) edgeGrading (2 1 1 1 1 1 1 1 1 1 1 1)"
        self.assertEqual(str(h1),string)

    def test_add_edge(self):
        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,4,1)
        v3 = pbm.Vertex(1,2,3)
        v4 = pbm.Vertex(1,2,4)
        v5 = pbm.Vertex(2,3,1)
        v6 = pbm.Vertex(2,4,1)
        v7 = pbm.Vertex(2,2,3)
        v8 = pbm.Vertex(2,2,4)

        v1['name'] = 0
        v2['name'] = 1
        v3['name'] = 2
        v4['name'] = 3
        v5['name'] = 4
        v6['name'] = 5
        v7['name'] = 6
        v8['name'] = 7


        h1 = pbm.Hexahedron([v1,v2,v3,v4,v5,v6,v7,v8],numberOfCells=[1,2,3])

        h1.add_edge([v1, v2], expansionRatio = 2)

        e1 = pbm.Edge([v1, v2], expansionRatio = 2)

        self.assertEqual(h1['edges'][0], e1)

        with pytest.raises(ValueError):
            h1.add_edge([v1,v7],expansionRatio = 1)

        with pytest.raises(ValueError):
            h1.add_edge([v1,v2+[1,2,3]], expansionRatio = 3)

    def test_add_face(self):
        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,4,1)
        v3 = pbm.Vertex(1,2,3)
        v4 = pbm.Vertex(1,2,4)
        v5 = pbm.Vertex(2,3,1)
        v6 = pbm.Vertex(2,4,1)
        v7 = pbm.Vertex(2,2,3)
        v8 = pbm.Vertex(2,2,4)

        v1['name'] = 0
        v2['name'] = 1
        v3['name'] = 2
        v4['name'] = 3
        v5['name'] = 4
        v6['name'] = 5
        v7['name'] = 6
        v8['name'] = 7


        h1 = pbm.Hexahedron([v1,v2,v3,v4,v5,v6,v7,v8],numberOfCells=[1,2,3])

        h1.add_face([v1, v2, v3, v4], name="inlet")

        f1 = pbm.Face([v1, v2, v3, v4], name="outlet")

        self.assertEqual(h1['faces'][0], f1)

        with pytest.raises(ValueError):
            h1.add_face([v1,v7,v3,v2], name="monkey")

        with pytest.raises(ValueError):
            h1.add_face([v1,v2+[0,0,1],v3,v4], name="Elizabeth")

        with pytest.raises(ValueError):
            h1.add_face("Elizabeth")

        with pytest.raises(ValueError):
            h1.add_face([v1,v2,v3,v4], name="Elizabeth")
            h1.add_face([v1,v2,v3,v4], name="Elizabeth")
