lines_dict = {}

with open('input_files/input_two.txt', 'r') as file:
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

partial = 1
total = 0
min_cubes = {"green": 0, "red": 0, "blue": 0}

for game_id, string in lines_dict.items():
	partial = 1
	min_cubes["green"] = 0
	min_cubes["red"] = 0
	min_cubes["blue"] = 0
	print("game id:", game_id)
	print("string:", string)
	# print(game_id, string)
	# string.split() return a list
	parts = string.split()
	for idx, part in enumerate(parts):
		for key, value in min_cubes.items():
			if part == key:
				cubes_nbr = int(parts[idx - 1])
				if cubes_nbr > min_cubes[key]:
					min_cubes[key] = cubes_nbr
	for value in min_cubes.values():
		partial *= value
	total += partial
	

print(total)
