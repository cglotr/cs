class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        C = len(matrix[0])

        top = 0
        bot = R-1
        lft = 0
        rgt = C-1

        ans = []

        while top <= bot and lft <= rgt:
            for i in range(lft, rgt+1):
                ans.append(matrix[top][i])

            top += 1

            for i in range(top, bot+1):
                ans.append(matrix[i][rgt])

            rgt -= 1

            if top > bot or rgt < lft:
                break

            for i in range(rgt, lft-1, -1):
                ans.append(matrix[bot][i])

            bot -= 1

            for i in range(bot, top-1, -1):
                ans.append(matrix[i][lft])

            lft += 1

        return ans
