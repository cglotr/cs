class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            visited[i][j] = True

            for imv, jmv in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                inx = i + imv
                jnx = j + jmv
                if inx < 0 or inx >= m:
                    continue
                if jnx < 0 or jnx >= n:
                    continue
                if grid[inx][jnx] != '1':
                    continue
                if visited[inx][jnx]:
                    continue

                dfs(inx, jnx)

        forest = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)

                    forest += 1

        return forest
