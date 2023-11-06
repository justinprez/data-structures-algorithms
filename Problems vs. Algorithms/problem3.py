def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return [0, 0]
    elif len(input_list) == 1:
        return [input_list[0], 0]

    heapsort(input_list) # O(n log n) sort function
    
    # logic to create the highest sum value
    num1, num2 = '', ''
    for i, val in enumerate(reversed(input_list)):
        if i % 2 == 0:
            num1 += str(val)
        else:
            num2 += str(val)
    return [int(num1), int(num2)]

def heapsort(arr):
    # first convert array to max heap in reverse order traversal
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,len(arr),i)

    # Then move top element to the end of array and heapify on first element
    for i in range(len(arr)-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    
def heapify(arr, n, i):
    largest_idx = i
    left_idx = i * 2 + 1
    right_idx = i * 2 + 2

    if left_idx < n and arr[left_idx] > arr[largest_idx]:
        largest_idx = left_idx
    
    if right_idx < n and arr[right_idx] > arr[largest_idx]:
        largest_idx = right_idx
    
    if largest_idx != i:
        arr[i], arr[largest_idx] = arr[largest_idx], arr[i]
        heapify(arr,n,largest_idx)



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print(sum(output),sum(solution))

        print("Fail")


test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1], [1, 1]])
test_function([[1], [1, 0]])
test_function([[], [0, 0]])
test_function([[0, 0, 0, 0, 0], [0, 0]])
test_function([[7, 7, 7, 7], [77, 77]])
test_function([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 86420]])
test_function([[9, 8, 7, 6, 5], [975, 86]])
test_function([[1, 1, 1, 1, 5, 6, 7], [7511, 611]])