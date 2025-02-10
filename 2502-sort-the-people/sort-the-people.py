class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        j = len(names)

        while j >= 0:
            for i in range(0,j - 1):
                if heights[i] < heights[i + 1]:
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
                    names[i], names[i + 1] = names[i + 1], names[i]
            j -= 1
        
        return names