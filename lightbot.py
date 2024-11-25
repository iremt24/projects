# I initially had the terrain, grey, starting_square and starting_direction as the inputs of the lightbot function below but
# in today's lecture Erkcan hoca said that the level should be set separately. I came up with the setlevel function after that.
# The default value of the terrain is a 10 x 10 matrix with all blue squares. The default value for the starting square is
# bottom left and the default value for the starting direction is rightward.

def setlevel(terrain = np.zeros((10, 10)), grey = [], starting_square = None, starting_direction = "→"):
    if starting_square == None:
        starting_square = (terrain.shape[0] - 1, 0)
    # Since the default value for the starting square depends on the input for the terrain, I set it inside the function.
    return terrain, grey, starting_square, starting_direction

level = setlevel()
# I store the conditions for a level inside a variable. This can be changed by changing the input for setlevel().

def lightbot(commands, level):
    
    terrain = level[0]
    grey = level[1]
    starting_square = level[2]
    starting_direction = level[3]
    
    A = np.zeros(terrain.shape, dtype = "object") # This is the matrix I will modify according to the commands and display with 
                                                  # the squares lit up. I will not show the height of the squares here,
                                                  # because I am not sure it would look very nice.
    i, j = starting_square
    A[i, j] = starting_direction
    lit = False
    lit_squares = []
    direction = "→"
    direction_list = ["←", "↑", "→", "↓"]
    for k in range(len(commands)):
        if commands[k] == "@":
            if (i, j) in lit_squares:
                lit_squares.remove((i, j)) # an already lit up square will go back to 0 if light command is used on it again
                A[i, j] = "*"
                lit = False
            else:
                if (i, j) not in grey: # check if the square is blue
                    lit = True
                    lit_squares.append((i, j))
                    A[i, j] = "*"
        elif commands[k] == "^":
            x, y = i, j # I will store i, j (the square before moving forward) because I will modify it later
            can_move = False
            if direction == "↑" and i > 0 and terrain[i-1, j] == terrain[i, j]: # added extra conditions for the height and indices
                i, j = i-1, j
                A[i, j] = "↑"
                can_move = True
            elif direction == "↓" and i < terrain.shape[0] - 1 and terrain[i+1, j] == terrain[i, j]:
                i , j = i+1, j
                A[i, j] = "↓"
                can_move = True
            elif direction == "→" and j < terrain.shape[1] - 1 and terrain[i, j+1] == terrain[i, j]:
                i, j = i, j+1
                A[i, j] = "→"
                can_move = True
            elif direction == "←" and j > 0 and terrain[i, j-1] == terrain[i, j]:
                i , j = i, j-1
                A[i, j] = "←"
                can_move = True
            else: 
                A[i, j] = direction
            if can_move == True:
                if (x, y) in lit_squares:
                    lit = True
                if lit == True:
                    A[x, y] = 1
                    if (x, y) not in lit_squares:
                        lit_squares.append((x, y))
                    lit = False
                else:
                    A[x, y] = 0
        elif commands[k] == "*": # This part is the same as the move forward command, I only changed the height condition to !=
            x, y = i, j
            can_move = False
            if direction == "↑" and i > 0 and terrain[i-1, j] != terrain[i, j]:
                i, j = i-1, j
                A[i, j] = "↑"
                can_move = True
            elif direction == "↓" and i < terrain.shape[0] - 1 and terrain[i+1, j] != terrain[i, j]:
                i , j = i+1, j
                A[i, j] = "↓"
                can_move = True
            elif direction == "→" and j < terrain.shape[1] - 1 and terrain[i, j+1] != terrain[i, j]:
                i, j = i, j+1
                A[i, j] = "→"
                can_move = True
            elif direction == "←" and j > 0 and terrain[i, j-1] != terrain[i, j]:
                i , j = i, j-1
                A[i, j] = "←"
                can_move = True
            else: 
                A[i, j] = direction
            if can_move == True:
                if (x, y) in lit_squares:
                    lit = True
                if lit == True:
                    A[x, y] = 1
                    if (x, y) not in lit_squares:
                        lit_squares.append((x, y)) 
                    lit = False
                else:
                    A[x, y] = 0
        elif commands[k] == "<":
            for k in range(len(direction_list)):
                if direction_list[k] == direction:
                    direction = direction_list[k-1]
                    break
            A[i, j] = direction
        elif commands[k] == ">":
            for l in range(len(direction_list)):
                if direction_list[l] == direction and l != 3:
                    direction = direction_list[l+1]
                    break
                elif direction_list[l] == direction and l == 3:
                    direction = direction_list[0]
                    break
            A[i, j] = direction
    # I added a set of function attributes in order to be able to access certain variables / output directly
    lightbot.coordinates = (i, j)
    lightbot.direction = direction
    lightbot.lit_squares = lit_squares
    lightbot.terrain = terrain
    return(A)