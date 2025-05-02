class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pcfc = set()
        pcfc_ans = set()

        atln = set()
        atln_ans = set()

        ans = []

        for r in range(m):
            pcfc.add((r, 0))
            atln.add((r, n - 1))

        for c in range(n):
            pcfc.add((0, c))
            atln.add((m - 1, c))

        def mark(r, c, ans):
            ans.add((r, c))

            for rd, cd in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rn = r + rd
                cn = c + cd
                if rn < 0 or rn >= m:
                    continue
                if cn < 0 or cn >= n:
                    continue
                if heights[rn][cn] < heights[r][c]:
                    continue
                if (rn, cn) in ans:
                    continue
                
                mark(rn, cn, ans)

        for r, c in pcfc:
            mark(r, c, pcfc_ans)

        for r, c in atln:
            mark(r, c, atln_ans)

        for r in range(m):
            for c in range(n):
                rc = (r, c)
                if rc in pcfc_ans and rc in atln_ans:
                    ans.append([r, c])

        return ans
