class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        diags = [[] for _ in range(2*n-1)]

        # Find the diagonals
        for i in range(n):
            s = n - 1 + i
            for j in range(n):
                diags[s].append(grid[i][j])
                s -= 1

        # Sort the diagonals
        for j in range(len(diags)):
            diags[j].sort(reverse = True if j+1 >= n else False)

        result = [[] for _ in range(n)]

        for i in range(n):
            s = n - 1 + i
            for _ in range(n):
                x = diags[s].pop(0)
                result[i].append(x)
                s -= 1

        return result