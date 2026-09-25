class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in ans:
                return [ans[diff], i+1]
            ans[num] = i + 1 
        return ans