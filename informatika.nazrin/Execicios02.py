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

#%%

players = ["Ronaldo", "Messi"]

if players[1] == "Ronaldo":
    print("CR7")

elif "Messi" in players:
    print("LM10")

else:
    print("GOAT")


#%%

s = 8
n = 40

while s + n <= 80:
    s = s + 6
    n = n - 3

print(s)

#%%

a = "Hello, World!"
b = a.split(',')
c = b[1][1:]
d = b[0].replace('H', 'J')
e = d + ' ' + c + '!'
i = 0

while i < len(e):
    if e[i] == 'l':
        print('y', end= ' ')
    else:
        print(e[i], end= ' ')
    i = i + 1


#%%

x = [1, 2, 3]
y = x
x.append(4)
y = y + [5]

print(x)
print(y)
print(x is y)
print(x == y)


#%%

x = [1, 2, 3]
y = x
y.append(4)
x = x + [5]
z = y[:2]
y[0] = 10
z.append(6)

print(x)
print(y)
print(z)