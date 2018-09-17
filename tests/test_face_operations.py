import pyblockmesh as pbm

from tests import *
from tests.helpers import *

# Unit tests are great but what about property tests?

class TestFace(unittest.TestCase):

    def test_initialization(self):
        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,5,6)
        v3 = pbm.Vertex(1,3,3)
        v4 = pbm.Vertex(1,5,7)

        # Must have vertices
        with pytest.raises(ValueError):
            f1 = pbm.Face([])
            self.assertEqual(f1,"Elizabeth")

        # Must have 4 vertices
        with pytest.raises(AssertionError):
            f1  = pbm.Face([v1,v2,v3])
            self.assertEqual(f1,"Elizabeth")

        # Face must have name
        with pytest.raises(ValueError):
            f1 = pbm.Face([v1,v2,v3,v4])
            self.assertEqual(f1,"Elizabeth")

        #if patchtype is not defines, default to patch
        f1 = pbm.Face([v1,v2,v3,v4],name="inlet")
        self.assertEqual(f1["patchType"],'patch')

    def test_magic_methods(self):

        v1 = pbm.Vertex(1,3,1)
        v2 = pbm.Vertex(1,5,6)
        v3 = pbm.Vertex(1,3,3)
        v4 = pbm.Vertex(1,5,7)
        f1 = pbm.Face([v1,v2,v3,v4],name="inlet")

        # __setitem__
        f1.__setitem__("nameFake","monkey")
        self.assertEqual(f1["nameFake"],"monkey")

        # __delitem__
        f1.__delitem__("nameFake")
        with pytest.raises(KeyError):
            self.assertEqual(f1["nameFake"],"monkey")

        # __iter__
        for v in f1:
            self.assertEqual(v in f1["vertices"].values(),True)

        # __len__
        self.assertEqual(len(f1),4)

        # __eq__

        # Two faces with the same vertices are equal
        f1 = pbm.Face([v1,v2,v3,v4],name="inlet")
        f2 = pbm.Face([v1,v3,v2,v4],name="outlet")

        self.assertEqual(f1,f2)

        # Faces with different vertices are not equal
        v5 = pbm.Vertex(4,5,2)
        f2 = pbm.Face([v1,v2,v3,v5],name="inlet")

        self.assertEqual(f1 == f2, False)

        # Faces with different patchTypes are different
        f2 = pbm.Face([v1,v2,v3,v4],
                      name="outlet",
                      patchType = 'wall')

        self.assertEqual(f1 == f2, False)

        # A face can only equal to another face
        self.assertEqual(f1 == "Elizabeth",False)

        # __repr__

        v1["name"] = 0
        v2["name"] = 1
        v3["name"] = 2
        v4["name"] = 3
        string = "inlet\n{\n    type patch;\n    faces\n    (\n        ( 0 1 2 3 ) \n    );\n}"
        self.assertEqual(str(f1),string)
        #Need to do this in a non shitty way
