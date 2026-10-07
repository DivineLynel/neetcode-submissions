class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        nines = 0
        ndigits = len(digits)
        while digits[-nines-1] == 9:
            nines += 1
            if nines == ndigits:
                return [1] + [0] * ndigits

        digits[-nines-1] += 1
        
        if nines > 0:
            digits[-nines:] = [0]*nines

        
        return digits
