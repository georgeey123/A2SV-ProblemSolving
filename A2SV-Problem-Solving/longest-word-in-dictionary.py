class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.is_end       

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True       

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ""
        trie = Trie()

        for word in words:
            trie.insert(word)

        for word in words:
            is_buildable = True
            for i in range(1, len(word)):
                if not trie.search(word[:i]):
                    is_buildable = False
                    break
            if is_buildable:
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word

        return res