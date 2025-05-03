class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g = dict()
        n = len(words)

        for word in words:
            for ch in word:
                g[ch] = []

        for i in range(n - 1):
            w1 = words[i]

            for j in range(i + 1, n):
                w2 = words[j]

                for k in range(len(w1)):
                    if k >= len(w2):
                        return ''

                    if w1[k] != w2[k]:
                        g[w1[k]].append(w2[k])
                        break

        in_degree = dict()
        q = collections.deque()
        ans = []

        for ch in g:
            in_degree[ch] = 0

        for u in g:
            for v in g[u]:
                in_degree[v] += 1

        for u in in_degree:
            if in_degree[u] <= 0:
                q.append(u)

        while q:
            u = q.popleft()

            ans.append(u)

            for v in g[u]:
                in_degree[v] -= 1

                if in_degree[v] <= 0:
                    q.append(v)

        if len(ans) < len(g):
            return ''

        return ''.join(ans)
