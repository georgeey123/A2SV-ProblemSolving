class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        def get_neighbors(s):
            neighbors = []
            for i in range(4):
                for d in [-1, 1]:
                    new_digit = (int(s[i]) + d) % 10
                    neighbor = s[:i] + str(new_digit) + s[i+1:]
                    neighbors.append(neighbor)
            return neighbors
        
        start = "0000"
        
        if start in deadends:
            return -1
        
        if target == start:
            return 0
        
        visited = set([start])
        queue = deque([(start, 0)])
        
        while queue:
            current, turns = queue.popleft()
            
            for neighbor in get_neighbors(current):
                if neighbor == target:
                    return turns + 1
                
                if neighbor not in visited and neighbor not in deadends:
                    visited.add(neighbor)
                    queue.append((neighbor, turns + 1))
        
        return -1
