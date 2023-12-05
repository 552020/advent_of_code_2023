def count_matches(card_numbers, winning_numbers):
    return sum(num in winning_numbers for num in card_numbers)

def process_scratchcards(cards):
    total_cards = len(cards)
    queue = [(i, card) for i, card in enumerate(cards)] 
    while queue:
        index, card = queue.pop(0)
        card_numbers, winning_numbers = card.split('|')
        card_numbers = set(map(int, card_numbers.split()))
        winning_numbers = set(map(int, winning_numbers.split()))
        matches = count_matches(card_numbers, winning_numbers)
        for _ in range(matches):
            if index + 1 < len(cards): 
                total_cards += 1
                queue.append((index + 1, cards[index + 1]))
                index += 1
    return total_cards

def read_scratchcards_from_file(file_path):
    scratchcards = []
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                scratchcard_data = line.split(':', 1)[1].strip()
                scratchcards.append(scratchcard_data)
    return scratchcards

file_path = './input_files/input_one_test.txt'
scratchcards = read_scratchcards_from_file(file_path)
total_scratchcards = process_scratchcards(scratchcards)
print(total_scratchcards)