import numpy as np
def lightbot(commands):
    A = np.zeros((9, 8), dtype = "object")
    # Numpy matrices by default only allow same type of input for the entries. Changing the dtype to "object" allowed me to
    # store strings as entries as well.
    i, j = 8, 0 # start from bottom left corner,
    A[i, j] = "→" # facing rightward
    lit = False # I will light up squares by checking the value of this boolean variable
    lit_squares = [] # I will append the lit squares to a list, so that I would keep track of them
    direction = "→" # I will keep track of the current direction here
    direction_list = ["←", "↑", "→", "↓"] # cyclic list to turn left or right
    for x in range(len(commands)):
        if commands[x] == "@":
            lit = True
            A[i, j] = "*"
        elif commands[x] == "^":
            if (i,j) in lit_squares:
                lit = True # if the square is already lit
            if lit == True:
                A[i, j] = 1 # light the square, or leave it lit
                if (i, j) not in lit_squares:
                    lit_squares.append((i, j)) 
                lit = False # reset lit variable, so that I will not light up squares unnecesarily
            else:
                A[i, j] = 0
            if direction == "↑":
                i, j = i-1, j
                A[i, j] = "↑"
            elif direction == "↓":
                i , j = i+1, j
                A[i, j] = "↓"
            elif direction == "→":
                i, j = i, j+1
                A[i, j] = "→"
            elif direction == "←":
                i , j = i, j-1
                A[i, j] = "←"
        elif commands[x] == "<":
            for k in range(len(direction_list)):
                if direction_list[k] == direction:
                    direction = direction_list[k-1] # When I decrease the index by 1 in the cyclic list, lightbot turns left
                                                    # if k == 0, direction is set to direction[-1] which is the last element
                    break
            A[i, j] = direction
        elif commands[x] == ">":
            for k in range(len(direction_list)):
                if direction_list[k] == direction and k != 3:
                    direction = direction_list[k+1] # When I increase the index by 1 in the cyclic list, lightbot turns right
                    break
                elif direction_list[k] == direction and k == 3: # deal with k == 3 separately because then k + 1 is out of range
                    direction = direction_list[0]
                    break
            A[i, j] = direction
    return(A)