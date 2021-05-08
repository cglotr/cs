class Prim:

    # N = number of vertices
    # G = adjacency graph, (cost, vertex)
    def mst(self, N, G):
        cost = 0
        mst = []
        seen = set()
        pq = []

        def add(u):
            seen.add(u)

            for cost, v in G[u]:
                if v in seen:
                    continue

                heapq.heappush(pq, (cost, u, v))

        add(0)

        while pq and len(seen) < N:
            cost, u, v = heapq.heappop(pq)

            if v in seen:
                continue

            add(v)

            cost += cost
            mst.append((u, v, cost))

        return cost, mst
