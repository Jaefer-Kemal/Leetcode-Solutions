class Solution:
    def interpret(self, command: str) -> str:
        s=""
        l=0
        while l<len(command):
            if command[l]=="G":
                s+="G"
                l+=1
            elif command[l]=="(" and command[l+1]==")":
                s+="o"
                l+=2
            else:
                s+="al"
                l+=4
        return s
                
        