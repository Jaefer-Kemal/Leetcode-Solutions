class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = 0
        count_L = 0

        balanced_ss = 0

        for char in s:
            if char == "R":
                count_R += 1
            elif char == "L":
                count_L += 1
            
            if count_L == count_R:
                balanced_ss += 1

                count_L = count_R = 0
        
        return balanced_ss