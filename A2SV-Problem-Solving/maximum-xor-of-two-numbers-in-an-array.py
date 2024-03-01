class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for bit in word:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_end = True

    def search(self, word):
        cur = self.root
        xor_str = ""
        for bit in word:
            opposite_bit = '1' if bit == '0' else '0'
            if opposite_bit in cur.children:
                xor_str += '1'
                cur = cur.children[opposite_bit]
            else:
                xor_str += '0'
                cur = cur.children[bit]
        return int(xor_str, 2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_xor = 0
        for num in nums:
            bit_num = format(num, '032b')
            trie.insert(bit_num)
    
            xor_val = trie.search(bit_num)
            max_xor = max(max_xor, xor_val)
        return max_xor

