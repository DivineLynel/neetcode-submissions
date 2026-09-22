class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in ans:
                ans[key] = []
            ans[key].append(i)
        return list(ans.values())