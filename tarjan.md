# Tarjan's algorithm

## Tarjan's bridges algorithm

```
tarjan_bridges(graph, n):
    discovery_times = [n](INF)
    low_links = [n](-1)
    visited = [n](FALSE)

    bridges = []
    time = -1

    dfs(u, parent):
        visited[u] = TRUE
        time += 1
        discovery_time[u] = time

        for v in graph[u]:
            if v == parent:
                continue
            if not visited[u]:
                dfs(v, u)

                low_links[u] = min(low_links[u], low_links[v])
                if discovery_time[u] < low_links[v]:
                    bridges.append((u, v))
            else:
                low_links[u] = min(low_links[v], discovery_time[v])
    
    return bridges
```

### Resources
- https://codeforces.com/blog/entry/71146
- https://www.youtube.com/watch?v=aZXi1unBdJA
- https://leetcode.com/problems/critical-connections-in-a-network/discuss/417095/Tarjan-Bridges-Algorithm-Python-faster-than-98.73
