class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str,nums))
        # multiplying the string by 10 will repeat it 10 time and then order lexicographically
        res =  "".join(sorted(str_nums, key = lambda x: x * 10, reverse = True))

        if res[0] == "0":
            return "0"
        else:
            return res