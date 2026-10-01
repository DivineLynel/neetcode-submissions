class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for items in nums:
            if items not in count:
                count[items] = 0
            else:
                count[items] += 1
        return max(count, key=count.get)