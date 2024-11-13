from math import floor
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        point1 = 0

        res = []
        for row in range(len(img)):
            row1 = []
            for col in range(len(img[0])):
                sum_ = img[row][col]
                len_ = 1

                if row - 1 != -1:
                    sum_ += img[row - 1][col]
                    len_ += 1

                    if col - 1 != -1:
                        sum_ += img[row - 1][col - 1]
                        len_ += 1

                    if col + 1 != len(img[0]):
                        sum_ += img[row - 1][col + 1]
                        len_ += 1

                if col - 1 != -1:
                    sum_ += img[row][col - 1]
                    len_ += 1

                
                if  row + 1 != len(img):
                    sum_ += img[row + 1][col]
                    len_ += 1

                    if col - 1 != -1:
                        sum_ += img[row + 1][col - 1]
                        len_ += 1

                    if col + 1 != len(img[0]):
                        sum_ += img[row + 1][col + 1]
                        len_ += 1
                
                if col + 1 != len(img[0]):
                    sum_ += img[row][col + 1]
                    len_ += 1
                
                avg = floor(sum_/len_)
                row1.append(avg)
            res.append(row1)

        return res
                
                
                

        