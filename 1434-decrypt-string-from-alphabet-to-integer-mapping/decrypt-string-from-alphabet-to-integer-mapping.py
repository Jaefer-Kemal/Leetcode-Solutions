class Solution:
    def freqAlphabets(self, s: str) -> str:
        l=0
        decrypt=""
        while l<len(s):
            if l+2<len(s )and s[l+2]=="#":
                ch=int(s[l:l+2])
                l+=3
            else:
                ch=int(s[l])
                l+=1
            decrypt+=(chr(ch+96))
        return decrypt
            

        