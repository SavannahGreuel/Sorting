# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  
# Linearly search x in arr[] 
# If x is present then return its location 
# else return -1 
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
target = 110

print(arr)
result = linear_search(arr,target)
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result); 



# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
