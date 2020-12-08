# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# -------Input-And-Output-----------
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def two_sum(nums, target):
    # stores nums as the key and 
    # the index from the array as the value
    compliments = {}
    result = []
    for index, num in enumerate(nums):
        if compliments.get(num) is None:
            compliments[target - num] = index
        else:
            result = [compliments[num], index]
    print(compliments)
    return result

print(two_sum([1, 5, 6], 11)) # [1, 2]