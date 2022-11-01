# define factorial function
# describing what happens if n is 3
# 3 * factorial(2)
# 2 * factorial(1)
# 1 * factorial(0)
# 1
# value is returned to the previous call
# 1 * 1 = 1
# 2 * 1 = 2
# 3 * 2 = 6

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# call factorial function
print(factorial(3))


# describing what happens if n is 3
# 1 * 1
# 1 * 2
# 2 * 3
# 6

# write the factorial function iteratively

def factorial_iter(n):
    result = 1
    # n+1
    for i in range(1, n+1):
        result *= i
    return result


# call factorial_iter function
print(factorial_iter(3))
