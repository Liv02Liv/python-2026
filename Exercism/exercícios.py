#exercícios de Python no Exercism.

#%%

#(Olá, mundo!)

def hello():
    return "Hello, World!"
print(hello())

#%%

#(Guido's Gorgeous Lasagna)

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Return the remaining baking time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
print(bake_time_remaining(30))

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes."""
    return number_of_layers * 2 
print(preparation_time_in_minutes(3))

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the total elapsed cooking time in minutes."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
print(elapsed_time_in_minutes(3, 20))

#%%

a = 1

while a <= 10:
    a = a + a
print(a)

#%%

#(Ghost Gobble Arcade Game)

"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

print(eat_ghost(False, True))

def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot

print(score(True, True))

def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost

print(lose(False, True))

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return  has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

print(win(False, True, False))

#%%

def soma(a, b, c):
    return a + b + c

print(soma(2, 2, 2))
print(soma(3, 3, 3))

#%%
nome = str(input("Digite seu nome: "))

def boasvindas(nome):
    return f"Seja-Bem-Vinda, {nome}!"

print(boasvindas(nome))

#%%

#(Currency Exchange)

"""Functions for calculating steps in exchanging currency."""

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

print(exchange_money(100, 5))

def get_change(budget, exchanging_value):
    return budget - exchanging_value

print(get_change(100, 5))

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

print(get_value_of_bills(5, 100))

def get_number_of_bills(amount, denomination):
    return amount // denomination

print(get_number_of_bills(100, 5))

def get_leftover_of_bills(amount, denomination):
    return amount % denomination

print(get_leftover_of_bills(95, 2))

def exchangeable_value(budget, exchange_rate, spread, denomination):
    taxa_real = exchange_rate * (1 + spread / 100)
    valor_convertido = budget / taxa_real
    return int((valor_convertido // denomination) * denomination)

print(exchangeable_value(100, 1.20, 10, 20))

#%%

#(Meltdown Mitigation)

"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    return (
        temperature < 800 
        and neutrons_emitted > 500 
        and temperature * neutrons_emitted < 500000
    )

print(is_criticality_balanced(750, 600))

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    eficiecia = (generated_power/theoretical_max_power) * 100
    if eficiecia >=  80:
        return "green"
    if eficiecia >= 60:
        return "orange"
    if eficiecia >= 30:
        return "red"
    
    return "black"
    
print(reactor_efficiency(200, 50, 15000))

def fail_safe(temperature, neutrons_produced_per_second, threshold): 
    valor = temperature * neutrons_produced_per_second 
    
    if valor < threshold * 0.9: 
        return "LOW" 
    if valor <= threshold * 1.1: 
        return "NORMAL" 
     
    return "DANGER" 
        
print(fail_safe(1000, 30, 5000))

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