class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d1 = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in d1:
                return [d1[difference], i]
            else:
                d1[num] = i
        d1 = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in d1:
                return [d1[difference], i]
            else:
                d1[num] = i
