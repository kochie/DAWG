from Trie import Trie


def main():
    trie = Trie.Trie()
    with open("./words.txt") as words:
        for word in words:
            trie.add_word(word.strip("\n"))
    print(trie)

if __name__ == '__main__':
    main()
