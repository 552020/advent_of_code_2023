# Manually processing each line according to the corrected logic

def get_number(word):
    """ Convert word to number or return the digit itself """
    mapping = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return mapping.get(word.lower(), word)

# Manually processing each line
lines_manual_processing = [
    'two1nine',       # 29 (two, nine)
    'eightwothree',   # 83 (eight, three)
    'abcone2threexyz',# 13 (one, three)
    'xtwone3four',    # 24 (two, four)
    '4nineeightseven2',# 42 (4, 2)
    'zoneight234',    # 84 (eight, 4)
    '7pqrstsixteen'   # 76 (7, six)
]

# Extract the first and last number from each line, then concatenate and sum them
total_sum_corrected = 0
for line in lines_manual_processing:
    numbers = extract_numbers_example(line)
    if numbers:
        first_number = get_number(numbers[0])
        last_number = get_number(numbers[-1])
        concatenated_number = int(first_number + last_number)
        total_sum_corrected += concatenated_number

total_sum_corrected

