class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        cur = self.trie

        for c in word:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]

        cur['$'] = True

    def search(self, word: str) -> bool:
        cur = self.trie

        for c in word:
            if c not in cur:
                return False
            cur = cur[c]

        return '$' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie

        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
