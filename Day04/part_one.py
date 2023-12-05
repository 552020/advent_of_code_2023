lines = []
cards = []
numbers = []


with open('input_files/input_one_test.txt', 'r') as file:
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
	tmp.append(card_int)
cards = tmp
for number in numbers:
	number_int = {int(nbr) for nbr in number.split()}
	tmp.append(number_int)
numbers = tmp
print("cards:", cards)
print("tmp:", tmp)
print("numbers", numbers)

for idx, item in enumerate(cards):
	intersection = cards[idx] & numbers[idx]
	members = len(intersection)
