class BinaryNode:
    def __init__(self, key, value_ref, left_ref=None, right_ref=None):
        self.key = key
        self.value_ref = value_ref
        self.left_ref = left_ref
        self.right_ref = right_ref

    def serialize(self):
        return f"{self.key},{self.value_ref},{self.left_ref},{self.right_ref}".encode()

class ValueRef:
    def __init__(self, value):
        self.value = value

    def follow(self, storage):
        return self.value
