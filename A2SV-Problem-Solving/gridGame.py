class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_top, prefix_bottom = grid[0].copy(), grid[1].copy()

        for i in range(1,n):
            prefix_top[i] += prefix_top[i-1]
            prefix_bottom[i] += prefix_bottom[i - 1]

        res = float('inf')

        for i in range(n):
            remaining_top = prefix_top[-1] - prefix_top[i]
            remaining_bottom = prefix_bottom[i-1] if i > 0 else 0
            second_robot = max(remaining_top, remaining_bottom)
            res = min(res, second_robot)
        return res 
