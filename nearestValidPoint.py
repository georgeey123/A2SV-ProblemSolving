class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_indicies = []

        for i, point in enumerate(points):
            px, py = point[0], point[1]
            man_distance = abs(x - px) + abs(y - py)
            
            if px == x or py == y:
                if man_distance < min_distance:
                    min_distance = man_distance
                    min_indicies = [i]
                elif man_distance == min_distance:
                    min_indicies.append(i)
        
        if len(min_indicies) > 0:
            return min(min_indicies)
        else:
            return -1
