lines = []
gears = []

def build_number(y, x):
	# print("build_number")
	# print("y: ", y)
	# print("x: ", x)
	num = ""

	i = x
	# print("lines[y][x]")
	print(lines[y][x])
	while i >= 0 and lines[y][i].isdigit():
		# print("num: ", num)
		num = lines[y][i] + num
		i -= 1
	j = x + 1
	while j < len(lines[y]) and lines[y][j].isdigit():
		# print("num: ", num)
		num += lines[y][j]
		j += 1

	return num

def check_for_number(y, x):
	# print("check_for_number")
	# start_range = x - 1
	# end_range = x + 1
	# if x == 0:
	# 	start_range = 0
	# if x > max_x_idx:
	# 	end_range = x
	start_range = max(0, x - 1)
	end_range = min(max_x_idx, x + 1)
	numbers = []
	product = 0
	if y > 0:
		# print("check line above")
		for idx, char in enumerate(lines[y - 1][start_range:end_range + 1]):
			# print("char: ", char)
			if char.isnumeric():
				# print("char: ", char)
				num = build_number(y - 1, start_range + idx)
				numbers.append(num)
				break
	if y < max_y_idx:
		# print("check line below")
		for idx, char in enumerate(lines[y + 1][start_range:end_range + 1]):
			if char.isnumeric():
				num = build_number(y + 1, start_range + idx)
				numbers.append(num)
				break
	if x > 0 and lines[y][x - 1].isnumeric():
		num = build_number(y, x - 1)
		numbers.append(num)
	if x < max_x_idx and lines[y][x + 1].isnumeric():
		num = build_number(y, x + 1)
		numbers.append(num)
	if len(numbers) == 2:
		product = int(numbers[0]) * int(numbers[1])
		gears.append(product)
		# print("numbers: ", numbers)
		# print("product: ", product)
		# print("gears: ", gears)
		return True

with open('input_files/input_two.txt', 'r') as file:
	for idx, line in enumerate(file):
		line_list = []
		for letter in line:
			line_list.append(letter)
		lines.append(line_list)

start_x = -1
max_x_idx = len(line) - 1
end_x = -1
max_y_idx = len(lines) - 1
total = 0
print("lines")
print(lines)
for y,line in enumerate(lines):
	print("line: ", line)
	for x, char in enumerate(line):
		# print("char: ", char)
		# print("x: ", x)
		# print("y: ", y)
		if char == '*':
			check_for_number(y, x)
total = sum(gears)
print("total: ", total)