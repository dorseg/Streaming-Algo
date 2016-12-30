"""
This class represents a vertex in a graph.
"""
class Vertex (object):

    def __init__(self, id):
        """
        :param index: the identifier of vertex v.
        :param radius: a non-negative integer selected from the truncated geometric distribution.
        :param label: label Object.
        """
        super(Vertex, self).__init__()
        self._index = -1
        self._radius = -1
        self._label = None
        self._table = set([]) # M(v) as describe in the algortihm
        self._sp = [] # sp(v) as describe in the algorithm

    def get_index(self):
        return self._index

    def get_radius(self):
        return self._radius

    def get_label(self):
        return self._label

    def get_table(self):
        return self._table

    def get_sp(self):
        return self._sp

    def set_index (self, index):
        self._index = index

    def set_radius(self, radius):
        self._radius = radius

    def set_label(self, label):
        self._label = label

    def update_label(self, label):
        self._label.set_level(label.get_level() + 1)
        self._label.set_base_val(label.get_base_val())

    def __repr__(self):
        str = "Vertex(i:{}, r:{}, {})".format(self._index, self._radius, self._label)
        return str

    def __gt__(self, other):
        self_val, other_val = int(self._label), int(other.get_label())
        ans = self_val > other_val or (self_val == other_val and self._index > other.get_index())
        return ans


