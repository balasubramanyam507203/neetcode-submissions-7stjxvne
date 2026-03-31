class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_set = {}

        for i,num in enumerate(nums):
            subtraction = target - num

            if subtraction in empty_set:
                return[empty_set[subtraction],i]
            empty_set[num] = i
        return[]