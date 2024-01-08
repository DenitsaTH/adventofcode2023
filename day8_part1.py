from collections import deque
 
directions = input()
directions_queue = deque(directions)
positions = {}
 
current_position = input()
 
while current_position != "stop":
    if current_position == "":
        current_position = input()
        continue
    key = current_position.split(" = ")[0]
    value = current_position.split(" = ")[1].split(", ")
    positions[key] = [value[0].strip("("), value[1].strip(")")]
 
    current_position = input()
 
starting_key = "AAA"
ending_key = "ZZZ"
step_counter = 0
 
while True:
    current_direction = directions_queue[0]
    if current_direction == "R":
        starting_key = positions[starting_key][1]
    else:
        starting_key = positions[starting_key][0]
    step_counter += 1
    directions_queue.popleft()
    directions_queue.append(current_direction)
 
    if starting_key == ending_key:
        break
 
print(step_counter)
