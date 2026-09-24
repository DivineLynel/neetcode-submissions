class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for s in words:
                if i in s and not i == s:
                    ans.append(i)
        return list(set(ans))