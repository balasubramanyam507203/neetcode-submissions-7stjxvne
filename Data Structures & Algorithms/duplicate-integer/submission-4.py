class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        checking = set()

        for num in nums:
            if num in checking:
                return True
            checking.add(num)
        return False
    