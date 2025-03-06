class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        
        opp = -1
        chance = maxDoubles
        
        while target:
            if chance and target % 2 == 0:
                target //= 2
                chance -= 1
                opp += 1
            elif chance:
                target -= 1
                opp += 1
            else:
                opp += target
                target = 0

        return opp