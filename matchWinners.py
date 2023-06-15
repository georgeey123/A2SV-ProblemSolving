class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = defaultdict(int), defaultdict(int)

        for match in matches:

            winners[match[0]] += 1
            losers[match[1]] += 1

        res_1, res_2 = [], []

        for i, j in winners.items():
            if i not in losers:
                res_1.append(i)
        
        for n, m in losers.items():
            if m == 1:
                res_2.append(n)

        res_1.sort()
        res_2.sort()
        
        return [ res_1, res_2 ]
