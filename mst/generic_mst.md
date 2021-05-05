# Generic Minimum Spanning Tree (MST)

```
GenericMst(G, w)
  A = {}
  
  while A != mst
    find safe edge (u, v)
    A = A union {(u, v)}
    
return A
```

- Invariant: `A` is a subset of some MST
- Initially, `A = {}` trivially satisfies the invariant
- The `while` loop maintains the invariant by only adding safe edge `(u, v)` to `A`
