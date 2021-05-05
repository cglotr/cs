#### Prim's Minimum Spanning Tree (MST)

```
MstPrim(G, r)
  for u in G.V
    u.parent = NULL
    u.cost = INF

  r.cost = 0
  Q = G.V
  
  while Q
    u = Min(Q)
    
    for v in G.Adj[u]
      if v in Q and cost(u, v) < v.cost
        v.parent = u
        v.cost = cost(u, v)
```
