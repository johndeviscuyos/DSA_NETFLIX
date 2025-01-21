def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr.copy()

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr.copy()
    yield i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Get the partition generator
        partition_gen = partition(arr, low, high)

        # Process all intermediate states from partition
        pivot_index = None
        for state in partition_gen:
            if isinstance(state, int):
                pivot_index = state  # This is our pivot index
            else:
                yield state  # This is an array state to visualize

        # Now use the pivot index for recursive calls
        if pivot_index is not None:
            yield from quick_sort(arr, low, pivot_index - 1)
            yield from quick_sort(arr, pivot_index + 1, high)

    yield arr.copy()