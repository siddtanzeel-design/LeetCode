class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i+1] for i in range(len(s)-1)):
            return 0

        if len(s) == 2:
            return -1

        mn, mx = min(s[1:-1]), max(s[1:-1])

        if s[0] <= s[-1] and (mn >= s[0] or mx <= s[-1]):
            return 1
        return 3 if s[-1] < mn and s[0] > mx else 2 