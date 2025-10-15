class Solution:
    def romanToInt(self, s: str) -> int:
        rn = {"I":1, "V":5, "X":10,  "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        j = 0
        while j < len(s):
            if j < len(s)-1 and rn[s[j]] < rn[s[j+1]]:
                ans += rn[s[j+1]] - rn[s[j]]
                j += 2
            else:
                ans += rn[s[j]]
                j += 1
        return ans