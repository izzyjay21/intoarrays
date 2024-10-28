from array import *

arr = array("i", [2,3,4,5,8,9,5,45,23,67,4,34,98])

def minimum(array,size):
    temp = array[0]
    for i in range(size):
       temp = min(temp,array[i]) 
    return temp


def maximum(array,size):
    temp = array[0]
    for i in range(size):
        temp = max(temp, array[i])
    return temp    

print(minimum(arr,len(arr)))
print(maximum(arr,len(arr)))