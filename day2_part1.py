colours_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}
 
current_game = input()
possible_games_score = 0
 
while current_game != 'stop':
    current_game_explode = current_game.split(": ")
    game_number = int(current_game_explode[0].split()[1])
    all_games_current_line = [x for x in current_game_explode[1].split("; ")]
 
    game_is_possible = True
 
    for x in all_games_current_line:
        if not game_is_possible:
            break
        x = x.split(", ")
        for idx, colour in enumerate(x):
            current_colour = x[idx].split()[1]
            current_value = x[idx].split()[0]
            if colours_dict[current_colour] < int(current_value):
                game_is_possible = False
                break
        if not game_is_possible:
            break
        game_is_possible = True
 
    if game_is_possible:
        possible_games_score += game_number
    current_game = input()
 
print(possible_games_score)
