# Python program for implementation of Bubble Sort
#Copyright: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# Angela Davey-Nightingale 2100.....

import random
import time
startTime = time.time()

def sortBubble(arr):
 n = len(arr)

 swapped = False

 for i in range(n-1):

  for j in range(0, n-i-1):


   if arr[j] > arr[j + 1]:
    swapped = True
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
  if not swapped:
   return

arr = [69, 420, 10, 19, 2003, 63, 56]

for i in range (len(arr)):
    arr[i] = random.randint(3, 90)

sortBubble(arr)

print("Sorted array is:")
for i in range(len(arr)):
 print("% d" % arr[i], end=" ")

endTime = time.time()
elapsedTime = endTime - startTime
print('Time elapsed: ', elapsedTime, 'seconds')
