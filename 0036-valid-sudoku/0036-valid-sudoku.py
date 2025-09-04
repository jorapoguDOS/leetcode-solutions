class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
             
        # 9*9 False List
        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        # Check for the i'th row/column/box
        for i in range(9):
            # i is the corresponding i'th row/column/box

            for j in range(9):
                
                # board[i][j] corresponds to the j'th number (column) on the i'th row
                if board[i][j] != ".": # skip non-number values
                    
                    num = ord(board[i][j]) - ord('1') # get number (index)
                    box_indx = (i//3)*3 + (j//3)

                    # Check if number already exist in the num's corresponding row/column/box (i.e. if it is True)
                    if row[i][num] or col[j][num] or box[box_indx][num]:
                        return False
                    
                    # Save that the num exist for that row/col/box
                    row[i][num] = col[j][num] = box[box_indx][num] = True

        return True


        ''' 
        box index explained:
        
                    j = 0 1 2  3 4 5  6 7 8
                    j//3 = 0 0 0  1 1 1  2 2 2

        i = 0  i//3 = 0    0 0 0  1 1 1  2 2 2
        i = 1  i//3 = 0    0 0 0  1 1 1  2 2 2
        i = 2  i//3 = 0    0 0 0  1 1 1  2 2 2

        i = 3  i//3 = 1    3 3 3  4 4 4  5 5 5
        i = 4  i//3 = 1    3 3 3  4 4 4  5 5 5
        i = 5  i//3 = 1    3 3 3  4 4 4  5 5 5

        i = 6  i//3 = 2    6 6 6  7 7 7  8 8 8
        i = 7  i//3 = 2    6 6 6  7 7 7  8 8 8
        i = 8  i//3 = 2    6 6 6  7 7 7  8 8 8

        See that box_indx = (i//3) * 3 + j//3
        ''' 


            

