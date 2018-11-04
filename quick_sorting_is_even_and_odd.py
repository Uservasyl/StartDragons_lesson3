import random
arr = random.sample(range(1, 100), 10)
print(arr)

l = 0
r = len(arr)-1
stack = []
stack.append(l)
stack.append(r)
while len(stack) > 0:
    r = stack[-1]
    stack.remove(r)
    l = stack[-1]
    stack.remove(l)
    i = l -1
    splitter = arr[r]
    j = l
    while j < r:
        if arr[j] % 2 == 0:
            if splitter % 2 == 0 and splitter < arr[j]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            elif splitter % 2 == 1:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        elif arr[j] % 2 == 1:
            if splitter % 2 == 1 and arr[j] < splitter:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            elif splitter % 2 == 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1], arr[r] = arr[r], arr[i+1]
    s = i + 1
    if s-1 > l:
        stack.append(l)
        stack.append(s-1)
    if s+1 < r:
        stack.append(s+1)
        stack.append(r)
print(arr)