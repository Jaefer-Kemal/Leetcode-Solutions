class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_zeroes = 0
        count_ones = 0

        for digit in s:
            if digit == "0":
                count_zeroes += 1
            else:
                count_ones += 1

        return ("1" * (count_ones - 1)) + ("0" * count_zeroes) + "1"

