lines_list = []
parts = []

def is_symbol(char):
	if char == '.':
		return False
	elif char.isnumeric():
		return False
	elif not char.isalpha():
		return True 

def is_a_part_number(start_x, end_x, line):
	start_range = start_x - 1
	if (start_x <= 0):
		start_range = 0
	end_range = end_x + 1
	if (end_x >= max_x):
		end_range = end_x
	if is_symbol(lines_list[line][start_range]):
		return True 
	if is_symbol(lines_list[line][end_range]):
		return True

	if (y_idx > 0):
		for char in lines_list[line - 1][start_range:end_range + 1]:
			if is_symbol(char):
				return True

	if (y_idx < max_y ):
		for char in lines_list[line + 1][start_range:end_range + 1]:
			if is_symbol(char):
				return True

	print("exiting is_a_part_number")
	return False 

def append_part(start_x, end_x, part):
	if (is_a_part_number(start_x, end_x, y_idx)):
		parts.append(part)
	
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
			
total = 0
print(parts)
for part in parts:
	total += int(part)
print(total)