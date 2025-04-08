class Solution:
    def valid(self, ranks, cars, time):
        total_cars = 0
        for rank in ranks:
            total_cars += floor(sqrt((time / rank)))

        return total_cars >= cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = max(ranks) * cars * cars
        res = None

        while low <= high:
            mid = (low + high) // 2

            if self.valid(ranks, cars, mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res

