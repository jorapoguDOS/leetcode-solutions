class Solution:
    def romanToInt(self, s: str) -> int:
        rn = {"I":1, "V":5, "X":10,  "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for j in range(0, len(s)):
            if j < len(s)-1 and rn[s[j]] < rn[s[j+1]]:
                ans -= rn[s[j]]
            else:
                ans += rn[s[j]]
        return ans