#%%

a = 12
b = 15

if a < b:
    if a == b:
        print(a + b)
    else:
        print(a - b)

#%%

a = 5
b = 8

if a > b:
    m = a
else:
    m = b
print(m)

#%%

s = 1

for i in range(1, 5):
    s*=i 
print(s)

#%%

x = 4
y = 9

if x + y > 10:
    if y - x > 3:
        print(1)
    else:
        print(2)
else:
    print(3)