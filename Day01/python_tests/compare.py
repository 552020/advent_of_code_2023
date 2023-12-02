def read_file(file_path):
    """Reads the file and returns a dictionary of line number to number."""
    numbers = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) == 2:
                line_number = int(parts[0].strip())
                number = int(parts[1].strip())
                numbers[line_number] = number
    return numbers

def compare_files(file_path1, file_path2):
    """Compares two files and prints discrepancies."""
    file1_numbers = read_file(file_path1)
    file2_numbers = read_file(file_path2)

    for line_number, number1 in file1_numbers.items():
        number2 = file2_numbers.get(line_number)
        if number2 is None:
            print(f"Line {line_number} is missing in the second file.")
        elif number1 != number2:
            print(f"Line {line_number} differs: {number1} vs {number2}")

# Replace with your actual file paths
file_path1 = './output_lines_c'
file_path2 = './output_lines_py'

compare_files(file_path1, file_path2)
