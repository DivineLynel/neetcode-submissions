class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        register = {}
        count = 0
        for i, items in enumerate(nums):
            if items == 1:
                count += 1
            else:
                register[i] = count
                count = 0
        if register and max(register.values()) > count:
            return max(register.values())
        else:
            return count