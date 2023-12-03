def is_symbol(char):
	if char == '.':
		return False
	elif char.isnumeric():
		return False
	elif not char.isalpha():
		return True 

word = "467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664.598.."

for char in word:
	if is_symbol(char):
		print(char)