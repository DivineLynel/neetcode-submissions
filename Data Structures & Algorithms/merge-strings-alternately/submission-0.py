class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        for i, n in zip(word1, word2):
            ans += i + n
            word1, word2 = word1[1:], word2[1:]
        if len(word1) > 0:
            ans += word1
        if len(word2) > 0:
            ans += word2 
        return ans