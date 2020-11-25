import numpy as np

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# insert O(nm) axis=1 for colums and axis=0 for rows
# newTwoDArray = np.insert(twoDArray, 4, [[1,2,3,4]], axis=0 )
# print(newTwoDArray)

# insert using append O(nm) 
# newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0 )
# print(newTwoDArray)

# Accessing an element Time O(1) Space O(1)

# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) and colIndex >= len(array[0]):    # O(1)
#         print('Incorrect index')                                # O(1)
#     else:
#         print(array[rowIndex][colIndex])                        # O(1)


# accessElements(twoDArray, 2, 3)
# Traversing a Two dimensional array Time O(n^2) Space O(1)
# def traverseTDArray(array):
#     for i in range(len(array)):         # O(mn)
#         for j in range(len(array[0])):  # O(n)
#             print(array[i][j])          # O(1)

# traverseTDArray(twoDArray)

# searching fro an element in a two dimensional array time Time O(n^2) Space O(1)
def searchTDArray(array, value):
    for i in range(len(array)):                                         # O(mn )
        print('i', i)
        for j in range(len(array[0])):                                  # O(n)
            print('i', i, 'j', j)
            if array[i][j] == value:                                    # O(1)
                return 'The value is at index '+str(i)+" "+str(j)
    return 'this element is not found'

print(searchTDArray(twoDArray, 15))

