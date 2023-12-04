def is_digit(char):
    return char.isdigit()

def product_around_asterisk(lines, x, y, processed_asterisks):
    if (x, y) in processed_asterisks:
        return None

    product = None
    if lines[y][x] == '*':
        print(f"Processing asterisk at ({x}, {y})")
        neighbors = []
        # Check left
        if x > 0 and is_digit(lines[y][x-1]):
            neighbors.append(int(lines[y][x-1]))
            print(f"Found left neighbor: {lines[y][x-1]}")
        # Check right
        if x < len(lines[y]) - 1 and is_digit(lines[y][x+1]):
            neighbors.append(int(lines[y][x+1]))
            print(f"Found right neighbor: {lines[y][x+1]}")
        # Check above
        if y > 0 and is_digit(lines[y-1][x]):
            neighbors.append(int(lines[y-1][x]))
            print(f"Found upper neighbor: {lines[y-1][x]}")
        # Check below
        if y < len(lines) - 1 and is_digit(lines[y+1][x]):
            neighbors.append(int(lines[y+1][x]))
            print(f"Found lower neighbor: {lines[y+1][x]}")

        if len(neighbors) == 2:
            product = neighbors[0] * neighbors[1]
            processed_asterisks.add((x, y))
            print(f"Product of neighbors: {product}")

    return product

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
