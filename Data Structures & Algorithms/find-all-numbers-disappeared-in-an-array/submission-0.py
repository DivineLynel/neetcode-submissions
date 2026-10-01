class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        miss = []
        lenght = len(nums)
        for i in range(lenght+1):
            if i == 0 or i in nums:
                pass
            else:
                miss.append(i)
        return miss