def check_if_word_starts_with_digit(current_line):
    for key in digits.keys():
        if current_line.startswith(key):
            return digits[key]
    return ""
 
 
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
 
final_result = 0
line = input()
 
while line != "stop":
    current_result = ""
 
    for idx in range(0, len(line)):
        if not line[idx].isdigit():
            string_to_check = line[idx::]
            word_to_digit = check_if_word_starts_with_digit(string_to_check)
            if word_to_digit:
                current_result += word_to_digit
                break
        else:
            current_result += line[idx]
            break
 
    for idx in range(len(line) - 1, -1, -1):
        if not line[idx].isdigit():
            string_to_check = line[idx::]
            word_to_digit = check_if_word_starts_with_digit(string_to_check)
            if word_to_digit:
                current_result += word_to_digit
                break
        else:
            current_result += line[idx]
            break
 
    if not len(current_result) == 2:
        current_result += current_result
 
    final_result += int(current_result)
    line = input()
 
print(final_result)
