
# Challenge What is the runtime complexity of this function

# O(n)
def power_r(a,b):
    try: # O(1)
        _ = int(b) # O(1)
    except ValueError: # O(1)
        print(f"Exponent (b) = ({b}) must be an integer") # O(1)
        return # O(1)
    if b == 0: # O(1)
        return 1 # O(1)
    elif b > 0: # O(1)
        return a * power_r(a, b - 1) # O(n) * O(1)
    else:
        return 1 / (a * power_r(a, -b - 1)) # O(1) + O(n) * O(1)
        # return 1 / power_r(a, -b)