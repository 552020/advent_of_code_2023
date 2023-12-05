lines = []
cards = []
numbers = []
cards_int = []
numbers_int = []


with open('input_files/input_one.txt', 'r') as file:
	for line in file:
		lines.append(line)
for line in lines:
	print(line)
print(lines)
for line in lines:
	buffer = line.split(':')[1]
	card = buffer.split('|')[0].strip()
	cards.append(card)
	number = buffer.split('|')[1].strip()
	numbers.append(number)
print("cards:", cards)
print("numbers: ", numbers)
tmp = []
for card in cards:
	card_int = {int(nbr) for nbr in card.split()}
	cards_int.append(card_int)
for number in numbers:
	number_int = {int(nbr) for nbr in number.split()}
	numbers_int.append(number_int)
print("cards:", cards)
print("cards_int:", cards_int)
print("numbers", numbers)
print("numbers_int", numbers_int)

partial = 0
total = 0
for idx, item in enumerate(cards):
	intersection = cards_int[idx] & numbers_int[idx]
	partial = 0
	members = len(intersection)
	if members > 0:
		partial = 1
		for _ in range(1, members):
			partial = partial * 2

	print('partial: ', partial)

	total += partial

print("total:", total)

