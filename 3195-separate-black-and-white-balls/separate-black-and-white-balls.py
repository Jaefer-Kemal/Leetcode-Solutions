class Solution:
    def minimumSteps(self, s: str) -> int:
        holder = 0
        seeker = 0
        size = len(s)
        s = list(s)
        min_operation = 0

        while holder < size and seeker < size:
            if s[seeker] == '0':
                if s[holder] == '1':
                    s[holder], s[seeker] = s[seeker], s[holder]
                    min_operation += seeker - holder
                    holder += 1
                    seeker += 1
                else:
                    holder += 1 

                if holder >= seeker:
                    seeker = holder + 1
            else:
                seeker += 1

        return min_operation