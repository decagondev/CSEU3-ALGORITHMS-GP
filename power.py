"""
Given a value (a) and an exponent (b), compute the value of a^b

1. Understand
- What types of inputs can we expect?
    - Valid
        - Integer
    - Invalid
        - Decimal
        - String
        - Char

2. Plan
- Iterative or recursive approach?
    - First pass
        - Iterative
    - Second Pass
        - Recursive
        - Third Pass
        - Forth Pass?
"""

def power(a, b):
    # store a result
    result = 1

    # iterate while exponent (b) is greater than 0
    while b > 0:
        # multiply the result by the value (a)
        result *= a
        # decrement the exponent (b)
        b -= 1
    
    # return the result to the caller
    return result

print(power(4, 2)) # => 16