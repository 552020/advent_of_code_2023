lines = []
cards = []
numbers = []

total = 0

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
	scratchcards = len(cards)
	for idx, item in enumerate(cards):
		intersection = cards[idx] & numbers[idx]
		members = len(intersection)
		if members > 0:
			start = idx + 1
			end = start + members + 1
			#if len(intersection) > len(cards):
				#end = start + len(cards) 
			if len(cards) >= 2:
				scratchcards += scratchcardcounter(cards[start:end], numbers[start:end])
	return scratchcards

total = scratchcardcounter(cards, numbers)
print(total)

