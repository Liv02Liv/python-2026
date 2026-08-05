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