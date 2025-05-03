class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        
        ans = []
        trie = Trie()

        for w in words:
            trie.add(w)

        def backtrack(r, c, word):
            w = word + board[r][c]

            if not trie.prefix(w):
                return

            if trie.find(w):
                ans.append(w)
                
                trie.remove(w)

            for rd, cd in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rn = r + rd
                cn = c + cd
                if rn < 0 or rn >= m:
                    continue
                if cn < 0 or cn >= n:
                    continue
                if visited[rn][cn]:
                    continue
                
                visited[rn][cn] = True

                backtrack(rn, cn, w)

                visited[rn][cn] = False

        for r in range(m):
            for c in range(n):
                visited[r][c] = True

                backtrack(r, c, '')

                visited[r][c] = False

        return ans


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0
        self.word = ''


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def add(self, word):
        node = self.trie

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

        node.word = word

    def prefix(self, pref):
        node = self.trie

        for ch in pref:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.count < 1:
                return False

        return True

    def find(self, word):
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.count < 1:
                return False

        return node.word == word

    def remove(self, word):
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return
            node = node.children[ch]
            if node.count > 0:
                node.count -= 1

        node.word = ''
