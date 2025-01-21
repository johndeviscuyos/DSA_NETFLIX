def merge_sort(arr):
    if len(arr) <= 1:
        yield arr.copy()
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Show the division
    yield arr.copy()

    # Sort left half
    left_sorter = merge_sort(left_half)
    for step in left_sorter:
        arr[:mid] = step
        yield arr.copy()

    # Sort right half
    right_sorter = merge_sort(right_half)
    for step in right_sorter:
        arr[mid:] = step
        yield arr.copy()

    # Merge process
    temp_arr = arr.copy()
    i = 0  # Index for left half
    j = mid  # Index for right half
    k = 0  # Index for merged array

    while i < mid and j < len(arr):
        if temp_arr[i] <= temp_arr[j]:
            arr[k] = temp_arr[i]
            i += 1
        else:
            arr[k] = temp_arr[j]
            j += 1
        k += 1
        yield arr.copy()

    # Copy remaining elements
    while i < mid:
        arr[k] = temp_arr[i]
        i += 1
        k += 1
        yield arr.copy()

    while j < len(arr):
        arr[k] = temp_arr[j]
        j += 1
        k += 1
        yield arr.copy()

    yield arr.copy()
