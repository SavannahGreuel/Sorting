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
    print("Element is not present in array") #should be at index 6
else: 
    print("Element is present at index", result)



# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  l = 0
  r = len(arr)-1
 
  while l <= r:
    mid = int(l + (r - 1)/2)

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      l = mid + 1
    else:
      r = mid - 1

  


arr = [ 2, 3, 4, 10, 40 ] 
target = 10 # should be index 3
result = binary_search(arr,target)

if result != -1:
  print (f'Element is present at index {result}')
else:
  print('Element is not present in this array')

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
