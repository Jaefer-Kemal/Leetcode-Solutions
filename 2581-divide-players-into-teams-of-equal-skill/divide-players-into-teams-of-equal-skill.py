class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        total_teams_chemistry = 0
        left = 0
        right = len(skill) - 1
        # Lets Assume that the lowest skilled player will team up with highest skill player
        total_skill = skill[left] + skill[right]

        while left < right:

            if total_skill != skill[left] + skill[right]:
                return -1
                
            total_teams_chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1

        return total_teams_chemistry
        