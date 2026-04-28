from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return result