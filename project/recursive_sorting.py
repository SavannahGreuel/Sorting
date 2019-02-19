### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    i = (low -1) # index of smaller element
    pivot = arr[high] # pivot (last element as pivot)

    for j in range( low, high):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot 
            i = i + 1 # increment index of smaller element 
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i + 1)


def run_quick_sort ( arr, low, high ):
    if low < high :
        qs = quick_sort(arr,low,high)

        run_quick_sort(arr, low, qs - 1)
        run_quick_sort(arr, qs + 1, high)

        return arr

# arr = [75, 29, 4, 47, 24, 67, 12, 50, 63, 96]
arr = [66, 84, 4, 57, 42, 77, 7, 59, 95, 26]
n = len(arr)

result = run_quick_sort( arr, 0, n - 1)
print (f'{result}')

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
