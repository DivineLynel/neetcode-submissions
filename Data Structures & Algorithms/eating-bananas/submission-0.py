class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimun = 1 #left
        maximum = max(piles) #right
        while minimun <= maximum:
            mid = (minimun + maximum) // 2
            total_h = 0
            for x in piles:
                total_h += (x + mid - 1) // mid
            if total_h <= h:
                maximum = mid - 1
            if total_h > h:
                minimun = mid + 1
        return minimun