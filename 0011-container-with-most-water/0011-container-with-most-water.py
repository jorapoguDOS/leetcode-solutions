class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        l_indx = 0
        r_indx = len(height) - 1
        left = height[l_indx]
        right = height[r_indx]
        dist = r_indx - l_indx

        while dist >= 1:
            if left > right:
                curr_vol = dist * right
                r_indx -= 1
                right = height[r_indx]
            else: 
                curr_vol = dist * left
                l_indx += 1
                left = height[l_indx]

            if curr_vol > max_vol:
                max_vol = curr_vol
            
            dist -= 1


        return max_vol

