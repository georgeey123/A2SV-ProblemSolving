class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        common_chars = set(words[0])

        for word in words[1:]:
            common_chars = common_chars.intersection(set(word))

        result = []
        for char in common_chars:
            min_count = min(word.count(char) for word in words)
            result.extend([char] * min_count)

        return result
