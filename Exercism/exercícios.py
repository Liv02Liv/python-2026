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