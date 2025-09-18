class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for key in ransom_count:
            if magazine_count[key] < ransom_count[key] :
                return False
        
        return True
        