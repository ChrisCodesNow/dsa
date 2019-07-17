'''
Approach 1:
n = size of board
nQueens(board, placed, row):
    Base case:
        Row out of range and placed Queens = n:
        => 1
    
    solutions = 0
    Iterate cols j [0 to n - 1]:
        Queen at (row, j) not threaten placed Queens:
            Place Queen in board and mark as placed
            solutions += Recursive compute nQueens at next row
            Remove placed Queen (row, j)

    Get solutions


Runtime: O()
Space Complexity: O()
'''
