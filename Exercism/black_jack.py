#%%

#(Black Jack)

def value_of_card(card):
    if card == "A":
        return 1
    elif card in ["J", "Q", "K"]:
        return 10
    else:
        return int(card)

print(value_of_card("K"))
print(value_of_card("4"))
print(value_of_card("A"))

def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two
        
print(higher_card("K", "10"))
print(higher_card("4", "6"))
print(higher_card("K", "A"))

def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1
        
print(value_of_ace("6", "K"))
print(value_of_ace("7", "3"))

def is_blackjack(card_one, card_two):
    if card_one == "A" and card_two in ["10", "J", "Q", "K"]:
        return True
    elif card_two == "A" and card_one in ["10", "J", "Q", "K"]:
        return True
    else:
        return False

print(is_blackjack("A", "K"))
print(is_blackjack("10", "9"))

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

print(can_split_pairs("Q", "K"))
print(can_split_pairs("10", "A"))

def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]

print(can_double_down("A", "9"))
print(can_double_down("10", "2"))