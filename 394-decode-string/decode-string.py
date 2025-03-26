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
                    i, word = decode(i + 1)
                    repeated_word = word * int("".join(num)) 
                    stack.append(repeated_word)
                    num = []
                    continue
                
                elif s[i] == "]":
                    return (i + 1, "".join(stack))
                
                else:
                    stack.append(s[i])

                i += 1
            
            return (i, "".join(stack))
        
        i, word = decode(0)

        return word

