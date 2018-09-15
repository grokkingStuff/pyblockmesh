from collections.abc import MutableMapping

class Vertex(MutableMapping):
    instances = []

    def __init__(self, x=None, y=None, z=None, *args, **kw):
        if x is None or y is None or z is None:
            raise ValueError("(x,y,z) cannot contain null values")
        self._storage = dict(x=x,y=y,z=z,name=None,*args, **kw)
        Vertex.instances.append(self)

    def __getitem__(self, key):
        return self._storage[key]
    def __setitem__(self, key, value):
        self._storage[key] = value
    def __delitem__(self, key):
        del self._storage[key]
    def __len__(self):
        return len(self._storage)
    def __iter__(self):
        return iter(self._storage)
    def __len__(self):
        return len(self._storage)
    def __repr__(self):
        string = "("+str(self["x"])+" "+str(self["y"])+" "+str(self["z"])+")"
        return string


    # Mathematical Functions: Addition, Negation and Subtraction
    def __add__(self, other):
        '''Adds a vertex, number or numpy array to a vertex together'''

        from numbers import Number # Used to check if the variable 'other' is actually a number
        import numpy as np         # Used to add numpy arrays of length 3 to the vertex

        if isinstance(other, Vertex):
            # Used to support Vertex(0,0,0) + Vertex(0,0,1)
            return Vertex(self["x"] + other["x"],
                          self["y"] + other["y"],
                          self["z"] + other["z"])
        elif isinstance(other, Number):
            # Used to support Vertex(0,0,0) + 4
            return Vertex(self['x'] + other,
                          self['y'] + other,
                          self['z'] + other)
        elif isinstance(other, list):
            # Used to support Vertex(0,0,0) + [1,2,3]
            assert len(other) is 3, "Length of list must be 3"
            return Vertex(self['x'] + other[0],
                          self['y'] + other[1],
                          self['z'] + other[2])
        elif isinstance(other, np.ndarray):
            # Used to support Vertex(0,0,0) + np.array([1,2,3]) or
            #                 Vertex(0,0,0) + np.array([[1],[2],[3]])
            dimension = other.shape
            # Ensure that other is either 1D or 2D
            assert len(dimension) is 2 or len(dimension) is 1, "numpy array must be of shape (3,) or (3,1)"

            # We need to find out if we're dealing with a vector in the math term or the programming term
            # programming term: theta = np.array([1,2,3,4,5])
            # math term: np.array([1,2,3,4,5])[:,np.newaxis]

            # We should really raise a error or warning here but I am a benovelent god.
            # (Also, I kinda forget to switch axes all the time and I'm guessing there are people like me out there)

            if len(dimension) is 1:
                # We're dealing with arrays like np.array([1,2,3])
                # aka programming term
                assert dimension[0] is 3, "numpy array should have only three elements"

                return Vertex(self['x'] + other[0],
                              self['y'] + other[1],
                              self['z'] + other[2])
            elif len(dimension) is 2:
                # We're dealing with arrays like np,array([[1],[2],[3]])
                # aka math term
                assert dimension[0] is 3, "numpy array should only have three elements"
                assert dimension[1] is 1, "numpy array must be a vector and have only three elements"

                return Vertex(self['x'] + other[0][0],
                              self['y'] + other[1][0],
                              self['z'] + other[2][0])

            else:
                raise ValueError("numpy array of shape %s cannot be added to a Vertex" % str(dimension))

    def __radd__(self,other):
        return self.__add__(other)
    def __neg__(self):
        '''Returns negative of self'''
        return Vertex(-self['x'],
                      -self['y'],
                      -self['z'])
    def __sub__(self,other):
        '''Implements subtraction. Refer __add__'''
        other = other.__neg__()
        return self.__add__(other)
    def __rsub__(self,other):
        return self.__sub__(other)

    def __mul__(self, other):
        ''' multiply self with other, e.g. Vertex(0,0,1) * 7 == Vertex(0,0,7) '''

        from numbers import Number # Used to check if the variable 'other' is actually a number
        import numpy as np         # Used for tensor multiplication

        if isinstance(other, Vertex):
            raise TypeError("Vertices cannot be multiplied together")
        elif isinstance(other, Number):
            return Vertex(self['x'] * other,
                          self['y'] * other,
                          self['z'] * other)
        elif isinstance(other,np.ndarray):
            dimension = other.shape

            assert dimension == (3, 3), "Only tensors of shape (3,3) can be used for multiplication"

            vector = np.array([self['x'],self['y'],self['z']])[:,np.newaxis]

            assert vector.shape == (3,1)
            ans = other.dot(vector)
            assert ans.shape == (3,1)

            import warnings
            warnings.warn("Please reverse order of multiplicands." + 
                          " While correct, it is best to keep the rules of matrix multiplication in mind." + 
                          " Vertex should be treated as a vector", UserWarning)

            return Vertex(ans[0][0],
                          ans[1][0],
                          ans[2][0])
        else:
            raise TypeError("Vertices cannot be multiplied with %s" % type(other))

    __array_priority__ = 10000  # Used so that other types respect your __rmul__ instead of using their __mul__
    def __rmul__(self, other):
        ''' multiply other with self, e.g. 7 * Vertex(0,0,0) '''
        import numpy as np       # Used to check if other is a numpy array
        if isinstance(other,np.ndarray):

            dimension = other.shape

            assert dimension == (3,3), "Only tensors of shape (3,3) can be used for multiplication"

            vector = np.array([self['x'],self['y'],self['z']])[:,np.newaxis]
            assert vector.shape == (3,1)
            ans = other.dot(vector)
            assert ans.shape == (3,1)

            return Vertex(ans[0][0],
                          ans[1][0],
                          ans[2][0])
        else:
            return self.__mul__(other)

    # Comparison Functions <, ==
    def __lt__(self,other):
        ''' Less than is implemented via Lexicographical order'''
        x = self["x"] < other["x"]
        y = self["y"] < other["y"]
        z = self["z"] < other["z"]

        x1 = self["x"] == other["x"]
        y1 = self["y"] == other["y"]
        z1 = self["z"] == other["z"]

        if x and not x1:
            return True
        elif x1:
            if y and not y1:
                return True
            elif y1:
                if z and not z1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        ''' Check for equality between vertices'''
        if type(other) is type(self):
            if self["x"] is other["x"] and self["y"] is other["y"] and self["z"] is other["z"]:
               return True
        else:
            return False


    @classmethod
    def list_all(cls):
        string = "\nvertices\n(" + "\n    " + "\n    ".join([str(vertex) for vertex in cls.instances]) + "\n)"
        return string

    @classmethod
    def assign_names(cls):
        for i,vertex in enumerate(cls.instances):
            vertex["name"] = str(i)
