class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        n = len(costs)//2
        idx = 0
        diff = []
        cityA, cityB = 0, 0


        sorted_diff = sorted(costs, key=lambda x: x[0] - x[1])

        print(sorted_diff)

        for group in sorted_diff:
            if idx < n:
                cityA += sorted_diff[idx][0]
                idx += 1
            else:
                cityB += sorted_diff[idx][1]
                idx += 1

        ans = cityA + cityB

        return ans
