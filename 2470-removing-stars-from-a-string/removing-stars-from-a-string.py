class Solution:
    def removeStars(self, s: str) -> str:
        result = []

        for i in range(len(s)):
            if s[i] != '*':
                result.append(s[i])
            else:
                if len(result) > 0:
                    result.pop()

        return ''.join(result)