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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionF = UnionFind(len(accounts))
        mapp = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in mapp:
                    unionF.union(i, mapp[e])
                else:
                    mapp[e] = i

        group = defaultdict(list)
        for i, email in mapp.items():
            rep = unionF.find(email)
            group[rep].append(i)

        res = []

        for i, emails in group.items():
            name = accounts[i][0]
            res.append([name] + sorted(group[i]))

        return res