import random
arr = random.sample(range(1, 100), 11)
print(arr)

sub_list_size = 1
list_size = len(arr)
while sub_list_size < list_size:
    l = 0
    while l < list_size - 1:
        m = min(l + sub_list_size - 1, list_size - 1)
        r = min(l + 2 * sub_list_size - 1, list_size - 1)
        n1 = m - l + 1
        n2 = r - m 
        L = [0] * (n1) 
        R = [0] * (n2) 

        for i in range(0 , n1): 
            L[i] = arr[l + i] 
        for j in range(0 , n2): 
            R[j] = arr[m + 1 + j]
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2 : 
            if L[i] >= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1
        while j < n2: 
            arr[k] = R[j] 
            j += 1
            k += 1
        l = l + sub_list_size * 2
    sub_list_size = sub_list_size * 2
print(arr)