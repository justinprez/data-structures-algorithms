def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:  # Handle the case of an empty list
        return None

    min_val = ints[0]
    max_val = ints[0]

    for num in ints:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

# Test
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test 1: Test with a list containing repeating numbers.
l = [2, 2, 2, 2, 2, 2]
print("Pass" if ((2, 2) == get_min_max(l)) else "Fail")

# Test 2: Test with a list containing negative numbers.
l = [-1, -2, -3, -4, -5]
print("Pass" if ((-5, -1) == get_min_max(l)) else "Fail")

# Test 3: Test with a list containing a single number.
l = [4]
print("Pass" if ((4, 4) == get_min_max(l)) else "Fail")

# Test 4: Test with an empty list.
l = []
print("Pass" if (None == get_min_max(l)) else "Fail")

# Test 5: Test with a list containing both positive and negative numbers.
l = [-10, -5, 0, 5, 10]
print("Pass" if ((-10, 10) == get_min_max(l)) else "Fail")

# Test 6: Test with a larger range of numbers.
l = [i for i in range(-1000, 1000)]
random.shuffle(l)
print("Pass" if ((-1000, 999) == get_min_max(l)) else "Fail")