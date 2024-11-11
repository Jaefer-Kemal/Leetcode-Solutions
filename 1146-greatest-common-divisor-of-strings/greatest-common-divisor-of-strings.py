class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b%a,a)

        len1 , len2 = len(str1) , len(str2)
        gc = gcd(len1,len2)
        div1 , div2 = len1//gc , len2//gc

        sliced = str1[:gc]
        print(sliced)
        if div1 * sliced == str1 and div2 * sliced == str2:
            return sliced
        return ""