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