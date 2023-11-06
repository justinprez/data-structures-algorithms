# Analysis

## Problem 1
The binary search algorithm is used here due to its logarithmic efficiency which suits the problem's requirement. Binary search is an efficient way to find a particular value from a sorted set of values. In this case, the set of values is the range from 0 to the given number, and we are searching for the square root within this range. Handling the base cases (0 and 1) separately at the beginning simplifies the main part of the function. This avoids unnecessary calculations and ensures the function directly returns for these simple inputs.
### Time Complexity
Binary search has a time complexity of O(log n).
### Space Complexity
The space complexity is O(1).


### Problem 2
The function first determines the pivot point of the rotated sorted array in O(logn) time. Once the pivot is found, the function performs a binary search on the two subarrays (the ones before and after the pivot) in O(logn) time for each subarray. 
### Time Complexity
he total time complexity remains O(logn).
### Space Complexity
The space complexity is O(1).


### Problem 3
The use of heapsort is in line with the problem's requirement for O(nlogn) time complexity. A heap-based approach to sorting takes advantage of the properties of a binary heap. The steps to create two numbers using the reversed list, ensures the numbers are created with alternating digits from the sorted list and guarantees that we get two numbers such that their sum is maximum.
### Time Complexity
The function uses heapsort which has a time complexity of O(nlogn) where n is the length of the input list. Iterating over the reversed list to form the two numbers has a time complexity of O(n). Thus, the overall time complexity is dominated by heapsort: O(nlogn).
### Space Complexity
The space complexity is O(1) as heapsort is an in-place sorting algorithm.


## Problem 4
The loop continues as long as idx doesn't surpass the right pointer. Within this loop:
- If input_list[idx] is 2, the value at idx is swapped with the value at right, and then the right pointer is decremented. This ensures all 2s are moved to the end of the list.
- If input_list[idx] is 0, the value at idx is swapped with the value at left, and both idx and left pointers are incremented. This ensures all 0s are moved to the beginning of the list.
- If input_list[idx] is 1, only idx is incremented, ensuring 1s stay in the middle.
### Time Complexity
This loop, at worst, traverses the entire list once, so it has a time complexity of O(n), where n is the length of the input list.
### Space Complexity
The space complexity is O(1).


## Problem 5
TrieNode Class:
- __init__: Initializes the node with an empty dictionary for its children and a flag is_word indicating if the node represents the end of a word. The time complexity and space complexity is O(1).
- insert: Adds a child node to the current node if it doesn't already exist. Time complexity is O(1) (for dictionary operations) and space complexity could be O(1) per character if the node doesn't exist.
- suffixes: This method is used to fetch all the suffixes of a given prefix in the trie. It uses recursion to traverse down the trie until it finds all words. In the worst case, this can be O(n) where n is the number of nodes in the trie (i.e., the total number of characters in the trie). The space complexity is the space required to store the list of suffixes, which can be O(n) in the worst case, plus the space used by the call stack due to recursion (which is at most the depth of the trie).

Trie Class:
- __init__: Initializes the Trie with a root node. Time and space complexity is O(1).
- insert: Inserts a word into the Trie. This function traverses the word character by character and inserts nodes as required. Since the function processes each character of the word once, the time complexity is O(n), where n is the length of the word being inserted. The space complexity is also O(n) in the worst case, if all characters of the word lead to new nodes.
- find: Finds if a prefix exists in the Trie. It traverses character by character for the given prefix. The time complexity is O(n) where n is the length of the prefix. The space complexity is O(1).


## Problem 6
As we iterate through the list, we can keep track of the current minimum and maximum values, updating them as we encounter smaller or larger values.
### Time Complexity
The code iterates through the list of integers just once. So, the time complexity is O(n).
### Space Complexity
We are using a constant amount of extra space, therefore the space complexity is O(1).


## Problem 7
### Time Complexity:
Insertion (add_handler method in the Router class):
- split_path: O(k), where k is the length of the path string. Inserting into RouteTrie: O(n), where n is the number of parts in the path. Combined, the time complexity for insertion remains O(k + n), but since n (number of parts) is limited by the length of the path string k, we can simplify this to O(k).
- Lookup (lookup method in the Router class): split_path: O(k), where k is the length of the path string. Finding in RouteTrie: O(n), where n is the number of parts in the path.
Combined, similar to insertion, the time complexity for lookup remains O(k + n), which simplifies to O(k) since n is limited by k.
### Space Complexity:
- RouteTrieNode: Each node has a dictionary children, which, in the worst case, will have as many entries as there are unique parts in all the paths. In practice, the number of unique parts will be far less than the number of paths, especially with shared prefixes. Each node also has a handler, which is a string, but we can consider this constant space for our analysis since the size of this string doesn't grow with the size of the input.
- RouteTrie: The space is primarily consumed by the nodes in the Trie. In the worst case, where every path part is unique, the space taken by the Trie will be O(p * n) where p is the average number of parts per path, and n is the number of paths. In many real-world scenarios, though, paths will have shared parts, and the Trie will consume significantly less space than this worst-case scenario.
- Router: The router uses a RouteTrie and two strings (root_handler and not_found_handler), so its space complexity is mainly determined by the RouteTrie.

Given these analyses, the time complexities for insertion and lookup are both O(k), where k is the length of the path string. The space complexity for the Trie-based router, in the worst case, is O(p * n), where p is the average number of parts per path and n is the number of paths.