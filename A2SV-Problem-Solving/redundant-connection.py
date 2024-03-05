class UnionFind:
    
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
        
    def find(self, x):
        root = x
        
        while root != self.parent[root]:
            root = self.parent[root]
            
        while x != root:
            parent = self.parent[x]
            self.parent[x] = root
            x = parent
            
        return root
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        unionF = UnionFind(n)
        
        for u,v in edges:
            if unionF.find(u-1) != unionF.find(v-1):
                unionF.union(u-1,v-1)
            else:
                return list((u,v))
            
        return []
            
        
            
        