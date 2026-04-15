class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            curr_char = s[right]

            if curr_char in freq:
                freq[curr_char] += 1
            else:
                freq[curr_char] = 1
            
            if freq[curr_char] > max_freq:
                max_freq = freq[curr_char]

            window_size = right - left + 1

            while window_size - max_freq > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
                window_size = right - left + 1

            if window_size > longest:
                longest = window_size
        return longest