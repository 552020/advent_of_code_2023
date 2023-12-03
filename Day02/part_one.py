lines_dict = {}

with open('input_files/input_one.txt', 'r') as file:
	for idx, line in enumerate(file, start=1):
		# print(idx, line)
		parts = line.split(':', 1)
		game_nbr = None
		for el in parts[0].split():
			if el.isdigit():
				game_nbr = int(el)
				break
		if game_nbr is not None and len(parts) > 1:
			cleaned_str = parts[1].replace(',', '').replace(';', '').strip()
			lines_dict[game_nbr] = cleaned_str
		else:
			lines_dict[idx] = ''

total = 0

for game_id, string in lines_dict.items():
	print("game id:", game_id)
	print("string:", string)
	# print(game_id, string)
	# string.split() return a list
	parts = string.split()
	flag = 0
	for idx, part in enumerate(parts):
		# print(idx)
		# print(part)
		if part.isdigit() and int(part) > 14:
			flag = 1
			break
		if part.isdigit() and int(part) > 13:
			# trying to access an idx outside the range woudl throw an IndexError!
			if (parts[idx + 1] != 'blue' and parts[idx + 1] != 'red'):
				flag = 1
				break
		if part.isdigit() and int(part) > 12:
			# print("break > 12 and red")
			if parts[idx + 1] == 'red':
				flag = 1
				break
	if flag == 0:
		print(game_id, string)
		total += game_id

print(total)
