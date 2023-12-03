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
	print("hello from is_a_part_number")
	print("start_x:", start_x)
	print("end_x:", end_x)
	print("max_y: ", max_y)
	print("max_x: ", max_x)
	print(lines_list)
	# Set up start_range and end_range
	start_range = start_x - 1
	if (start_x <= 0):
		start_range = 0
	end_range = end_x + 1
	if (end_x >= max_x):
		end_range = end_x
	print("max_x", max_x)
	print("start_range: ", start_range)
	print("end_range: ", end_range)

	# Check the actual line
	if is_symbol(lines_list[line][start_range]):
		# return False
		return True 
	if is_symbol(lines_list[line][end_range]):
		# return False
		return True

	# Check the previous line
	if (y_idx > 0):
		for char in lines_list[line - 1][start_range:end_range + 1]:
			if is_symbol(char):
				# return False
				return True

	# Check the next line
	print('Check the next line')
	print("y_idx:", y_idx, "max_y: ", max_y)
	print("start_range, endrange:", start_range, end_range)
	if (y_idx < max_y ):
		print(y_idx)
		print(max_y)
		for char in lines_list[line + 1][start_range:end_range + 1]:
			if is_symbol(char):
				# return False
				return True

	print("exiting is_a_part_number")
	# return True
	return False 

def append_part(start_x, end_x, part):
	print("start_x, end_x:", start_x,",", end_x)
	if (is_a_part_number(start_x, end_x, y_idx)):
		print("This part gets appended:", part)				
		parts.append(part)
	
with open('input_files/input_one_test_two.txt', 'r') as file:
	for idx, line in enumerate(file):
		line_list = []
		# print(idx)
		# print(line)
		# print(idx, line)
		for letter in line:
			line_list.append(letter)
		# print("line_list:")
		# print(line_list)
		lines_list.append(line_list)
	# print(lines_list)

start_x = -1
max_x = len(line) - 1
end_x = -1
max_y = len(lines_list) - 1

for y_idx,line in enumerate(lines_list):
	# print(line)
	print(y_idx)
	print("print line: ", line)
	print("print same line: ", lines_list[y_idx])
	if (y_idx > 0):
		print("print previous line: ", lines_list[y_idx - 1])
	part = ''
	for idx, char in enumerate(line):
		#  print(char)
		#  print(idx)
		if char.isdigit():
			if (start_x == -1):
				start_x = idx
			# part = ''.join([part, char])
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

				# Perform the check before appending
			
total = 0
print('parts:')
print(parts)
for part in parts:
	total += int(part)
print(total)

