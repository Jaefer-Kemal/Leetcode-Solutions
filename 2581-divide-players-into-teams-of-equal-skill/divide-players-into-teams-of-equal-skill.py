class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        check = set()
        merge = []
        ans = 0
        for i in range(0,len(skill)//2):
            ch = skill[i] * skill[-(i + 1)]
            
            total = skill[i] + skill[-(i + 1)]
            if i == 0:
                check.add(total)
            if total not in check:
                return -1
            ans += ch
        
        return ans
           
        