def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1

    lo, hi = 0, len(input_list) - 1

    # Find pivot index first in O(logn)
    while lo <= hi:
        mid = (lo+hi)//2
        if input_list[mid] < input_list[-1]:
            hi = mid - 1 
        else:
            lo = mid + 1
    pivot = lo
    
    # Perform Binary search on each sorted subarray using pivot index
    left = binary_search(input_list, 0, pivot-1, number)
    right = binary_search(input_list, pivot, len(input_list)-1, number)

    return max(left, right)

def binary_search(input_list, left_idx, right_idx, number):
    l, r = left_idx, right_idx
    while l <= r:
        mid = (l + r) // 2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] > number:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[9, 11, 13, 2, 3, 4, 6, 8], 5])  # Number is not in the list
test_function([[4, 1, 2, 3], 4])
test_function([[3, 4, 1, 2], 4])
test_function([[2, 3, 4, 1], 4])
test_function([[1, 2, 3, 4], 4])
test_function([[1], 1])
