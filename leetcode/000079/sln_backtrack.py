class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        seen = [[False for _ in range(n)] for _ in range(m)]

        def backtrack(i, j, i_word):
            if board[i][j] != word[i_word]:
                return False
            if i_word == len(word) - 1:
                return True
            ans = False

            for move in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                inx = i + move[0]
                jnx = j + move[1]
                if inx < 0 or inx >= m:
                    continue
                if jnx < 0 or jnx >= n:
                    continue
                if seen[inx][jnx]:
                    continue

                seen[inx][jnx] = True
                
                if backtrack(inx, jnx, i_word + 1):
                    ans = True

                seen[inx][jnx] = False

            return ans

        for i in range(m):
            for j in range(n):
                seen[i][j] = True

                if backtrack(i, j, 0):
                    return True

                seen[i][j] = False

        return False
