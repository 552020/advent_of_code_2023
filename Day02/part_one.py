lines_dict = {}

with open('input_files/input_one_test.txt', 'r') as file:
	for idx, line in enumerate(file, start=1):
		print(idx, line)
		parts = line.split(':', 1)
		if len(parts) > 1:
			lines_dict[idx] = parts[1].strip()
		else:
			lines_dict[idx] = ''

total = 0

for line_nbr, string in lines_dict.items():
	print(line_nbr, string)
	# string.split() return a list
	parts = string.split()
	for idx, part in enumerate(parts):
		if part.isdigit() and int(part) > 15:
			break
		if part.isdigit() and int(part) > 14:
			# trying to access an idx outside the range woudl throw an IndexError!
			if idx + 1 < len(parts) and parts[idx + 1] != 'red':
				break
		if part.isdigit() and int(part) > 13:
			if idx + 1 < len(parts) and parts[idx + 1] != 'red' and parts[idx + 1] != 'green':
				break
	else:
		total += line_nbr

print(total)
