class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        def reverse(image):
            n = len(image)
            for row in range(n) :
                for col in range(n // 2):
                    image[row][col], image[row][-(col + 1)] = image[row][-(col + 1)] , image[row][col]

        def invert(image):
            n = len(image)
            for row in range(n):
                for col in range(n):
                    if image[row][col] == 0:
                        image[row][col] = 1
                    else:
                        image[row][col] = 0
        
        reverse(image)

        invert(image)

        return image

        