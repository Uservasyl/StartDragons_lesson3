import random
lst = random.sample(range(1, 100), 20)
print(lst)

j = 0
k = 1
while j < len(lst) -1:
    if lst[j] < lst[k] and j % 2 == 0:
        lst[j], lst[k] = lst[k], lst[j]
    j += 1
    k += 1
print(lst)