class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictt = {}

        for word in words:
            dictt[word] = dictt.get(word, 0) + 1

        heap = [(-freq, word) for word, freq in dictt.items()]
        heapify(heap)

        res = [heappop(heap)[1] for _ in range(k)]

        return res
