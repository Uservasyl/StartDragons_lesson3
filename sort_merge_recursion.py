import random
 
 
def merge_sort(arr):
    if len(arr) > 1:
        center = len(arr) // 2
        left = arr[:center]
        right = arr[center:]

        merge_sort(left)
        merge_sort(right)
 
        i, j, k = 0, 0, 0
 
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = random.sample(range(1, 100), 11)
print(arr)
merge_sort(arr)
print(arr)
