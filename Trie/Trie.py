from .node import Node


class Trie:
    def __init__(self):
        self.root = Node('')
        self.words = 0
        self.end_nodes = []

    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                current_node = current_node.add_child(letter)
        self.end_nodes.append(current_node)
        current_node.last_letter = True
        self.words += 1

    def delete_word(self, word):
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                raise LookupError("Word does not exist.")

        self.end_nodes.remove(current_node)
        current_node.last_letter = False
        self.words -= 1

    def __str__(self):
        stack = [self.root]
        visited = dict()
        words = list()
        while stack:
            current_node = stack[-1]

            if current_node.last_letter and current_node not in visited:
                words.append("".join([str(node) for node in stack]))
            else:
                pass

            visited.update({current_node: True})

            number_done = 0

            for child in current_node.children:
                if current_node.children[child] not in visited:
                    stack.append(current_node.children[child])
                    break
                else:
                    number_done += 1

            if number_done == len(current_node.children):
                stack.pop()
            else:
                pass

        return "\n".join(words)
