FIVE_A_KIND = "five-a-kind"
FOUR_A_KIND = "four-a-kind"
FULL_HOUSE = "full-house"
THREE_A_KIND = "three-a-kind"
TWO_PAIR = "two-pair"
ONE_PAIR = "one-pair"
HIGH_CARD = "high-card"
file_path = 'input.txt'
sum=0
winning_groups={}
final_list=[]
points_list=[HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_A_KIND, FULL_HOUSE, FOUR_A_KIND, FIVE_A_KIND]
conversion_table= {
    HIGH_CARD: {
        1: ONE_PAIR
    },
    ONE_PAIR: {
        1: THREE_A_KIND,
        2: THREE_A_KIND
    },
    TWO_PAIR: {
        1: FULL_HOUSE,
        2: FOUR_A_KIND
    },
    THREE_A_KIND: {
        1: FOUR_A_KIND,
        2: FIVE_A_KIND,
        3: FOUR_A_KIND
    },
    FULL_HOUSE: {
        2: FIVE_A_KIND,
        3: FIVE_A_KIND
    },
    FOUR_A_KIND: {
        1: FIVE_A_KIND,
        4: FIVE_A_KIND
    },
    FIVE_A_KIND: {
        5: FIVE_A_KIND
    }

}
def card_comparator(x):
    translation_table = str.maketrans("TJQKA", "B1DEF")
    return x[0].translate(translation_table)
def count_occurrences(hand):
    char_count = {}

    for char in hand:
        char_count[char] = int(char_count.get(char, 0) + 1)

    values = list(char_count.values())
    if values.count(1) == 5:
        return HIGH_CARD
    elif values.count(2) == 1 and values.count(1) == 3:
        return ONE_PAIR
    elif values.count(2) == 2:
        return TWO_PAIR
    elif values.count(3) == 1 and values.count(2) == 0:
        return THREE_A_KIND
    elif values.count(3) == 1 and values.count(2) == 1:
        return FULL_HOUSE
    elif values.count(4) == 1:
        return FOUR_A_KIND
    elif values.count(5) == 1:
        return FIVE_A_KIND


def check_jollies(point, hand):
    jolly_occurences = hand.count('J')
    if jolly_occurences == 0:
        return point
    else:
     return conversion_table[point][jolly_occurences]


with open(file_path, 'r') as file:
    for line in file:
        hand, bid = line.split()
        point = count_occurrences(hand)
        point = check_jollies(point, hand)
        winning_groups[point] = winning_groups.get(point, [])
        winning_groups[point].append((hand, bid))

    for point, tuple in winning_groups.items():
        winning_groups[point] = sorted(tuple, key=card_comparator)

    for p in points_list:
        final_list.append(winning_groups.get(p, []))

    rank = 1
    for item in final_list:
        for winning in item:
            sum += int(winning[1]) * rank
            rank += 1
print(sum)





