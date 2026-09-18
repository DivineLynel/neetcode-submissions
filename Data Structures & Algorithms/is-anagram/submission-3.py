class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        baseS, baseT = {}, {}
        for char in range(len(s)):
            baseS[s[char]] = 1 + baseS.get(s[char], 0)
            baseT[t[char]] = 1 + baseT.get(t[char], 0)
        return baseS == baseT