lines_list = []
parts = []
gears = []

def is_symbol(char):
	if char == '.':
		return False
	elif char.isnumeric():
		return False
	elif not char.isalpha():
		return True 

def has_gear(char, line, idx):
	print("has_gear")
	print("char: ", char)
	print("line: ", line)
	print(lines_list[line])
	joined = "".join(lines_list[line])
	print(joined)
	print("idx: ", idx)
	counter = 0
	if (char != "*"):
		return False
	start_range = idx - 1
	if (idx == 0):
		start_range = 0
	end_range = idx + 2
	if (idx == max_x):
		end_range = idx + 1
	if (idx >= 1):
		if lines_list[line][idx - 1].isnumeric():
			print("first counter")
			counter += 1
	if (idx <= max_x - 1):
		if lines_list[line][idx + 1].isnumeric():
			print("second counter")
			counter += 1
	if (line > 0):
		print("line", line)
		print("after line > 0")
		print(lines_list[line - 1])
		joined = "".join(lines_list[line - 1])
		print(joined)
		print("len line: ", len(lines_list[line - 1]))
		print("start_range", start_range)
		print("end_range: ", end_range)
		for char in lines_list[line - 1][start_range:end_range]:
			print("third counter for loop")
			print(char)
			if char.isnumeric():
				print("third counter")
				counter += 1
				break
	if (line < max_y):
		for char in lines_list[line + 1][start_range:end_range]:
			if char.isnumeric():
				print("fourth counter")
				counter += 1
				break
	if counter >= 2:
		print("counter before exiting has_gear", counter)
		return True

gear = ""
def is_a_part_number(start_x, end_x, line):
	print("start_range, end_range")
	print(start_x)
	print(end_x)
	start_range = start_x - 1
	if (start_x <= 0):
		start_range = 0
	end_range = end_x + 1
	if (end_x >= max_x):
		end_range = end_x
	prev_char = lines_list[line][start_range]
	if is_symbol(prev_char):
		if (has_gear(prev_char, line, start_range)):
			gear = int(str(line) + str(start_range))
			gears.append([gear, 0])
			return True 
	next_char = lines_list[line][end_range]
	if is_symbol(next_char):
		if (has_gear(next_char, line, end_range)):
			gear = int(str(line) + str(end_range))
			gears.append([gear, 0])
			return True

	if (y_idx > 0):
		for idx, char in enumerate(lines_list[line - 1][start_range:end_range + 1]):
			if is_symbol(char):
				if (has_gear(char, line - 1, start_range + idx)):
					gear = int(str(line) + str(start_range + idx))
					gears.append([gear, 0])
					return True

	if (y_idx < max_y ):
		for idx, char in enumerate(lines_list[line + 1][start_range:end_range + 1]):
			if is_symbol(char):
				print("has_gear(char,line + 1, idx)", char, line, idx, idx + 1)
				print("".join(lines_list[line + 1]))
				if (has_gear(char, line + 1, start_range + idx)):
					gear = int(str(line) + str(start_range + idx))
					gears.append([gear, 0])
					return True

	print("exiting is_a_part_number")
	return False 

def append_part(start_x, end_x, part):
	if (is_a_part_number(start_x, end_x, y_idx)):
		parts.append(part)
		gears[-1][1] = int(part)
	
with open('input_files/input_two.txt', 'r') as file:
	for idx, line in enumerate(file):
		line_list = []
		for letter in line:
			line_list.append(letter)
		lines_list.append(line_list)

start_x = -1
max_x = len(line) - 1
end_x = -1
max_y = len(lines_list) - 1

for y_idx,line in enumerate(lines_list):
	part = ''
	for idx, char in enumerate(line):
		if char.isdigit():
			if (start_x == -1):
				start_x = idx
			part += char
			print("part:", part)
			if (idx < max_x):
				if not line[idx + 1].isdigit():
					end_x = idx
					append_part(start_x, end_x, part)
					part = ''
					start_x = -1

			elif (idx == max_x):
				end_x = idx
				append_part(start_x, end_x, part)
				part = ''
				start_x = -1

def sum_of_products(list):
	total = 0
	for i in range(0, len(list), 2):
		if i + 1 < len(list):
			product = list[i] * list[i + 1]
			total += product
	return total
total = 0
print(parts)
# for part in parts:
# 	total += int(part)
# parts_int = [int(item) for item in parts]
# print(parts_int)
# total = sum_of_products(parts_int)
print(gears)
print(total)
gears.sort(key=lambda x: x[1])
print(gears)