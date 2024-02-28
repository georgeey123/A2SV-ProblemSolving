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

    # def search(self, word: str) -> bool:
    #     cur = self.root

    #     for ch in word:
    #         idx = ord(ch) - ord('a')
    #         if not cur.children[idx]:
    #             return False
    #         cur = cur.children[idx]
    #     return cur.is_end       

    def startsWith(self, word) -> bool:
        cur = self.root

        prefixstr = ""
        for ch in word:
            idx = ord(ch) - ord('a')
            if not cur.children[idx]:
                return prefixstr
            prefixstr += ch
            cur = cur.children[idx]
        return prefixstr        

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        # self.val = val

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        
        strs.sort()
        tree = Trie()

        tree.insert(strs[0])

        res = ""

        for word in strs[1:]:
            res = tree.startsWith(word)

        return res            