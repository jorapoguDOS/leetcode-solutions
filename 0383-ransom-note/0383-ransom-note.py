class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char = {}
        for i in ransomNote:
            if i in char:
                char[i] = char[i] + 1
            else:
                char[i] = 1
        
        possible = False
        for j in magazine:
            if j in char:
                char[j] -= 1
                if char[j] == 0:
                    del char[j]
            if not char:
                possible = True
                break
        
        return possible



