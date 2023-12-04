def extract_number(x, y, dx, dy):
    number = ''
    x += dx
    y += dy
    while 0 <= x < len(lines[0]) and 0 <= y < len(lines) and (lines[y][x].isdigit() or lines[y][x] == '*'):
        if lines[y][x].isdigit():
            number += lines[y][x]
        x += dx
        y += dy
    return int(number) if number else None

def product_around_asterisk(lines, x, y, processed_asterisks):
    if lines[y][x] != '*' or (x, y) in processed_asterisks:
        return None

    number_left = extract_number(x, y, -1, 0)
    number_right = extract_number(x, y, 1, 0)
    number_above = extract_number(x, y, 0, -1)
    number_below = extract_number(x, y, 0, 1)

    horizontal_numbers = [n for n in [number_left, number_right] if n is not None]
    vertical_numbers = [n for n in [number_above, number_below] if n is not None]
    print(f"Processing asterisk at ({x}, {y})")
    print(f"Number left: {number_left}, Number right: {number_right}")
    print(f"Number above: {number_above}, Number below: {number_below}")

    if horizontal_numbers and vertical_numbers:
        product = max(horizontal_numbers) * max(vertical_numbers)
        processed_asterisks.add((x, y))
        return product

    return None

lines_list = []
with open('input_files/input_two_test.txt', 'r') as file:
    for line in file:
        lines_list.append(line.strip())

products = []
processed_asterisks = set()
lines = [list(line) for line in lines_list]  # Convert each line to a list of characters

for y in range(len(lines)):
    for x in range(len(lines[y])):
        result = product_around_asterisk(lines, x, y, processed_asterisks)
        if result is not None:
            products.append(result)

total = sum(products)
print(f"Total sum of products: {total}")
