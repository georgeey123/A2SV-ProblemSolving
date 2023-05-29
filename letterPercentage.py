class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        percentage = 0
        for char in s:
            if char == letter:
                count += 1
        percentage = (count / len(s)) * 100
        rounded_percentage = int(percentage)
        return rounded_percentage
