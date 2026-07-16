#%%
# MODO JUNIOR 
nums = [10, 20, 20, 30, 40, 30, 50]
unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
unique_nums.sort()
print(unique_nums)

#%%
# MODO SENIOR
nums = [10, 20, 20, 30, 40, 30, 50]
print(sorted(set(nums)))