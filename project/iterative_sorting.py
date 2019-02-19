# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc) 
             
        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr

my_arr = [2,5,9,7,4,1,3,8,6]
print(my_arr)
arr = selection_sort(my_arr)
print(my_arr)

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    # traverses 1 through length of array
    for i in range(1,len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        x = i-1
        while x >=0 and key < arr[x]:
           arr[x+1] = arr[x]
           x -= 1
        arr[x+1] = key

    return arr

arr = [54,26,93,17,77,31,44,55,20]

result = insertion_sort(arr)
print(f'{result}')


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90] 
result = bubble_sort(arr)

print (f'Your sorted array is {result}')


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr