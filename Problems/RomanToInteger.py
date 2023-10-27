class Solution:
    def romanToInt(self, s: str) -> int:
        numberDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for letter in s:
            value = numberDict[letter]
            result += value

        return result

sol = Solution()
print(sol.romanToInt("III"))