def main_bubble_sort(arr, array):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
        array[i], array[j] = array[j], array[i]
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
