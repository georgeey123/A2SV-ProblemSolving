class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = []
        
        table = [[float('inf')] * numCourses for _ in range(numCourses)]
        
        for u, v in prerequisites:
            table[u][v] = 1
            
        for i in range(numCourses):
            table[i][i] = 0
        # print(table)
    
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    table[i][j] = min(table[i][j], (table[i][k] + table[k][j]))
            # print(table)

        for u,v in queries:
            if table[u][v] == 0 or table[u][v] != float('inf'):
                answer.append(True)
            else:
                answer.append(False)
            
        return answer