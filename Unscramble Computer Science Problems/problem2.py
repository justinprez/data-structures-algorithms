import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if suffix == None:
        return []

    list_of_paths = []
    for p in os.listdir(path):
        if p.endswith("." + suffix):
            list_of_paths.append(p)
        elif os.path.isdir(os.path.join(path,p)):
            list_of_paths.extend(find_files(suffix, os.path.join(path,p)))

    return list_of_paths

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

testdir = os.path.join(os.getcwd(),'testdir')

## Test Case 1
print(find_files(suffix='c', path=testdir)) # [a.c', 'b.c', 'a.c', 't1.c']

## Test Case 2
print(find_files(suffix='h', path=testdir)) # ['a.h', 'b.h', 'a.h', 't1.h']

## Test Case 3
print(find_files(suffix='z', path=testdir)) # []

# Test Case 4
print(find_files(suffix='', path=testdir)) # []