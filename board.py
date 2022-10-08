grid = [ [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
         [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
         [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
         [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
         [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
         [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
         [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
         [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
         [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(board[0])):
          if j % 3 == 0 and j != 0:
            print("|", end="")
            
          if j == 8:
            print(board[i][j])
          else:
            print(str(board[i][j]) + " ", end=" ")


def findEmpty(board):
    for x in range(len(board)): #going through vertically
        for y in range(len(board)): #going through horizontaly
            if board[x][y] == 0: # if spot on the board has 0 aka is empty: return the x, y of the board
                return (x, y)
        
    return False
    

def is_valid(board, num, pos):
    #horizontal
    for x in range(len(board[0])):
        if board[pos[0]][x] == num and pos[1] != x:
            return False
    #vertical
    for y in range(len(board[0])):
        if board[pos[0]][y] == num and pos[1] != x:
            return False
    
    box_x =  pos[1] // 3
    box_y =  pos[0] // 3 #checking which 3x3 we're in
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_y*3 + 3):  #this nesterd for loop will check all the 3x3 cubes
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
    

def solve(board):
    empty = findEmpty(board)
    if not empty:
        return True
    else:
        x, y = empty
    
    for i in range(1,10):
        if is_valid(board, i, (x, y)):  # if number 'i' is valid in a certain spot in the board, it will replace it, otherwise, continue.
            board[x][y] = i

            if solve(board): # recursively trying to solve it.
                return True
            
            board[x][y] = 0
    return False


printBoard(grid)
solve(grid)
print(solve(grid))
print("Solved board --------------------------------------")
printBoard(grid)
        
    
    
    
    
    

