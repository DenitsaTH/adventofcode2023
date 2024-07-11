current_game = input()
final_score = 0
 
while current_game != 'stop':
    colours_dict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    current_game_score = 1
    current_game_explode = current_game.split(": ")
    game_number = int(current_game_explode[0].split()[1])
    all_games_current_line = [x for x in current_game_explode[1].split("; ")]
 
    for x in all_games_current_line:
        x = x.split(", ")
        for idx, colour in enumerate(x):
            current_colour = x[idx].split()[1]
            current_value = x[idx].split()[0]
            if colours_dict[current_colour] < int(current_value):
                colours_dict[current_colour] = int(current_value)
 
    current_game_score_list = [x for x in colours_dict.values()]
 
    for el in current_game_score_list:
        current_game_score *= el
 
    final_score += current_game_score
    current_game = input()
 
print(final_score)
