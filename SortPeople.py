class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)

        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if heights[j] > heights[max_index]:
                    max_index = j
                    names[i], names[max_index] = names[max_index], names[i]
                    heights[i], heights[max_index] = heights[max_index], heights[i]

        return names

        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if heights[max_idx] < heights[j]:
                   max_idx = j
            heights[i] , heights[max_idx] = heights[max_idx], heights[i]
            names[i] , names[max_idx] = names[max_idx], names[i]

        return(names)
