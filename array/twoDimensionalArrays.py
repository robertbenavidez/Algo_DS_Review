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
newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0 )
print(newTwoDArray)