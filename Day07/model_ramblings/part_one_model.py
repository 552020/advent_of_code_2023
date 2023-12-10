def rank_hand(hand):
    """
    Rank the hand based on Camel Cards rules.
    """
    card_order = "AKQJT98765432"
    card_values = {card: index for index, card in enumerate(card_order, start=1)}
    cards = sorted(hand[:-1], key=lambda x: card_values[x], reverse=True)
    counts = {card: cards.count(card) for card in set(cards)}

    if len(set(counts.values())) == 1:
        return (8, [card_values[cards[0]]])
    if 4 in counts.values():
        return (
            7,
            sorted(
                [card_values[card] for card, count in counts.items() if count == 4],
                reverse=True,
            ),
        )
    if 3 in counts.values() and 2 in counts.values():
        return (
            6,
            sorted(
                [card_values[card] for card, count in counts.items() if count == 3],
                reverse=True,
            ),
        )
    if 3 in counts.values():
        return (
            5,
            sorted(
                [card_values[card] for card, count in counts.items() if count == 3],
                reverse=True,
            ),
        )
    if list(counts.values()).count(2) == 2:
        return (
            4,
            sorted(
                [card_values[card] for card, count in counts.items() if count == 2],
                reverse=True,
            ),
        )
    if 2 in counts.values():
        return (
            3,
            sorted(
                [card_values[card] for card, count in counts.items() if count == 2],
                reverse=True,
            ),
        )
    return (2, sorted([card_values[c] for c in cards], reverse=True))


def calculate_winnings(file_path):
    # Read the file and process each hand
    with open(file_path, "r") as file:
        lines = file.readlines()
        hands = [(line.split()[0], int(line.split()[1])) for line in lines]

    # Rank each hand and sort
    ranked_hands = sorted(
        [(hand, bid, rank_hand(hand)) for hand, bid in hands],
        key=lambda x: x[2],
        reverse=True,
    )

    # Calculate total winnings
    total_winnings = sum(
        bid * (rank + 1) for rank, (hand, bid, _) in enumerate(ranked_hands)
    )

    return total_winnings


# Define the file path
file_path = "../input_files/input_one_test.txt"

# Calculate the total winnings (when run in an appropriate environment)
total_winnings = calculate_winnings(file_path)
print("Total winnings:", total_winnings)
