class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_l = sorted(nums1 + nums2)
        mid = len(new_l) // 2

        if len(new_l) % 2 != 0:
            return new_l[mid]
        else:
            return (new_l[mid - 1]+ new_l[mid]) / 2