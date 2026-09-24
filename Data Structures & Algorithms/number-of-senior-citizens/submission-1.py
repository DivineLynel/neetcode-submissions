class Solution:
    def countSeniors(self, details: List[str]) -> int:
        tot = 0
        for i in range(len(details)):
            age = details[i][11] + details[i][12]
            if int(age) > 60:
                tot += 1
            else:
                pass
        return tot