#data
with open(file_path, 'r') as file:
    lines = file.readlines()

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
