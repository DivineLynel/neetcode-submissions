class Solution:
    def isValid(self, s: str) -> bool:
        
        marker = []
        fit = {']': '[', '}': '{', ')': '('}

        for i in s:
            if i in '[({':
                marker.append(i)
            elif i in '])}':
                if not marker or marker.pop() != fit[i]:
                    return False
        return not marker
