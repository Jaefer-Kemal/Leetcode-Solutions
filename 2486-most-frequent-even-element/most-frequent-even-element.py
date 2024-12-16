class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        frequent = 0
        minimum = {}
        for key, val in cnt.items():
            if key % 2 == 0 and frequent <= val:
                frequent = val
                if frequent not in minimum:
                    minimum[frequent] = key
                elif minimum[frequent] > key:
                    minimum[frequent] = key

        return minimum[frequent] if len(minimum) != 0 else -1

        