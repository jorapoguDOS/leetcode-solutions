class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        long_diag = 0
        max_area = 0
        for i in dimensions:
            cur_diag = (i[0]**2 + i[1]**2)**(1/2)
            if cur_diag > long_diag:
                long_diag = cur_diag
                max_area = i[0] * i[1]
            elif cur_diag == long_diag:
                area = i[0] * i[1]
                if area > max_area:
                    max_area = area

        return max_area