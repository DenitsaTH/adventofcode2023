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
 
 
def make_card_stronger(current_type, counter):
    if current_type == "High card":
        return "One pair"
    if current_type == "One pair":
        return "Three of a kind"
    if current_type == "Two pair" and counter == 1:
        return "Full house"
    if current_type == "Two pair" and counter == 2:
        return "Four of a kind"
    if current_type == "Three of a kind":
        return "Four of a kind"
    if current_type == "Full house":
        return "Five of a kind"
    if current_type == "Four of a kind":
        return "Five of a kind"
    return "Five of a kind"
 
 
def replace_all_letters(current_type, letters_dict):
    for idx, hand in enumerate(current_type):
        current_hand_cards = hand[0]
        for char in current_hand_cards:
            if char in letters_dict.keys():
                current_type[idx][0] = current_type[idx][0].replace(char, letters_dict[char])
    return current_type
 
 
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
    "J": "1",
    "Q": "D",
    "K": "E",
    "A": "F"
}
 
rank = 0
while line != 'stop':
    current_card = line.split()[0]
    current_card_bid = int(line.split()[1])
    current_card_type = get_card_type(current_card)
 
    if "J" in current_card:
        j_counter = current_card.count("J")
        current_card_type = make_card_stronger(current_card_type, j_counter)
 
    current_values = [current_card, current_card_bid]
    cards[current_card_type].append(current_values)
 
    line = input()
 
counter = 0
result = 0
 
for card_type in cards.keys():
    if cards[card_type]:
        cards[card_type] = replace_all_letters(cards[card_type], letter_values)
        cards[card_type].sort(key=lambda x: x[0])
 
        for hand in cards[card_type]:
            counter += 1
            result += counter * hand[1]
 
print(result)
