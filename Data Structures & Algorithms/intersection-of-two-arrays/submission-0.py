class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            for i in nums2:
                if n == i and n not in ans:
                    ans.append(n)
        return ans