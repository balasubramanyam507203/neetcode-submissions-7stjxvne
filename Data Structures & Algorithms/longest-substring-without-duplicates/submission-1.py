class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s) #7
        max_length = 0

        for i in range(n): #0 #1
            seen = [] #z #x
            for j in range(i, n): #0 #1
                if s[j] in seen:
                    break
                seen.append(s[j])
                length = j - i + 1 #1
                max_length = max(max_length, length) #1
        return max_length
        