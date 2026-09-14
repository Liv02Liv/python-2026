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