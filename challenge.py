
# Challenge What is the runtime complexity of this function

# O(n)
def power_r(a,b):
    # Error cehcking
    # try to cast our exponent to an int
    try: # O(1)
        _ = int(b) # O(1)
    # exception on fail with error message
    except ValueError: # O(1)
        print(f"Exponent (b) = ({b}) must be an integer") # O(1)
        return # O(1)
    # and return
    # base case
    if b == 0: # O(1)
        return 1 # O(1)
    # recursive positive case
    elif b > 0: # O(1)
        # Recursive case
        # call the function on b - 1

        return a * power_r(a, b - 1) # O(n) * O(1)
    # recursive negative case
    else:
        # return 1 divided by a multiplied by the function with b - 1
        return 1 / (a * power_r(a, -b - 1)) # O(1) + O(n) * O(1)
        # or return 1 divided by function with -b
        # return 1 / power_r(a, -b)