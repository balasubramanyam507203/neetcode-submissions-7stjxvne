class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        imagine = set()

        for num in nums:
            if num in imagine:
                return True
            imagine.add(num)
        return False
    