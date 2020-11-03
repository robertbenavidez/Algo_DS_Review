# Calculate exponents using recursion

def power(base, exponent):
    assert exponent >= 0 and int(exponent), 'The exponent must be a positive integer'
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * power(base, exponent-1)

print(power(4, 2))