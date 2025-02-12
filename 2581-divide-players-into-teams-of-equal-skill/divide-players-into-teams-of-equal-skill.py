class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        teams_chemistry = 0
        left = 0
        right = len(skill) - 1
        # Lets Assume that the first player and last player will be teamed up
        total_skill = skill[left] + skill[right]
        while left < right:
            if total_skill != skill[left] + skill[right]:
                return -1
            teams_chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1

        return teams_chemistry
        