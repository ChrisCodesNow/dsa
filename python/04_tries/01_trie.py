class Node:
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = [None for _ in range(26)]


    def set_end_word(self):
        self.end_word = True


class Trie:
    def __init__(self):
        self.root = Node()


    def idx(self, char):
        return ord(char) - ord('a')


    def insert(self, key):
        
        itr = self.root
        prev = None
        for char in key:
            i = self.idx(char)
            if not itr.children[i]:
                itr.children[i] = Node()

            prev = itr
            itr = itr.children[i]

        # prev.set_end_word()
        itr.set_end_word()


    def search(self, key):
        itr = self.root
        prev = None
        for char in key:
            i = self.idx(char)
            if not itr.children[i]:
                return False
            
            prev = itr
            itr = itr.children[i]

        # return prev.end_word
        return itr.end_word



if __name__ == '__main__':
    trie = Trie()
    words = 'car call caller carrot bacon bar zap'.split()
    for word in words:
        trie.insert(word)

    words += 'carrots calling bat soap camera zip'.split()


    for word in words:
        if trie.search(word):
            print(f'{word} in trie')
        else:
            print(f'{word} NOT IN trie')
