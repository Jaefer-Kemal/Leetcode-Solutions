class Solution:
    def kthCharacter(self, k: int) -> str:
        length = 2 ** ceil(log2(k))

        def generate(length):

            if length == 1:
                return ["a"]

            previous = generate(length // 2)
            
            len_ = len(previous)
            for i in range(len_):
                char = previous[i]
                if char == "z":
                    previous.append("a")
                else:
                    new_char = chr(ord(char) + 1)
                    previous.append(new_char)
            return previous
            
        return generate(length)[k - 1]

