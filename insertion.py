def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            yield arr.copy()  # Yield a copy of the array after each shift
        arr[j+1] = key
        yield arr.copy()  # Yield a copy of the array after each insertion