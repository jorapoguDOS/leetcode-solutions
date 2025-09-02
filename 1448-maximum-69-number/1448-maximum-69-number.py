class Solution:
    def maximum69Number (self, num: int) -> int:
        y = 0
        while num > 10**(y+1):
            y += 1
        x = 9*10**y
        while y >= 0:
            if num < x:
                num += 3*10**y
                return num
            y -= 1
            x += 9*10**y
        return num

