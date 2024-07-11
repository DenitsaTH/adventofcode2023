def get_new_values(ll):
    result = []
    for el in range(len(ll) - 1):
        result.append(ll[el + 1] - ll[el])
 
    return result
 
 
line = input()
final_result = 0
 
while line != "stop":
    current_line = [int(x) for x in line.split()]
    new_values = get_new_values(current_line)
    first_placeholders = [current_line[0]]
    new_values_set = set()
 
    while {0} != new_values_set:
        first_placeholders.append(new_values[0])
        new_values = get_new_values(new_values)
        new_values_set = set(new_values)
 
    reversed_placeholders = first_placeholders[::-1]
    current_result = reversed_placeholders[0]
    for idx in range(len(reversed_placeholders) - 1):
        current_result = reversed_placeholders[idx + 1] - current_result
 
    final_result += current_result
    line = input()
 
print(final_result)