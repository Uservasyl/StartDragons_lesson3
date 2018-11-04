number = int(input("Введіть довжину списку: \n"))
i = 1
j = 1
k = 1
arr = []

while j <= number or k <= number:
    if i % 2 == 0 and j % 3 == 0:
        arr.append(j)
        i += 1
    elif i % 2 == 1 and k % 7 == 0:
        arr.append(k)
        i += 1
    k += 1
    j += 1
print(arr)
