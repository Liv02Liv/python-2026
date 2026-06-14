#%%
n = int(input())

count = 0 
temp = n 

while temp > 0:
    if temp % 10 != 0:
        count += 1
    temp //= 10

print(count)