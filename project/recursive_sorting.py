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
        left = merge_sort(arr[0:int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # L = arr[start:mid]
    # R = arr[mid:end]
    # i = 0
    # j = 0

    # for x in range(start,end):
    #     if j>= len(R) or (i < len(L) and L[i] < R[j]):
    #         arr[x] = L[i]
    #         i = i + 1
    #     else:
    #         arr[x] = R[j]

    return arr
    

def merge_sort_in_place(arr, l, r): 
    pass
    # TO-DO
#     if r-l > 1:
#         mid = int((l+r)/2)
#         merge_sort_in_place(arr, l, mid)
#         merge_sort_in_place(arr, mid, r)
#         merge_in_place(arr,l,mid,r)



# arr1 = [32, 91, 8, 58, 5, 92, 61, 76, 31, 44]
# result = merge_sort_in_place(arr1, 0, len(arr1))
# print(f'{result}')

# TO-DO: implement the Quick Sort function below USING RECURSION
def pivot( arr, low, high ):
    i = (low -1) # index of smaller element
    pivot = arr[high] # pivot (last element as pivot)

    for j in range( low, high):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot 
            i = i + 1 # increment index of smaller element 
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i + 1)


def quick_sort ( arr, low, high ):
    if low < high :
        piv = pivot(arr,low,high)

        quick_sort(arr, low, piv - 1)
        quick_sort(arr, piv + 1, high)

    return arr

# arr = [75, 29, 4, 47, 24, 67, 12, 50, 63, 96]
arr = [66, 84, 4, 57, 42, 77, 7, 59, 95, 26]
n = len(arr) -1


print (quick_sort( arr, 0, n))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
