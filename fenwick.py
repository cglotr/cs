class Fenwick:
    def __init__(self, n):
        self.a = [0 for i in range(n + 1)]

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < len(self.a):
            self.a[i] += x
            i += i & -i
