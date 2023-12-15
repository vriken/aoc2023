#part 1
def extract_and_sum_calibrations(lines):
    total_sum = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            total_sum += int(first_digit + last_digit)
    return total_sum

calibration_sum = extract_and_sum_calibrations(lines)
calibration_sum

#53386

#part 2
num_map = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def word_to_digit(word):
    return num_map.get(word)

def find_numbers(line):
    words = line.split()
    found_nums = []
    for word in words:
        if word.isdigit():
            found_nums.append(word)
        elif word_to_digit(word):
            found_nums.append(word_to_digit(word))
    return found_nums

total_sum = 0
for line in lines:
    numbers = find_numbers(line.strip())
    if numbers:
        total_sum += int(numbers[0]) + int(numbers[-1])

print(total_sum)


#53312
