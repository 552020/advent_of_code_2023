
def extract_number(x, y, dx, dy):
	number = ''
	x += dx
	y += dy
	while 0 <= x < len(lines[0]) and 0 <= y < len(lines) and lines[y][x].isdigit():
		number += lines[y][x]
		x += dx
		y += dy
	print(f"Extracted number: {number}")
	return int(number) if number else None
	print(f"Character at ({x}, {y}): {lines[y][x]}")

def product_around_asterisk(lines, x, y, processed_asterisks):
	if lines[y][x] != '*' or (x, y) in processed_asterisks:
		return None

	print(f"Processing asterisk at ({x}, {y})")


number_left = extract_number(x, y, -1, 0)
number_right = extract_number(x, y, 1, 0)
number_above = extract_number(x, y, 0, -1)
number_below = extract_number(x, y, 0, 1)
horizontal_numbers = [n for n in [number_left, number_right] if n is not None]
vertical_numbers = [n for n in [number_above, number_below] if n is not None]

print(f"Numbers around asterisk: left={number_left}, right={number_right}, above={number_above}, below={number_below}")


if horizontal_numbers and vertical_numbers:
	product = max(horizontal_numbers) * max(vertical_numbers)
	processed_asterisks.add((x, y))
	print(f"Product found: {product}")
	return product 

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