
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]

            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right

            length = right - left + 1

            if length > longest:
                longest = length

        return longest