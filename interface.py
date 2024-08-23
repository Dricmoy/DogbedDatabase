from dbdb.physical import Storage
from dbdb.binary_tree import BinaryTree

class DBDB:
    def __init__(self, f):
        self._storage = Storage(f)
        self._tree = BinaryTree(self._storage)

    def __getitem__(self, key):
        self._assert_not_closed()
        return self._tree.get(key)

    def __setitem__(self, key, value):
        self._assert_not_closed()
        self._tree = self._tree.set(key, value)

    def __delitem__(self, key):
        self._assert_not_closed()
        self._tree = self._tree.delete(key)

    def commit(self):
        self._storage.commit(self._tree)

    def _assert_not_closed(self):
        if self._storage.closed:
            raise ValueError('Database closed.')
