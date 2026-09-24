class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        repeats = tot = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                repeats += 1
                if repeats > tot:
                    tot = repeats
            else:
                repeats = 0
        return tot