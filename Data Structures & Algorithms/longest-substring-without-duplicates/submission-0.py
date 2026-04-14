class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        max_length = 0

        for i in range(n):
            seen = []
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.append(s[j])
                length = j - i + 1
                max_length = max(max_length, length)
        return max_length
        