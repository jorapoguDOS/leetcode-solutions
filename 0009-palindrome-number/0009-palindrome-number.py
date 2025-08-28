class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        ## soln 1
        k = x
        y = 0
        while k > 0:
            y = y * 10 + k % 10
            k = k // 10

        return x == y

        # # soln 2
        # x = str(x)
        # k = len(x)
        # return True if x[k//2 - 1::-1] == x[k//2 + (0 if k % 2 == 0 else 1):] else False

        