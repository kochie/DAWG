from .node import Node


class DAWG:
    def __init__(self):
        self.start = Node()
        self.end = Node()
        self.word_count = 0

        self.start.add_child(self.end, "")



    def add_word(self, word):
        word = list(word)
        top_node = self.start
        bottom_node = self.end
        while word:
            letter = word[0]
            if letter in top_node.children:
                top_node = top_node.children[letter]
                word.pop(0)
            else:
                word.reverse()
                break

        while word:
            letter = word[0]
            if letter in bottom_node.children:
                if bottom_node.children[letter] != top_node:
                    bottom_node = bottom_node.children[letter]
                    word.pop(0)
                else:
                    bottom_node = self.add_parent(bottom_node, letter, word)
            else:
                bottom_node = self.add_parent(bottom_node, letter, word)

    @staticmethod
    def add_parent(bottom_node, letter, word):
        new_node = Node()
        new_node.add_child(bottom_node, letter)
        bottom_node = new_node
        word.pop(0)
        return bottom_node



