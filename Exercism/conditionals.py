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