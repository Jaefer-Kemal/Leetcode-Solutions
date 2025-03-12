class Solution:
    def kthCharacter(self, k: int) -> str:
        string = ["a"]

        while len(string) < k:

            length = len(string)

            for i in range(length):
                if string[i] == "z":
                    string.append("a")
                else:
                    new_char = chr(ord(string[i]) + 1)
                    string.append(new_char)
            
        return string[k - 1]
