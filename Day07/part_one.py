import copy

card_labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_labels_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
hands = []
hand = {"cards": "", "bid": 0, "type": "", "rank": 0, "cards_chars": ""}
types = ["five", "four", "house", "three", "two_pair", "one_pair", "high_card"]
types_nbr = {
    "five": 0,
    "four": 0,
    "house": 0,
    "three": 0,
    "two_pair": 0,
    "one_pair": 0,
    "high_card": 0,
}
hands_five = []
hands_four = []
hands_house = []
hands_three = []
hands_two_pair = []
hands_one_pair = []
hands_high_card = []

all_hands_type = [
    hands_five,
    hands_four,
    hands_house,
    hands_three,
    hands_two_pair,
    hands_one_pair,
    hands_high_card,
]


with open("input_files/input_one_test.txt", "r") as lines:
    for idx, line in enumerate(lines):
        hand_line = line.strip().split()[0]
        bid_line = line.strip().split()[1]
        if idx <= len(hands):
            hands.append(hand.copy())
        hands[idx]["cards"] = hand_line
        hands[idx]["bid"] = int(bid_line)

print(hands)


def define_type(hands, idx, hand):
    hand["cards_chars"] = replace_chars_in_hand(hand, card_labels, card_labels_chars)
    hand_set = set(hand["cards"])
    if len(hand_set) == 1:
        hands[idx]["type"] = "five"
        types_nbr["five"] += 1
    elif len(hand_set) == 2:
        if (
            hand["cards"].count(hand["cards"][0]) == 4
            or hand["cards"].count(hand["cards"][0]) == 1
        ):
            hands[idx]["type"] = "four"
            types_nbr["four"] += 1
        else:
            hands[idx]["type"] = "house"
            types_nbr["house"] += 1
    elif len(hand_set) == 3:
        if (
            hand["cards"].count(hand["cards"][0]) == 3
            or hand["cards"].count(hand["cards"][1]) == 3
            or hand["cards"].count(hand["cards"][2]) == 3
        ):
            hands[idx]["type"] = "three"
            types_nbr["three"] += 1
        else:
            hands[idx]["type"] = "two_pair"
            types_nbr["two_pair"] += 1
    elif len(hand_set) == 4:
        hands[idx]["type"] = "one_pair"
        types_nbr["one_pair"] += 1
    else:
        hands[idx]["type"] = "high_card"
        types_nbr["high_card"] += 1


def define_rank(hands, idx, hand):
    print("hand: ", hand)
    tc5 = types_counter["five"]
    print("tc5: ", tc5)
    tc4 = types_counter["four"]
    print("tc4: ", tc4)
    tch = types_counter["house"]
    print("tch: ", tch)
    tc3 = types_counter["three"]
    print("tc3: ", tc3)
    tc2 = types_counter["two_pair"]
    print("tc2: ", tc2)
    tc1 = types_counter["one_pair"]
    print("tc1: ", tc1)
    tc0 = types_counter["high_card"]
    print("tc0: ", tc0)
    if hand["type"] == "five":
        hands[idx]["rank"] = l_h - (q5 - tc5)
        types_counter["five"] -= 1
    elif hand["type"] == "four":
        hands[idx]["rank"] = l_h - q5 - (q4 - tc4)
        types_counter["four"] -= 1
    elif hand["type"] == "house":
        hands[idx]["rank"] = l_h - q5 - q4 - (qh - tch)
        types_counter["house"] -= 1
    elif hand["type"] == "three":
        print("three")
        print("hand: ", hand)
        print(
            f"l_h: {l_h}, q5: {q5}, q4: {q4}, qh: {qh}, q3: {q3}, q2: {q2}, q1: {q1}, q0: {q0}, tc0: {tc0}"
        )
        print("q3: ", q3)
        print("tc3: ", tc3)
        hands[idx]["rank"] = l_h - q5 - q4 - qh - (q3 - tc3)
        types_counter["three"] -= 1
        print("hands[idx]: ", hands[idx])
    elif hand["type"] == "two_pair":
        hands[idx]["rank"] = l_h - q5 - q4 - qh - q3 - (q2 - tc2)
        types_counter["two_pair"] -= 1
    elif hand["type"] == "one_pair":
        hands[idx]["rank"] = l_h - q5 - q4 - qh - q3 - q2 - (q1 - tc1)
        print(
            f"l_h: {l_h}, q5: {q5}, q4: {q4}, qh: {qh}, q3: {q3}, q2: {q2}, q1: {q1}, q0: {q0}, tc0: {tc0}"
        )

        print("hands[idx]['rank']: ", hands[idx]["rank"])
        print("handes[idx]: ", hands[idx])
        types_counter["one_pair"] -= 1
    else:
        hands[idx]["rank"] = l_h - q5 - q4 - qh - q3 - q2 - q1 - (q0 - tc0)
        types_counter["high_card"] -= 1


def assign_type_list(hands, idx, hand):
    if hand["type"] == "five":
        hands_five.append(hand)
    elif hand["type"] == "four":
        hands_four.append(hand)
    elif hand["type"] == "house":
        hands_house.append(hand)
    elif hand["type"] == "three":
        hands_three.append(hand)
    elif hand["type"] == "two_pair":
        hands_two_pair.append(hand)
    elif hand["type"] == "one_pair":
        hands_one_pair.append(hand)
    else:
        hands_high_card.append(hand)


def replace_chars_in_hand(hand, original_chars, replacement_chars):
    char_map = {
        original: replacement
        for original, replacement in zip(original_chars, replacement_chars)
    }
    return "".join(char_map.get(char, char) for char in hand["cards"])


def sort_hands(hands):
    n = len(hands)
    for i in range(n):
        for j in range(0, n - i - 1):
            if hands[j]["cards_chars"][0] > hands[j + 1]["cards_chars"][0]:
                # Swap the ranks
                hands[j]["rank"], hands[j + 1]["rank"] = (
                    hands[j + 1]["rank"],
                    hands[j]["rank"],
                )


for idx, hand in enumerate(hands):
    define_type(hands, idx, hand)
print(types_nbr)
l_h = len(hands)
q5 = types_nbr["five"]
q4 = types_nbr["four"]
qh = types_nbr["house"]
q3 = types_nbr["three"]
q2 = types_nbr["two_pair"]
q1 = types_nbr["one_pair"]
q0 = types_nbr["high_card"]
types_counter = copy.deepcopy(types_nbr)
for idx, hand in enumerate(hands):
    define_rank(hands, idx, hand)
for idx, hand in enumerate(hands):
    assign_type_list(hands, idx, hand)

# for type in all_hands_type:
for hands_type in all_hands_type:
    sort_hands(hands_type)
total_winnings = 0

print("Calulating total_winnings")
for hands_type in all_hands_type:
    for idx, hand in enumerate(hands_type):
        print("hand: ", hand)
        print("idx: ", idx)
        print("hand['bid']: ", hand["bid"])
        print("hand['rank']: ", hand["rank"])
        print("total_winnings: ", total_winnings)
        total_winnings += hand["bid"] * hand["rank"]
print("total_winnings: ", total_winnings)
