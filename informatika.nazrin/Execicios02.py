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


#%%

cart = ("Shoes", "Bag", "Watch")
a, b, c = cart 
print(b)

#%%

fruits = ["apple", "banana"]
res = []

for f in fruits:
    res.append(f[:2])
print("-".join(res))


#%%

meals = ["Maggi", "Pizza", "Sandwich"]

for x in meals:
    meals.remove(x)

print(meals)


#%%

team = "Barcelona"

if "barca" in team.lower():
    print(team[:5])
else:
    print(team[3:])


#%% 

a =7
b = 3
c = 12

if a > 5:
    if b > 5:
        print("P")
    elif c > 10:
        if a + b > c:
            print("S")
        else:
            print("T")
    else:
        print("F")
elif c > a:
    print("U")
else:
    print("P")