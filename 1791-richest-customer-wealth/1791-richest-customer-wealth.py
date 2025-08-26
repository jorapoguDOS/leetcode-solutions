class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            if sum > max_wealth:
                max_wealth = sum
        return max_wealth
        