def is_digit(char):
    return char.isdigit()

def product_around_asterisk(lines, x, y):
    if lines[y][x] != '*':
        return None

    def extract_number(x, y, dx, dy):
        # Extracts a complete number from a specified direction
        number = ''
        x += dx
        y += dy
        while 0 <= x < len(lines[0]) and 0 <= y < len(lines) and lines[y][x].isdigit():
            number += lines[y][x]
            x += dx
            y += dy
        return int(number) if number else None

    # Check in all four directions for numbers
    number_left = extract_number(x, y, -1, 0)
    number_right = extract_number(x, y, 1, 0)
    number_above = extract_number(x, y, 0, -1)
    number_below = extract_number(x, y, 0, 1)

    # Identify and multiply any two numbers connected by the asterisk
    horizontal_numbers = [n for n in [number_left, number_right] if n is not None]
    vertical_numbers = [n for n in [number_above, number_below] if n is not None]

    if horizontal_numbers and vertical_numbers:
        return max(horizontal_numbers) * max(vertical_numbers)

    return None

lines_list = []
with open('input_files/input_two_test.txt', 'r') as file:
    for line in file:
        lines_list.append(line.strip())

products = []
processed_asterisks = set()
for y in range(len(lines_list)):
    for x in range(len(lines_list[y])):
        result = product_around_asterisk(lines_list, x, y, processed_asterisks)
        if result is not None:
            products.append(result)

total = sum(products)
print(f"Total sum of products: {total}")
