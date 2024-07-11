card = input()
final_result = 0
 
while card != "stop":
    current_card = card.split(": ")
    all_numbers = current_card[1].split(" | ")
    winning_numbers = all_numbers[0].split()
    my_numbers = all_numbers[1].split()
    first_win = False
    current_card_result = None
 
    for x in my_numbers:
        for y in winning_numbers:
            if x == y and not current_card_result:
                first_win = True
                current_card_result = 1
            if x == y and not first_win:
                current_card_result *= 2
            first_win = False
 
    if current_card_result is not None:
        final_result += current_card_result
 
    card = input()
 
print(final_result)
