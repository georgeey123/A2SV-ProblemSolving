class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        max_heap = [-n for n in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            y = -heappop(max_heap)
            x = -heappop(max_heap)

            if x != y:
                new = y-x

                heappush(max_heap, -new)
        return abs(max_heap[0]) if len(max_heap) >= 1 else 0

        