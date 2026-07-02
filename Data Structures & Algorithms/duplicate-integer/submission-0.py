class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for val in nums:
            if val not in dictionary:
                dictionary[val] = 1
            else:
                return True
        return False