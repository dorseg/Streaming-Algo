"""
    This class represents a label for vertex v, initialized as I(v).
    The labels of vertices may grow as the execution proceeds,
    they accept values from the set {1,2,...,n*t}.
"""


class Label (object):

    def __init__(self, level, base_val, base_vertex, N):
        """
        :param level:
        :param base_val:
        :param base_vertex:
        """
        super(Label, self).__init__()
        self._level = level
        self._base_val = base_val
        self._base_vertex = base_vertex
        self._N = N

    def get_level(self):
        return self._level

    def get_base_val(self):
        return self._base_val

    def get_base_vertex(self):
        return self._base_vertex

    def is_selected(self):
        """
        :return: True if level < radius(base_vertex) otherwise false.
        """
        return self._level < self._base_vertex.get_radius()

    def set_level(self, level):
        self._level = level

    def set_base_val(self, base_val):
        self._base_val = base_val

    def __repr__(self):
        str = "Label({}, {}, {})".format(self._level, self._base_val, self._base_vertex)
        return str

    def __str__(self):
        """
        label P can be seen as a pair (B(P),L(P))
        """
        str = "Label(b:{Bp}, l:{Lp})".format(Bp=self._base_val, Lp=self._level)
        return str

    def __int__(self):
        """
        :return: integer value represent the label
        """
        value = self._N*self._level+self._base_val
        return value

