class UnionFind: 
    def __init__(self, size):
        self.parent = {chr(i):chr(i) for i in range(ord('a'),ord('a')+size)}
        self.size = {chr(i):1 for i in range(ord('a'),ord('a') + size)}    

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
    def equationsPossible(self, equations: List[str]) -> bool:
        unionF = UnionFind(26)

        check = []
        for equation in equations:
            # print(x[1:3])
            if equation[1:3] == '!=':
                check.append(equation)
            else:
                unionF.union(equation[0],equation[-1])
        
        for pair in check:
            if pair[1:3] == '!=':
                if unionF.find(pair[0]) == unionF.find(pair[-1]):
                    return False
        
        # print(unionFind.parent)
        return True
        
