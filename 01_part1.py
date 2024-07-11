final_result = 0
line = input()
 
while line != "stop":
    split_line = [x for x in line if x.isdigit()]
 
    if len(split_line) >= 2:
        current_result = split_line[0] + split_line[-1]
    else:
        current_result = split_line[0] * 2
 
    final_result += int(current_result)
 
    line = input()
 
print(final_result)
