def isPalindrome(x):
    # turn x into string --> str(x)
    # turn x into string and reverse --> str(x)[::-1]
    return str(x) == str(x)[::-1] 

print(isPalindrome(123))
print(isPalindrome(12321))
