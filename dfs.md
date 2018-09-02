**Depth-first search**

```
dfs(G):
  for each u in G.V:
    u.color = WHITE
    u.parent = NIL
  time = 0
  for each u in G.V:
    if u.color == WHITE:
      dfsVisit(G, u)
```

**Depth-first search visit**

```
dfsVisit(G, u):
  time = time + 1
  u.discovery = time
  u.color = GRAY
  for each v in G.Adj[u]:
    if v.color == WHITE
      v.parent = u
      dfsVisit(G, v)
  u.color = BLACK
  time = time + 1
  u.finish = time
```
