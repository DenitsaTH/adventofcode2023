def get_card_type(card):
    chars_set = set()
    for char in card:
        chars_set.add(char)
 
    if len(chars_set) == 1:
        return "Five of a kind"
    if len(chars_set) == 2:
        for char in card:
            if card.count(char) == 4:
                return "Four of a kind"
        return "Full house"
    if len(chars_set) == 3:
        for char in card:
            if card.count(char) == 3:
                return "Three of a kind"
        return "Two pair"
    if len(chars_set) == 4:
        return "One pair"
    if len(chars_set) == 5:
        return "High card"
 
 
def replace_all_letters(type, letters_dict):
    for idx, hand in enumerate(type):
        current_hand_cards = hand[0]
        for char in current_hand_cards:
            if char in letters_dict.keys():
                type[idx][0] = type[idx][0].replace(char, letters_dict[char])
    return type
 
 
line = input()
 
cards = {
    "High card": [],
    "One pair": [],
    "Two pair": [],
    "Three of a kind": [],
    "Full house": [],
    "Four of a kind": [],
    "Five of a kind": [],
}
letter_values = {
    "T": "B",
    "J": "C",
    "Q": "D",
    "K": "E",
    "A": "F"
}
 
rank = 0
while line != 'stop':
    current_card = line.split()[0]
    current_card_bid = int(line.split()[1])
    current_card_type = get_card_type(current_card)
    current_values = [current_card, current_card_bid]
    cards[current_card_type].append(current_values)
 
    line = input()
 
counter = 0
result = 0
 
for type in cards.keys():
    print(type)
    if cards[type]:
        cards[type] = replace_all_letters(cards[type], letter_values)
        cards[type].sort(key=lambda x: x[0])
 
        for hand in cards[type]:
            counter += 1
            result += counter * hand[1]
            print(f"{hand}, {counter}, {result}")
 
print(result)
