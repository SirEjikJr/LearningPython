def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

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

global middle_array
middle_array=[]

def middle_value(arr):

    if len(arr)%2==0:
        h=len(arr)//2
        global s
        s = (arr[h-1] + arr[h])//2
        print (s)
        middle_array.append(s)
        #print(middle_array)
    else:
        h = (len(arr)//2)
        s = arr[h]
        print(s)
        middle_array.append(s)
       # print(middle_array)
