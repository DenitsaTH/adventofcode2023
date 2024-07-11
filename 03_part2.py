def check_if_special_char_is_adjacent(matrix, row, starting_idx, ending_idx):
 
    for col_idx in range(starting_idx, ending_idx + 1):
        cells_to_check = [
            (row - 1, col_idx - 1),
            (row - 1, col_idx),
            (row - 1, col_idx + 1),
            (row, col_idx - 1),
            (row, col_idx + 1),
            (row + 1, col_idx - 1),
            (row + 1, col_idx),
            (row + 1, col_idx + 1)
        ]
        for coordinates in cells_to_check:
            current_row = coordinates[0]
            current_col = coordinates[1]
            if 0 <= current_row < len(matrix):
                if 0 <= current_col < len(matrix[row]):
                    current_symbol = matrix[current_row][current_col]
                    if not current_symbol.isdigit() and current_symbol != ".":
                        return True, coordinates
    return False, None
 
 
matrix = []
current_line = input()
final_result = 0
 
while current_line != "stop":
    matrix.append([x for x in current_line])
    current_line = input()
 
positions = []
gears = {}
 
for row in range(len(matrix)):
    current_number = ""
    positions = []
 
    for col in range(len(matrix[row])):
        current_char = matrix[row][col]
 
        if current_char.isdigit():
            current_number += matrix[row][col]
            positions.append(col)
 
        if current_number and (not current_char.isdigit() or col == len(matrix[row]) - 1):
            starting_idx = positions[0]
            ending_idx = positions[-1]
            is_char_adjacent, \
                current_coordinates = check_if_special_char_is_adjacent(matrix, row, starting_idx, ending_idx)
            if is_char_adjacent:
                if current_coordinates not in gears:
                    gears[current_coordinates] = []
                gears[current_coordinates].append(current_number)
 
            current_number = ""
            positions = []
 
for key, value in gears.items():
    current_char_result = 1
    if len(value) == 2:
        for number in value:
            current_char_result *= int(number)
        final_result += current_char_result
 
print(final_result)
