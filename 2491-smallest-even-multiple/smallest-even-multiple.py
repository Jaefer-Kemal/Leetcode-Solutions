
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b % a, a)

        return (2 * n //gcd(n,2))
        