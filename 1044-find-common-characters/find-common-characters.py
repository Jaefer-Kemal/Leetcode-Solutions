class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=list(words[0])
        for word in words:
            res=[]
            for l in word:
                if l in common:
                    res.append(l)
                    common.remove(l)
            common=res
        return res