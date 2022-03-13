array=[-2,1,3,6,-8,2,-5,-7,3,5,-1]

# start or end item of maximum subarray
def find_item(arr):
  maxSum=arr[0]
  curSum = maxSum
  curItem = 0
  maxItem = curItem 
  for i in range(1, len(arr)):
    curSum=max(curSum+arr[i], arr[i])
    if curSum == arr[i]:
      curItem =i
    if maxSum != max(maxSum,curSum):
      maxItem = i
      
    maxSum=max(maxSum, curSum)

  Item = min(curItem, maxItem) # Item is start  or end of max_subarray 
  return Item

def find_max(arr):
  maxSum=arr[0]
  curSum = maxSum
  for i in range(1, len(arr)):
    curSum=max(curSum+arr[i], arr[i])
    maxSum=max(maxSum, curSum)
  return maxSum

Item = find_item(array)
Max = find_max(array)

arr1 = array[:Item+1]
arr2 = array[Item:]

Max_1 = find_max(arr1)
Max_2 = find_max(arr2)

if Max == Max_1:
  # The item is end and calculate start itme
  end = Item
  # add code ...
else: # Max == Max_2
  start = Item
  # The item is start and calcualte end item
  # add code ...


## add print
# code ...


