import re
from collections import Counter
from pathlib import Path

data_raw = Path(__file__).with_name("./input_one.txt").read_text().splitlines()

# Transform and sort hands
transformed_hands = sorted(
    (
        (
            max(Counter(hand).values()) - len(set(hand)),
            *map("23456789TJQKA".index, hand),
            int(str_bid),
            hand,  # Include original hand for printing
        )
        for hand, str_bid in map(str.split, data_raw)
    )
)

# Enumerate over sorted list to assign ranks and print
for rank, (hand_type, *_, bid, hand) in enumerate(transformed_hands, start=1):
    print(f"Hand: {hand}, Rank: {rank}, Bid: {bid}")

# Calculate total winnings
total_winnings = sum(
    (rank) * bid for rank, (_, *_, bid, _) in enumerate(transformed_hands, start=1)
)

print("Total winnings:", total_winnings)
