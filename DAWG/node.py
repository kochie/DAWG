class Node:
    def __init__(self):
        self.parent_vertices = dict()
        self.children_vertices = dict()

    def add_child(self, node, letter):
        self.children_vertices.update({letter: node})

    def add_parent(self, node, letter):
        self.parent_vertices.update({letter: node})

    def remove_parent(self, letter):
        del self.parent_vertices[letter]

    def remove_child(self, letter):
        del self.children_vertices[letter]

    def __str__(self):
        parents = []
        for letter in self.parent_vertices:
            parents.append(letter)

        children = []
        for letter in self.children_vertices:
            children.append(letter)

        parents = ", ".join(parents)
        children = ", ".join(children)
        return "{0} \n {1}".format(parents, children)

