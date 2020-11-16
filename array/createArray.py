from array import *

arr1 = array('i', [1,2,3,4,5,6])

print(arr1)

# O(n) insertion 
# arr1.insert(6, 7)
# print(arr1)


# def traverseArray(array):
#     # for i in array:    # O(n)
#         print(i)         # O(1)

# traverseArray(arr1)


# O(1)
# def accessElement(array, index):
#     if index >= len(array):                           # O(1)
#         print("There is no element in the index")     # O(1)
#     else:
#         print(array[index])                           # O(1)

# accessElement(arr1, 1) # 2

# Time: O(n) Space O(1)
# def searchInArray(array, value):
#     for i in array:                                     # O(n)
#         if i == value:                                  # O(1)
#             return array.index(value)                   # O(1)
#     return "The element doe not exist in this array"    # O(1)

# print(searchInArray(arr1, 6))

