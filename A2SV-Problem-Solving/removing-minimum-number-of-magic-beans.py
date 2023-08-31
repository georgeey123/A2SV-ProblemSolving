class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        diff = []
        total = sum(beans)

        for i in range(n):
            diff.append(total - (beans[i] * (n -i)))

        return min(diff)
        