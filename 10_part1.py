import math
 
 
def get_starting_point(sketch):
    for rr in range(len(sketch)):
        for cc in range(len(sketch[rr])):
            if sketch[rr][cc] == "S":
                starting_position = sketch[rr][cc]
                return rr, cc
 
 
def get_next_position(sketch, rr, cc, current_direction):
    current_pipe = sketch[rr][cc]
    if current_pipe == "|" and current_direction == "up":
        rr -= 1
    elif current_pipe == "|" and current_direction == "down":
        rr += 1
    elif current_pipe == "-" and current_direction == "right":
        cc += 1
    elif current_pipe == "-" and current_direction == "left":
        cc -= 1
    elif current_pipe == "7" and current_direction == "right":
        rr += 1
        current_direction = "down"
    elif current_pipe == "7" and current_direction == "up":
        cc -= 1
        current_direction = "left"
    elif current_pipe == "L" and current_direction == "down":
        cc += 1
        current_direction = "right"
    elif current_pipe == "L" and current_direction == "left":
        rr -= 1
        current_direction = "up"
    elif current_pipe == "J" and current_direction == "down":
        cc -= 1
        current_direction = "left"
    elif current_pipe == "J" and current_direction == "right":
        rr -= 1
        current_direction = "up"
    elif current_pipe == "F" and current_direction == "left":
        rr += 1
        current_direction = "down"
    elif current_pipe == "F" and current_direction == "up":
        cc += 1
        current_direction = "right"
 
    return rr, cc, current_direction
 
 
line = input()
matrix = []
 
while line != "stop":
    current_line = []
 
    for char in line:
        current_line.append(char)
 
    matrix.append(current_line)
 
    line = input()
 
row, col = get_starting_point(matrix)
direction = ""
 
if matrix[row][col + 1] != "." and matrix[row][col + 1] not in "|FL":
    col += 1
    direction = "right"
elif matrix[row][col - 1] != "." and matrix[row][col - 1] not in "|J7":
    col -= 1
    direction = "left"
elif matrix[row - 1][col] != "." and matrix[row - 1][col] not in "-LJ":
    row -= 1
    direction = "up"
elif matrix[row + 1][col] != "." and matrix[row + 1][col] not in "-7F":
    row += 1
    direction = "down"
 
all_steps = 0
 
while True:
    row, col, direction = get_next_position(matrix, row, col, direction)
    all_steps += 1
 
    if matrix[row][col] == "S":
        break
 
print(math.ceil(all_steps / 2))