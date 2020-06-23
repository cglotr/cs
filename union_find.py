class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        
    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota == rootb:
            return False
        if self.size[roota] < self.size[rootb]:
            self.size[rootb] += self.size[roota]
            self.parent[roota] = rootb
        else:
            self.size[roota] += self.size[rootb]
            self.parent[rootb] = roota
        return True
    
    def find(self, a):
        root = self.parent[a]
        while root != self.parent[root]:
            root = self.parent[root]
        curr = a
        
        # path compression
        while curr != root:
            after = self.parent[curr]
            self.parent[curr] = root
            curr = after
        
        return root
