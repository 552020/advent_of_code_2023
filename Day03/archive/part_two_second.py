def is_digit(char):
    return char.isdigit()

def product_around_asterisk(lines, x, y, processed_asterisks):
    if (x, y) in processed_asterisks:
        return None

    product = None
    if lines[y][x] == '*':
        print(lines[y][x])
        neighbors = []
        if x > 0 and is_digit(lines[y][x-1]):
            neighbors.append(int(lines[y][x-1]))
        if x < len(lines[y]) - 1 and is_digit(lines[y][x+1]):
            neighbors.append(int(lines[y][x+1]))
        if y > 0 and is_digit(lines[y-1][x]):
            neighbors.append(int(lines[y-1][x]))
        if y < len(lines) - 1 and is_digit(lines[y+1][x]):
            neighbors.append(int(lines[y+1][x]))

        if len(neighbors) == 2:
            product = neighbors[0] * neighbors[1]
            processed_asterisks.add((x, y))

    return product

print('hello')
lines_list = []
with open('input_files/input_two_test.txt', 'r') as file:
    for line in file:
        lines_list.append(line.strip())

print(lines_list)
products = []
processed_asterisks = set()
for y in range(len(lines_list)):
    for x in range(len(lines_list[y])):
        result = product_around_asterisk(lines_list, x, y, processed_asterisks)
        if result is not None:
            products.append(result)

total = sum(products)
print(total)
