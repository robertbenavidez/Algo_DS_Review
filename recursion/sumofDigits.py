# Find the sum of positive integers that are 10 or more
# 11 1 + 1 = 2
# 25 2 + 5 = 7

def sumofDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer'
    assert n >= 9, 'The number must be 10 or more'
    if n == 0:  # base case
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n / 10)) # recursive case

print(sumofDigits(9))