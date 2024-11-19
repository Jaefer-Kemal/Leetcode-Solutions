class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check = set()
        ans = 0
        l = 0
        r = len(skill) - 1
        while l < r:
            ch = skill[l] * skill[r]
            total = skill[l] + skill[r]
            
            if not check:
                check.add(total)
            if total not in check:
                return -1
           
            ans += ch
            
            l += 1
            r -= 1
            
        return ans
            
        
'''First Solution'''
#         for i in range(0,len(skill)//2):
#             ch = skill[i] * skill[-(i + 1)]
            
#             total = skill[i] + skill[-(i + 1)]
#             if i == 0:
#                 check.add(total)
#             if total not in check:
#                 return -1
#             ans += ch
        
#         return ans
           
        