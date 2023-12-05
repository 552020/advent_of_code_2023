lines = []
cards = []
numbers = []

total = 0
scratchcards = 0
cards_nbr = 0

def init():
	cards_tmp = []
	numbers_tmp = []
	with open('input_files/input_two_test.txt', 'r') as file:
		for line in file:
			lines.append(line)

	for line in lines:
		buffer = line.split(':')[1]
		card = buffer.split('|')[0].strip()
		cards_tmp.append(card)
		number = buffer.split('|')[1].strip()
		numbers_tmp.append(number)
	for card in cards_tmp:
		card_int = {int(nbr) for nbr in card.split()}
		cards.append(card_int)
	for number in numbers_tmp:
		number_int = {int(nbr) for nbr in number.split()}
		numbers.append(number_int)

init()

def scratchcardcounter(cards, numbers):
	""" It returns the numbers of of scratchcards
		It takes two lists, the list of cards (the scratchcards), and the list of numbers.
		Both are lists of sets.
	"""
	cards_nbr = len(cards)
	print(cards)
	print(numbers)
	print("cards in the call: ", cards_nbr)
	for idx, item in enumerate(cards):
		intersection = []
		intersection = cards[idx] & numbers[idx]
		members = len(intersection)
		if members > 1:
			print("members: ", members)
			print("idx:", idx)
			start = idx + 1
			end = start + members 
			if len(intersection) + 1 > len(cards):
				print("this case")
				end = len(cards) + 1
			if len(cards) >= 2:
				print("start:end", start, end)
				print(cards[start:end])
				print("before recursion")
				cards_nbr += scratchcardcounter(cards[start:end], numbers[start:end])
		elif members == 1:
			cards_nbr += 1
	print("before return: ", cards_nbr)
	return cards_nbr 

total = scratchcardcounter(cards, numbers)
print(total)

