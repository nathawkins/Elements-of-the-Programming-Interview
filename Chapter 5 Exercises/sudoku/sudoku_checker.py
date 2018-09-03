##Program to score a sudoku board. Requires it to be stored
##as a 2D numpy array or list of lists.


##Need to import numpy library to be able to read in boards
##as txt files, won't be using array functionality though
# import numpy as np
# data = np.loadtxt('complete_solution.txt', delimiter = ",")
# data = np.loadtxt('incorrect_solution.txt', delimiter = ",")

##Test case defined as a list of lists to verify either behavior works
data = [[5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]]


##Function that checks to see whether or not each row, column,
##or region that needs to be scored contains the values 1-9 
##and has no repeats
def check_completion(input_section):
    verify_against = [1,2,3,4,5,6,7,8,9]
    ##If the input is a list
    if type(input_section) == type(verify_against):
        ##sort each row and see if they match
        return verify_against == sorted(input_section)
    ##otherwise, make the verification list into an array
    verify_against = np.array(verify_against)
    ##sort the input array and see perform the same comparison
    comparison_result = np.sort(input_section) == verify_against 
    return comparison_result.all()

##Function to section the board into 3x3 sections
##to check not only rows and columns, but if regions have
##acceptable inputs
def section_board(board):
    ##if the input is a list of lists
    if type(board) == type(list()):
        ##make a list of flattened regions to verify
        flattened_grids = []
        ##sections to check, groupings of 3 to move to next 
        ##3x3 area
        row_index = [0, 3, 6]
        col_index = [0, 3, 6]
        
        ##for each of the row indices
        for i in row_index:
            ##iterate through column indices
            for j in col_index:
                ##keep track of a list for this
                ##3x3 region
                region = []
                ##iterate through indexed lists
                for item in board[i:i+3]:
                    ##add j through j + 3 to region
                    region += item[j:j+3]

                ##append this to our list of flattened regions
                flattened_grids.append(region)
        ##return list of lists
        return flattened_grids

    ##otherwise, do the same thing using numpy array
    ##functionality
    else:
        flattened_grids = []
        rows = [0, 3, 6]
        cols = [0, 3, 6]
        for i in rows:
            for j in cols:
                flattened_grids.append(board[i:i+3, j:j+3].flatten())
        return flattened_grids

##Function to check board
def check_sudoku(board):
    ##Whether it is list or array, check rows for correctness first
    ##since it is the least computationally expensive.
    ##Next, iterate through columns and score those.
    ##Finally, iterate through 3x3 regions.
    ##The scoring is done in order of increasing computational
    ##complexity and cost. 
    if type(board) == type(list()):
        for i in board:
            if not check_completion(i):
                print("Repeat Values in the Same Row")
                print(i)
                return False

        for j in range(len(board)):
            if not check_completion([board[x][j] for x in range(len(board))]):
                print("Repeat Values in the Same Column")
                return False

        regions = section_board(board)
        for region in regions:
            if not check_completion(region):
                print("Repeat Values in the Same Region")
                return False
                
        return True


    else:    
        for i in board:
            if not check_completion(i):
                print("Repeat Values in the Same Row")
                return False

        for j in range(board.shape[1]):
            if not check_completion(board[:,j]):
                print("Repeat Values in the Same Column")
                return False

        regions = section_board(board)
        for region in regions:
            if not check_completion(region):
                print("Repeat Values in the Same Region")
                return False
                
        return True

print(check_sudoku(data))