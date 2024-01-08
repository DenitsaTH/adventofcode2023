def expand_galaxies(matrix):
    non_empty_cols = []
    matrix_copy = matrix.copy()
    added_rows = 0

    for line in range(len(matrix)):
        if "#" not in matrix[line]:
            added_rows += 1
            matrix_copy.insert(line + added_rows, ["."] * len(matrix[line]))
        else:
            for char in range(len(matrix[line])):
                if matrix[line][char] == "#":
                    non_empty_cols.append(char)

    non_empty_cols = sorted(set(non_empty_cols))

    second_matrix_copy = matrix_copy.copy()

    for row in range(len(matrix_copy)):
        added_cols = 0
        for col in range(len(matrix_copy[row])):
            if col not in non_empty_cols:
                added_cols += 1
                second_matrix_copy[row].insert(col + added_cols, ".")

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

for galaxy in range(len(galaxies_coordinates) - 1):
    for next_galaxy in range(len(galaxies_coordinates[galaxy + 1::])):
        current_result = abs(galaxies_coordinates[galaxy + 1::][next_galaxy][0] - galaxies_coordinates[galaxy][0]) + abs(galaxies_coordinates[galaxy + 1::][next_galaxy][1] - galaxies_coordinates[galaxy][1])
        final_result += current_result

print(final_result)
