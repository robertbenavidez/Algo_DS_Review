def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer' # edge case
    if n in [0, 1]:  # Base Case
        return 1
    else:
        return n * factorial(n - 1) # recursive call

print(factorial(4)) # 24