def seeds_converted(starting_seeds, current_seeds):
    current_seeds_list = [int(x) for x in current_seeds.split()]
    destination_range_start = current_seeds_list[0]
    source_range_start = current_seeds_list[1]
    range_len = current_seeds_list[2]

    for idx, seed in enumerate(starting_seeds):
        if source_range_start <= seed < source_range_start + range_len and initial_seeds_copy[idx] == 0:
            starting_seeds[idx] = (seed - source_range_start) + destination_range_start
            initial_seeds_copy[idx] = starting_seeds[idx]

    return starting_seeds, initial_seeds_copy


current_line = input()
all_data = []
initial_seeds = []

while current_line != "stop":
    all_data.append(current_line)
    current_line = input()

for line in all_data:
    if line == '':
        initial_seeds_copy = [0] * len(initial_seeds)
        continue
    elif line.startswith("seeds:"):
        initial_seeds = [int(x) for x in line.split() if x.isdigit()]
    elif line[0].isalpha():
        continue
    else:
        initial_seeds, initial_seeds_copy = seeds_converted(initial_seeds, line)


print(min(initial_seeds))
