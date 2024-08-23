import os

class Storage:
    def __init__(self, f):
        self._f = f
        self._root_address = None
        self._locked = False

    @property
    def locked(self):
        return self._locked

    def get_root_address(self):
        if self._root_address is None:
            self._root_address = self._f.seek(0, os.SEEK_END)
        return self._root_address

    def commit(self, tree):
        self._locked = True
        self._root_address = self.write_node(tree)
        self._f.flush()
        self._locked = False

    def write_node(self, node):
        address = self._f.seek(0, os.SEEK_END)
        self._f.write(node.serialize())
        return address
