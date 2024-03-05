class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        # if x == self.parent[x]:
        #     return x
        # self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]
        root = x

        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            parent = self.parent[x]
            self.parent[x] = root
            x = parent
        return root

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        unionF = UnionFind(n)
        count = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and unionF.find(i) != unionF.find(j):
                    count -= 1
                    unionF.union(i,j)

        return count



