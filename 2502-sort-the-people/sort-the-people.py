class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maximum_height = 10 ** 5 + 1
        height_array = ["" for _ in range(maximum_height)]

        for i in range(len(names)):
            index = heights[i]

            height_array[index] = names[i]

        res = []

        for name in height_array[::-1]:
            if name:
                res.append(name)

        return res
            


        '''Insertion Sort'''
        size = len(names)
        for i in range(1, size):
            j = i - 1
            current_index = i
            while j >= 0:
                if heights[j] < heights[current_index]:
                    heights[current_index], heights[j] = heights[j], heights[current_index]
                    names[current_index], names[j] = names[j], names[current_index]
                else:
                    break
                j -= 1
                current_index -= 1
        
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