class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''.join(filter(str.isalnum, s)).lower()
        return True if cleaned_text == cleaned_text[::-1] else False
