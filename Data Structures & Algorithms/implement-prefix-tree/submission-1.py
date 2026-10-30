class TreeNode:
    def __init__(self): 
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()

            node = node.children[c]

        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return True if node and node.endOfWord else False

    def startsWith(self, prefix: str) -> bool:
        node = self._find(prefix)
        return True if node else False

    def _find(self, word: str) -> TreeNode:
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return None

        return node