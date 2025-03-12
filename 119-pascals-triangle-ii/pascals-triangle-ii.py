class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]

        previous = self.getRow(rowIndex - 1)

        current = [1]

        for i in range(len(previous) - 1):
            val = previous[i] + previous[i + 1]
            current.append(val)
        
        current.append(1)

        return current

        