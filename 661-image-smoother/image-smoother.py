from math import floor
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    
        res = []

        for row in range(len(img)):
            r_row = []
            for col in range(len(img[0])):
                sum_ = 0
                len_ = 0
                for r in range(row - 1,row + 2):
                    for c in range(col - 1, col + 2):
                        if r == -1 or r == len(img) or c == -1 or c == len(img[0]):
                            continue
                        else:
                            sum_ += img[r][c]
                            len_ += 1
                r_row.append(floor(sum_/len_))
            res.append(r_row)
            
        return res


                        



        '''First Solution'''
        # res = []
        # for row in range(len(img)):
        #     row1 = []
        #     for col in range(len(img[0])):
        #         sum_ = img[row][col]
        #         len_ = 1

        #         if row - 1 != -1:
        #             sum_ += img[row - 1][col]
        #             len_ += 1

        #             if col - 1 != -1:
        #                 sum_ += img[row - 1][col - 1]
        #                 len_ += 1

        #             if col + 1 != len(img[0]):
        #                 sum_ += img[row - 1][col + 1]
        #                 len_ += 1

        #         if col - 1 != -1:
        #             sum_ += img[row][col - 1]
        #             len_ += 1

                
        #         if  row + 1 != len(img):
        #             sum_ += img[row + 1][col]
        #             len_ += 1

        #             if col - 1 != -1:
        #                 sum_ += img[row + 1][col - 1]
        #                 len_ += 1

        #             if col + 1 != len(img[0]):
        #                 sum_ += img[row + 1][col + 1]
        #                 len_ += 1
                
        #         if col + 1 != len(img[0]):
        #             sum_ += img[row][col + 1]
        #             len_ += 1
                
        #         avg = floor(sum_/len_)
        #         row1.append(avg)
        #     res.append(row1)

        # return res
                
                
                

        