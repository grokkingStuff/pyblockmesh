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

        e2 = pbm.Edge([v1,v1],keyword='spline')
        self.assertEqual(e2["keyword"],'spline')

        with pytest.raises(ValueError):
            e2 = pbm.Edge([v1,v1],keyword='Kenobi')
            self.assertEqual(e2["keyword"],'spline')
