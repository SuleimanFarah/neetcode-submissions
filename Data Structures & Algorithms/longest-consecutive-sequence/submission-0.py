class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = set(nums)
        longestCounter = 0

        for val in lst:
            if (val - 1) not in lst:
                length = 0
                while (val + length) in lst:
                    length += 1
                longestCounter = max(length, longestCounter)

        return longestCounter
        