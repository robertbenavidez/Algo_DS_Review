# def factorial(n):
#     assert n >= 0 and int(n) == n, 'The number must be a positive integer' # edge case
#     if n in [0, 1]:  # Base Case
#         return 1
#     else:
#         return n * factorial(n - 1) # recursive call

# print(factorial(4)) # 24

# def recursiveRange(num):

#   # Base case
#   if num <= 0:
#     return 0
#   else:
#     return num + recursiveRange(num -1)

# print(recursiveRange(6))
def reverse(string):
    
  if len(string) <= 1:
    return string
  else:
    return reverse(string[1:]) + string[0]


print(reverse('taco'))