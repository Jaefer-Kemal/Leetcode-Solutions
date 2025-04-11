class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_candy = max(candies)

        truth_array = []

        for i in range(len(candies)):
            current_candy = extraCandies + candies[i]

            if greatest_candy <= current_candy:
                truth_array.append(True)

            else:
                truth_array.append(False)
        
        return truth_array