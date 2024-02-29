class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] != ".":
                idx = ord(word[i]) - ord("a")
                if not node.children[idx]:
                    return False
                return dfs(node.children[idx], i + 1)
            else:
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
        return dfs(self.root, 0)


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)