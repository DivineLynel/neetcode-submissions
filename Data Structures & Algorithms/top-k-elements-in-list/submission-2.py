from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        # Sort keys based on count[x] in descending order, then take top k
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]
        