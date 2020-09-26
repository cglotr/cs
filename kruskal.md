# Kruskal minimum spanning tree (MST)

## Algo

1. Sort edges by their weight (ascending order)
2. Dequeue edge & check if we can union vertex _A_ and _B_:
   - If we can, add the edge into our MST & union _A_ and _B_
3. Stop when either of these happens:
   - All edges are processed
   - All of the vertices have been unified

#### Notes

1. Use Union Find/Disjoint Set Union (DSU) to help with union operation
