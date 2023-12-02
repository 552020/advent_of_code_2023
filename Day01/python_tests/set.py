import re

def extract_numbers_example(line):
    """ Extracts numbers from the given line considering both words and digits. """
    #pattern = r'\b(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9)\b'
    pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
    
    return re.findall(pattern, line, re.IGNORECASE)

def get_number(word):
    """ Convert word to number or return the digit itself """
    mapping = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return mapping.get(word.lower(), word)

def extract_and_process_line(line):
    """ Extracts the first and last number from the line and concatenates them """
    #print("Processing line:", line)
    numbers = extract_numbers_example(line)
    #print("Extracted numbers:", numbers)
    if numbers:
        first_number = get_number(numbers[0])
        last_number = get_number(numbers[-1])
        concatenated_number = int(first_number + last_number)
        #print("Concatenated number:", concatenated_number)
        return int(first_number + last_number)
    return 0

def calculate_total_sum_from_file(file_path):
    """ Reads from a file and calculates the total sum of processed numbers """
    total_sum = 0
    with open(file_path, 'r') as file:
        line_number = 1
        for line in file:
            concatenated_number = extract_and_process_line(line.strip())
            total_sum += concatenated_number
            print(f"{line_number}: {concatenated_number}")
            line_number += 1
    return total_sum

input_file_path = './input_files/input_part_two.txt'
total_sum = calculate_total_sum_from_file(input_file_path)
print("Total Sum:", total_sum)
