class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        '''Insertion Sort'''
        size = len(names)
        for i in range(1, size):
            j = i - 1
            while j >= 0:
                if heights[j] < heights[i]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
                else:
                    break
                j -= 1
                i -= 1
        
        return names
                

        ''' Using Selection sort '''
        # size = len(names)
        # for i in range(size):
        #     min_index = i
        #     biggest_element = heights[i]
        #     for j in range(i + 1, size):
        #         if biggest_element < heights[j]:
        #             min_index = j
        #             biggest_element = heights[j]
        #     if i != min_index:
        #         heights[i], heights[min_index] = heights[min_index], heights[i]
        #         names[i], names[min_index] = names[min_index], names[i]
            
        # return names
        

        """ Using Bubble sort """
        # j = len(names)
        # while j >= 0:
        #     for i in range(0,j - 1):
        #         if heights[i] < heights[i + 1]:
        #             heights[i], heights[i + 1] = heights[i + 1], heights[i]
        #             names[i], names[i + 1] = names[i + 1], names[i]
        #     j -= 1
        
        # return names
