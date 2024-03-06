class UnionFind: 
    def __init__(self, size):
        self.parent = {chr(ord("a")+i): chr(ord("a")+i) for i in range(26)}        
        # self.size =  
        
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
            if rootX < rootY:
                self.parent[rootY] = rootX
                # self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                # self.size[rootY] += self.size[rootX]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(baseStr)
        unionF = UnionFind(n)
        for i in range(len(s1)):
            unionF.union(s1[i], s2[i])

        return ''.join(unionF.find(word) for word in baseStr)