# Floyd-Warshall

```
D = [R x C](INF)
for u in V:
    D[u][u] = 0
for u, v in E:
    D[u][v] = cost(u, v)
for k in V:
    for u in V:
        for v in V:
            if D[u][k] + D[k][v] < D[u][v]:
                D[u][v] = D[u][k] + D[k][v]
```

Time `O(n^3)`, Space `O(n^2)`
