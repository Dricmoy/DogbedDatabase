class LogicalBase:
    def __init__(self, storage):
        self._storage = storage
        self._refresh_tree_ref()

    def get(self, key):
        if not self._storage.locked:
            self._refresh_tree_ref()
        return self._get(self._follow(self._tree_ref), key)

    def set(self, key, value):
        if not self._storage.locked:
            self._refresh_tree_ref()
        new_root = self._set(self._follow(self._tree_ref), key, value)
        self._tree_ref = self.node_ref_class(self._storage.write_node(new_root))
        return self._tree_ref

    def delete(self, key):
        if not self._storage.locked:
            self._refresh_tree_ref()
        new_root = self._delete(self._follow(self._tree_ref), key)
        self._tree_ref = self.node_ref_class(self._storage.write_node(new_root))
        return self._tree_ref

    def _refresh_tree_ref(self):
        self._tree_ref = self.node_ref_class(self._storage.get_root_address())

    def _follow(self, node_ref):
        return node_ref.follow(self._storage)
