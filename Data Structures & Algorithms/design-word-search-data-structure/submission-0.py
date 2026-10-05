class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        res = self._find(curr, word, 0)
        return res
        
    def _find(self, node, word, i) -> bool:
        for j in range(i, len(word)):
            c = word[j]
            if c == '.':
                return any(self._find(child, word, j + 1) for child in node.children.values())
            if c not in node.children:
                return False
            node = node.children[c]
        return node.endOfWord
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)