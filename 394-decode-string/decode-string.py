class Solution:
    def decodeString(self, s: str) -> str:
        
        def decode(index):
            stack = []
            num = []
            i = index

            while i < len(s):

                if s[i].isdigit():
                    num.append(s[i])

                elif s[i] == "[":
                    word, index = decode(i + 1)
                    new_word = int("".join(num)) * word
                    stack.append(new_word)
                    i = index # todo
                    num = []

                elif s[i] == "]":
                    return ("".join(stack), i)
                else:
                    stack.append(s[i])
                
                i += 1

            return ("".join(stack), i)
                    

        word, index = decode(0)

        return word



                

