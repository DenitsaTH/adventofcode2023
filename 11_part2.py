def expand_galaxies(matrix):
    non_empty_cols = []
    matrix_copy = matrix.copy()

    for line in range(len(matrix)):
        if "#" not in matrix[line]:
            for idx, char in enumerate(matrix_copy[line]):
                matrix_copy[line][idx] = "*"
        else:
            for char in range(len(matrix[line])):
                if matrix[line][char] == "#":
                    non_empty_cols.append(char)

    non_empty_cols = sorted(set(non_empty_cols))

    second_matrix_copy = matrix_copy.copy()

    for row in range(len(matrix_copy)):
        for col in range(len(matrix_copy[row])):
            if col not in non_empty_cols:
                second_matrix_copy[row][col] = "*"

    return second_matrix_copy


line = input()
galaxies = []


while line != "stop":
    current_line = []
    for char in line:
        current_line.append(char)
    galaxies.append(current_line)
    
    line = input()


galaxies = expand_galaxies(galaxies)

for line in galaxies:
    print(line)
galaxies_coordinates = []

for row in range(len(galaxies)):
    for col in range(len(galaxies[row])):
        if galaxies[row][col] == "#":
            current_coordinates = [row, col]
            galaxies_coordinates.append(current_coordinates)

final_result = 0
current_result = 0

for galaxy in range(len(galaxies_coordinates) - 1):
    for next_galaxy in range(len(galaxies_coordinates[galaxy + 1::])):
        current_result = abs(galaxies_coordinates[galaxy + 1::][next_galaxy][0] - galaxies_coordinates[galaxy][0]) + abs(galaxies_coordinates[galaxy + 1::][next_galaxy][1] - galaxies_coordinates[galaxy][1])

        first_row, first_col = galaxies_coordinates[galaxy][0], galaxies_coordinates[galaxy][1]
        second_row, second_col = galaxies_coordinates[galaxy + 1::][next_galaxy][0], galaxies_coordinates[galaxy + 1::][next_galaxy][1]
        
        for row in range(first_row + 1, second_row + 1):
            if galaxies[row][first_col] == "*":
                current_result += 999999

        if second_col > first_col:
            for col in range(first_col + 1, second_col + 1):
                if galaxies[second_row][col] == "*":
                    current_result += 999999
        elif first_col > second_col:
            for col in range(first_col - 1, second_col - 1, -1):
                if galaxies[second_row][col] == "*":
                    current_result += 999999

        final_result += current_result

print(final_result)
