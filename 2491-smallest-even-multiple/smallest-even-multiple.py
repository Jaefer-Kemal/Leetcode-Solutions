from math import gcd
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return (2 * n)//gcd(n,2)
        