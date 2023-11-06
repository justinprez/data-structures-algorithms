def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    idx = 0
    left = 0
    right = len(input_list) - 1

    while idx <= right:
        if input_list[idx] == 2:
            input_list[right], input_list[idx] = input_list[idx], input_list[right]
            right -= 1
        elif input_list[idx] == 0:
            input_list[left], input_list[idx] = input_list[idx], input_list[left]
            idx += 1
            left += 1
        else:
            idx += 1
    
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 0, 1])

test_function([])  # Empty list
test_function([0, 0, 0, 0])  # All 0s
test_function([1, 1, 1, 1])  # All 1s
test_function([2, 2, 2, 2])  # All 2s
test_function([0, 0, 0, 1, 1, 1])  # 0s and 1s, no 2s
test_function([1, 1, 1, 2, 2, 2])  # 1s and 2s, no 0s
test_function([0, 0, 0, 2, 2, 2])  # 0s and 2s, no 1s
test_function([0])  # Single element 0
test_function([1])  # Single element 1
test_function([2])  # Single element 2
