import pyblockmesh as pbm

from tests import *
from tests.helpers import *

# Unit tests are great but what about property tests?

class TestInitialization(unittest.TestCase):

    def test_expansionRatio(self):
        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,5,6)

        e1 = pbm.Edge([v1,v1],keyword='line')
        self.assertEqual(e1["expansionRatio"],1)

        e2 = pbm.Edge([v1,v1],expansionRatio=3,keyword='line')
        self.assertEqual(e2["expansionRatio"],3)

    def test_keyword(self):
        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,5,6)

        e1 = pbm.Edge([v1,v1])
        self.assertEqual(e1["keyword"],'line')
        self.assertEqual(e1["interpolationPoints"],[])

        e1 = pbm.Edge([v1,v1],keyword='spline')
        self.assertEqual(e1["keyword"],'spline')

        with pytest.raises(ValueError):
            e1 = pbm.Edge([v1,v1],keyword='Kenobi')
            self.assertEqual(e1["keyword"],'spline')

        e1 = pbm.Edge([v1,v2])
        self.assertEqual(e1["keyword"],'line')
        self.assertEqual(e1["interpolationPoints"],[])

    def test_iter(self):
        v1 = pbm.Vertex(1,2,3)
        v2 = pbm.Vertex(1,4,3)

        e1 = pbm.Edge([v1,v2])
        for vertex in e1:
            self.assertEqual(vertex in [v1,v2],True)

    def test_del(self):
        v1 = pbm.Vertex(1,2,3)
        v2 = pbm.Vertex(3,4,2)

        v1["name"]=0
        v2["name"]=2

        e1 = pbm.Edge([v1,v2])
        e1["name"] = "Elizabeth"
        e1.__delitem__("name")

        with pytest.raises(KeyError):
            self.assertEqual(e1["name"],"Elizabeth")

    def test_len(self):
        v1 = pbm.Vertex(1,2,3)
        v2 = pbm.Vertex(1,4,3)

        e1 = pbm.Edge([v1,v2])
        self.assertEqual(len(e1),2)

    def test_repr(self):
        v1 = pbm.Vertex(1,2,3)
        v2 = pbm.Vertex(1,4,3)

        with pytest.raises(ValueError):
            e1 = pbm.Edge([v1,v2])
            self.assertEqual(str(e1),"Elizabeth")

        v1["name"]=0
        v2["name"]=2

        e1 = pbm.Edge([v1,v2])
        self.assertEqual(str(e1),"line 0 2")

        v3 = pbm.Vertex(1,3,4)
        e1 = pbm.Edge([v1,v2],keyword = 'arc',interpolationPoints = v3)
        self.assertEqual(str(e1),"arc 0 2 (1 3 4)")

        e1 = pbm.Edge([v1,v2],keyword = "spline",interpolationPoints = [v1,v2,v3])
        self.assertEqual(str(e1),"spline 0 2 ( (1 2 3) (1 4 3) (1 3 4) )")

    def test_eq(self):
        v1 = pbm.Vertex(1,2,3)
        v2 = pbm.Vertex(1,4,3)

        e1 = pbm.Edge([v1,v2])
        e2 = pbm.Edge([v1,v2])
        self.assertEqual(e1,e2)

        e2 = pbm.Edge([v1,v2+[1,2,3]])
        self.assertEqual(e1 == e2, False)

        e2 = "Elizabeth"
        self.assertEqual(e1 == e2, False)

        e2 = pbm.Edge([v1,v2],keyword='arc',interpolationPoints=v1+[1,0,0])
        self.assertEqual(e1 == e2, False)

        e1 = pbm.Edge([v1,v2],keyword='arc',interpolationPoints=v1)
        self.assertEqual(e1 == e2, False)

        e2 = pbm.Edge([v1,v2],expansionRatio = 2)
        self.assertEqual(e1 == e2, False)


