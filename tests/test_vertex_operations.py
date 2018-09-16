import pyblockmesh as pbm

from tests import *
from tests.helpers import *

# Unit tests are great but what about property tests?

class TestInitialization(unittest.TestCase):

    def test_initialization(self):
        with pytest.raises(ValueError):
            v1 = pbm.Vertex(None,3,1)


    def test_iter(self):
        v1 = pbm.Vertex(1,1,1)
        import numpy as np
        for i in v1:
            self.assertEqual(i,np.int64(1))

    def test_len(self):
        v1 = pbm.Vertex(0,0,0)
        self.assertEqual(len(v1),3)

    def test_repr(self):
        v1 = pbm.Vertex(0,0,0)
        self.assertEqual(str(v1),"(0 0 0)")

    def test_del(self):
        v1 = pbm.Vertex(0,0,0)
        v1["name"] = "Henry"
        v1["name"] = "Elizabeth"
        v1.__delitem__("name")
        with pytest.raises(KeyError):
            self.assertEqual(v1["name"],"Elizabeth")

class TestOperation(unittest.TestCase):

    def test_lt(self):
        v1 = pbm.Vertex(0,3,1)
        v2 = pbm.Vertex(1,2,2)
        self.assertEqual( v1 < v2, True)

        v2 = pbm.Vertex(0,4,1)
        self.assertEqual( v1 < v2, True)

        v2 = pbm.Vertex(0,3,2)
        self.assertEqual( v1 < v2, True)

        v2 = pbm.Vertex(0,3,0)
        self.assertEqual( v1 < v2, False)

        v2 = pbm.Vertex(0,2,0)
        self.assertEqual( v1 < v2, False)

    def test_equal(self):
        v1 = pbm.Vertex(0,0,0)
        v2 = pbm.Vertex(0,0,0)
        self.assertEqual( v1 == v2, True)

        v2 = pbm.Vertex(1,0,0)
        self.assertEqual( v1 == v2, False)

        v2 = "Hello World!"
        self.assertEqual( v1 == v2, False)

    def test_gt(self):
        v1 = pbm.Vertex(0,0,0)
        v2 = pbm.Vertex(1,0,0)
        self.assertEqual( v1 > v2, False)

    def test_add(self):

        # Addition of two vertices
        v1 = pbm.Vertex(0,0,0)
        v2 = pbm.Vertex(1,0,0)
        self.assertEqual( v1 + v2, pbm.Vertex(1,0,0) )

        # Addition of list to vertex
        v2 = [1,0,0]
        self.assertEqual( v1 + v2, pbm.Vertex(1,0,0))

        # Addition of np.array to vertex
        import numpy as np
        v2 = np.array([1,0,0])
        self.assertEqual( v1 + v2, pbm.Vertex(1,0,0))

        v2 = np.array([1,0,0])[:,np.newaxis]
        self.assertEqual(v1 + v2, pbm.Vertex(1,0,0))

        with pytest.raises(AssertionError):
            v2 = np.array([1])
            self.assertEqual(v1 + v2,0)

        # Test radd
        self.assertEqual(v1 + [1,2,3],[1,2,3] + v1)


    def test_sub(self):

        # Subtraction of two vertices
        v1 = pbm.Vertex(0,0,0)
        v2 = pbm.Vertex(1,0,0)
        self.assertEqual( v1 - v2, pbm.Vertex(-1,0,0) )

        # Subtraction of list to vertex
        v2 = [1,0,0]
        self.assertEqual( v1 - v2, pbm.Vertex(-1,0,0))

        # Subtraction of np.array to vertex
        import numpy as np
        v2 = np.array([1,0,0])
        self.assertEqual( v1 - v2, pbm.Vertex(-1,0,0))

        # Test radd
        self.assertEqual(v1 - np.array([1,2,3]),-(np.array([1,2,3]) - v1))


    def test_mult(self):

        with pytest.raises(TypeError):
            # Multiplication of two vertices
            v1 = pbm.Vertex(0,0,0)
            v2 = pbm.Vertex(1,0,0)
            self.assertEqual( v1 * v2, pbm.Vertex(0,0,0) )

        # Multiplication of number with vertex
        v1 = pbm.Vertex(1,0,0)
        v2 = 5
        self.assertEqual( v1 * v2, pbm.Vertex(5,0,0))
        self.assertEqual( v2 * v1, pbm.Vertex(5,0,0))
        with pytest.raises(AssertionError):
            # Multiplication of np.array to vertex
            import numpy as np
            v2 = np.array([1,0,0])
            self.assertEqual( v1 * v2, pbm.Vertex(1,0,0))

        with pytest.warns(UserWarning):
            import numpy as np
            v2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
            self.assertEqual(v1*v2, pbm.Vertex(1,0,0))

        with pytest.raises(TypeError):
            v2 = "Hello there! General Kenobi"
            self.assertEqual(v1*v2,None)

        import numpy as np
        v2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
        self.assertEqual(v2 * v1, pbm.Vertex(1,0,0))

