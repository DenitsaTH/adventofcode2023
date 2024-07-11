card = input()
final_result = 0
cards_dict = {}
 
while card != "stop":
    current_card = card.split(": ")
    all_numbers = current_card[1].split(" | ")
    card_number = int(current_card[0].split()[1])
    winning_numbers = all_numbers[0].split()
    my_numbers = all_numbers[1].split()
    if card_number not in cards_dict:
        cards_dict[card_number] = [0, 1]
 
    current_matches = 0
    for x in my_numbers:
        for y in winning_numbers:
            if x == y:
                current_matches += 1
    cards_dict[card_number][0] += current_matches
 
    card = input()
 
for key, value in cards_dict.items():
    for j in range(key + 1, key + value[0] + 1):
        cards_dict[j][1] += value[1]
 
final_result = 0
for key, value in cards_dict.items():
    final_result += value[1]
 
print(final_result)
