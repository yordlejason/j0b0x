from collections import defaultdict


class Trie:

    def __init__(self):
        self.node = lambda: defaultdict(lambda: False)
        self._root = self.node()
        self._root[None] = True

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self._root
        for c in word:
            if not node[c]:
                node[c] = self.node()
                node[None] = True
            node = node[c]
        node[True] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._root
        for c in word:
            if not node[c]:
                return False
            node = node[c]
        return node[True]

    def startswith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._root
        for c in prefix:
            if not node[c]:
                return False
            node = node[c]
        return True
