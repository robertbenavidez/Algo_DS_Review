def containsDuplicate(nums):
    # if nums contains duplicates than the set() will remove the duplicates
    # so the length will be less than original.
    # The return will either be True or False
    return len(nums) > len(set(nums))




print(containsDuplicate([1,2,3,1]))    # True
print(containsDuplicate([1, 2, 3, 4])) # False