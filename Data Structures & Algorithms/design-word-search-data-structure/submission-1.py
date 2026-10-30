class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()

            node = node.children[c]
        
        node.endOfWord = True

    def search(self, word: str) -> bool:
        res = self._find(self.root, word, 0)
        return res

    def _find(self, node, word, i):
        for j in range(i, len(word)):
            c = word[j]

            if c == '.':
                return any(self._find(n, word, j+1) for n in node.children.values())
            else:
                if c not in node.children:
                    return False
                else:
                    node = node.children[c]

        return node.endOfWord