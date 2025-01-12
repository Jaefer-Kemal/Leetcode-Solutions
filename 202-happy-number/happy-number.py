class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            num = str(n * n)
        else:
            num = str(n)
        flag = True
        while len(num) > 1 or flag:
            n = 0
            if len(num) == 1:
                flag = False
            for i in num:
                n += (int(i) * int(i))
            num = str(n)
            print(num)
        return True if int(num) == 1 else False