class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in d1:
                return [d1[difference], i]
            else:
                d1[num] = i
