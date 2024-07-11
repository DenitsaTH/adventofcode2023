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
 

def check_if_inside(rr, cc, matrix):
    counter = 0

    for cell in range(rr + 1, len(matrix)):
        if matrix[cell][cc] in "H*":
            counter += 1
    if counter % 2 == 0:
        return "0"
    else:
        counter = 0
    
    for cell in range(rr - 1, -1, -1):
        if matrix[cell][cc] in "H*":
            counter += 1
    if counter % 2 == 0:
        return "0"
    else:
        counter = 0
    
    for cell in range(cc + 1, len(matrix[rr])):
        if matrix[rr][cell] in "V*":
            counter += 1
    if counter % 2 == 0:
        return "0"
    else:
        counter = 0
    
    for cell in range(cc - 1, -1, -1):
        if matrix[rr][cell] in "V*":
            counter += 1
    if counter % 2 == 0:
        return "0"
    
    return "I"



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

while True:
    next_row, next_col, direction = get_next_position(matrix, row, col, direction)
    if matrix[row][col] == "|":
        matrix[row][col] = "V"
    elif matrix[row][col] in "-":
        matrix[row][col] = "H"
    elif matrix[row][col] in "7FLJ":
        matrix[row][col] = "*"
 
    if matrix[next_row][next_col] == "S":
        matrix[next_row][next_col] = "*"
        break

    row = next_row
    col = next_col

inside_counter = 0

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] not in "HV*":
            matrix[row][col] = check_if_inside(row, col, matrix)
            if matrix[row][col] == "I":
                inside_counter += 1

print(inside_counter)
