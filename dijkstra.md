## Dijkstra

Given graph `g` & source node `s`, find the shortest path from `s` to every other nodes.

```
dijkstra(g, s):
    dist = [inf] * n
    heap = []
    prev = [nil] * n
    seen = [false] * n

    dist[s] = 0
    heap.insert((0, s))
    while heap:
        d, u = heap.pop()
        seen[u] = true
        if d > dist[u]:
            continue
        for v in g[u]:
            if seen[v]:
                continue
            cand = d + w(u, v)
            if cand < dist[v]:
                dist[v] = cand
                prev[v] = u
                heap.insert((cand, v))
    return dist, prev
```

Print shortest path from node `s` to `e`:

```
findShortestPath(g, s, e):
    dist, prev = dijkstra(g, s)
    if dist[e] >= inf:
        return []
    curr = e
    while curr:
        path.push(curr)
        curr = prev[curr]
    return path.reverse()
```
