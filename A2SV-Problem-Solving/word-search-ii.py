class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        rows, cols = len(board), len(board[0])
        res, path = set(), set()

        for word in words:
            trie.insert(word)

        def dfs(r, c, node, word): 

            if (r < 0 or c < 0 or 
            r == rows or c == cols or
            board[r][c] not in node.children or
            (r,c) in path):
                return 

            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_end:
                res.add(word)

            dfs(r, c + 1,node, word) 
            dfs(r, c - 1, node, word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, "")

        return list(res)
        