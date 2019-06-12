# Breadth-first search

```
bfs(G, s):
	for u in G.V - {s}:
		u.color = WHITE
		u.d = null
		u.parent = null
	s.color = GRAY
	s.d = 0
	s.parent = null
	Q <- s
	while Q:
		u <- Q
		for v in G.Adj[u]:
			if v.color == WHITE:
				v.color = GRAY
				v.d = u.d + 1
				v.parent = u
				Q <- v
		u.color = BLACK
```
