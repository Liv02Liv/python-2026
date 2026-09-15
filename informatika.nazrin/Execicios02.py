#%%

score = 85

if score > 90:
    print("Lionel Messi")

elif score > 75 and score < 90:
    print("Cristiano Ronaldo")

elif score == 100:
    print("Neymar")

else:
    print("Kylian Mbappé")


#%%

x = [1, 2, 3]
y = [4, 5, 6]
x = y

y.append(7)
x[0] = 10
print(x)
print(y)

#%%

home = "Barcelona"
away = "Real Madrid"

if len(home) > len(away):
    print("Camp Nou")

elif len(away) > len(home):
    print("Bernabeu")

else:
    print("El Classico")