def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                yield arr.copy()  # Yield a copy of the array after each swap
        if swapped == False:
            break
    yield arr.copy()  # Yield the final sorted array