# Description:
# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
# Input: "race a car"
# Output: false
# Constraints: s consists only of printable ASCII characters.

def isPalindrome(s):
    # normalize string by removing non alphanumeric characters and spaces
    normalized_string = []
    for i in s:
        if i.isalnum():
            normalized_string += i.lower()
    # set up a left and a right pointer to compare letters
    n = len(normalized_string)
    left = 0
    right = n - 1

    while left < right:
        if normalized_string[left] != normalized_string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
            


    # loop through the string comparing the left and right pointer
print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car"))                     # False