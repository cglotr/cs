class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = collections.defaultdict(set)
        colors = collections.defaultdict(str)

        for a, b in prerequisites:
            preq[a].add(b)

        for c in range(numCourses):
            colors[c] = 'white'

        def dfs(u):
            colors[u] = 'gray'

            for v in preq[u]:
                if colors[v] == 'gray':
                    return False
                if colors[v] == 'white':
                    if not dfs(v):
                        return False

            colors[u] = 'black'

            return True

        for c in range(numCourses):
            if colors[c] == 'white':
                if not dfs(c):
                    return False

        for c in range(numCourses):
            if colors[c] != 'black':
                return False

        return True
        
