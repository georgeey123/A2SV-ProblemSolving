class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.count += 1

        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root

        count = 0
        for ch in word:
            cur = cur.children[ch]
            count += cur.count 
        return count   

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        res = []

        for word in words:
            trie.insert(word)

        for word in words:
            cur_sum = trie.search(word)
            res.append(cur_sum)
        return res
