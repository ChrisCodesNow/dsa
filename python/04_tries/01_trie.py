class Node:
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = [None for _ in range(26)]


    def set_end_word(self):
        self.end_of_word = True


class Trie:
    def __init__(self):
        self.root = Node()


    def idx(self, char):
        return ord(char) - ord('a')


    def insert(self, key):
        
        itr = self.root
        for char in key:
            i = self.idx(char)
            if not itr.children[i]:
                itr.children[i] = Node()

            itr = itr.children[i]

        itr.set_end_word()


    def search(self, key):
        itr = self.root
        for char in key:
            i = self.idx(char)
            if not itr.children[i]:
                return False
            
            itr = itr.children[i]

        return itr.end_of_word



if __name__ == '__main__':
    trie = Trie()
    words = 'car call caller carrot bacon bar zap'.split()
    for word in words:
        trie.insert(word)

    words += 'carrots calling bat soap camera zip so'.split()


    in_trie = [word for word in words if trie.search(word)]
    not_in_trie = [word for word in words if not trie.search(word)]
    
    print(f"words in trie = {in_trie}")
    print(f"words NOT in trie = {not_in_trie}")
