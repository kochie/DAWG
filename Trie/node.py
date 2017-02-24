class Node:
    def __init__(self, value):
        self.parent = None
        self.value = value
        self.children = dict()
        self.last_letter = False

    def __iter__(self):
        return self.value

    def add_child(self, value):
        self.children.update({value: Node(value)})
        self.children[value].add_parent(self)
        return self.children[value]

    def add_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return self.value
