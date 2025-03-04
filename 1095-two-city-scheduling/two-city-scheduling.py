class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key = lambda x: x[0] - x[1])
       
        minimum_cost = 0
        for i in range(n):
           minimum_cost += costs[i][0]
           minimum_cost += costs[-(i + 1)][1]

        return minimum_cost