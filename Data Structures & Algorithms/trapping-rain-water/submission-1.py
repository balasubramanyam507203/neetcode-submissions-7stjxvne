class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0

        while left <= right:
            l = height[left]
            r = height[right]
            if l <= r:
                if l >= left_max:
                    left_max = l
                else:
                    water += left_max - l
                left += 1
            else:
                if r >= right_max:
                    right_max = r
                else:
                    water += right_max - r
                right -= 1
        return water
            

        

        