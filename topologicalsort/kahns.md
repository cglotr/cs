# Topological sort
Ordering of nodes in a directed acyclic graph (DAG) where for each directed edge from node `u` to `v`, node `u` comes first before node `v` in the ordering.

## Kahn's algorithm

```
def kahns(graph, n):
    topological_sort = [n](null)
    safe_edges = {}
    incoming_degrees = [n](0)
    
    for u, v in graph:
        incoming_degrees[v] += 1
    
    for u in [0 -> n):
        if incoming_degrees[u] == 0:
            safe_edges <- u
            
    index = 0
    
    while safe_edges:
        u <- safe_edges
        topological_sort[index] = u
        index += 1
        
        for v in graph[u]:
            incoming_degrees[v] -= 1
            if incoming_degrees[v] <= 0:
                safe_edges <- v
                
    if index < n:
        return null
        
    return topological_sort
```

### Time complexity
`O(V + E)`

### Practice
- https://leetcode.com/problems/parallel-courses/

### Resources
- [Wiki](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm)
- [WilliamFiset](https://www.youtube.com/watch?v=cIBFEhD77b4)
