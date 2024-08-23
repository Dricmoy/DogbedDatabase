from dbdb.logical import LogicalBase, ValueRef

class BinaryTree(LogicalBase):
    def _get(self, node, key):
        while node is not None:
            if key < node.key:
                node = self._follow(node.left_ref)
            elif node.key < key:
                node = self._follow(node.right_ref)
            else:
                return self._follow(node.value_ref)
        raise KeyError

    def _set(self, node, key, value):
        if node is None:
            return BinaryNode(key, value)
        elif key < node.key:
            left = self._set(self._follow(node.left_ref), key, value)
            return BinaryNode(node.key, node.value_ref, left, node.right_ref)
        elif node.key < key:
            right = self._set(self._follow(node.right_ref), key, value)
            return BinaryNode(node.key, node.value_ref, node.left_ref, right)
        else:
            return BinaryNode(key, ValueRef(value), node.left_ref, node.right_ref)

    def _delete(self, node, key):
        if node is None:
            raise KeyError
        elif key < node.key:
            left = self._delete(self._follow(node.left_ref), key)
            return BinaryNode(node.key, node.value_ref, left, node.right_ref)
        elif node.key < key:
            right = self._delete(self._follow(node.right_ref), key)
            return BinaryNode(node.key, node.value_ref, node.left_ref, right)
        else:
            if node.left_ref is None:
                return self._follow(node.right_ref)
            elif node.right_ref is None:
                return self._follow(node.left_ref)
            else:
                min_larger_node = self._find_min(self._follow(node.right_ref))
                return BinaryNode(min_larger_node.key, min_larger_node.value_ref, node.left_ref, node.right_ref)

    def _find_min(self, node):
        while node.left_ref is not None:
            node = self._follow(node.left_ref)
        return node
