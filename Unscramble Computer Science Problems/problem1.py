import collections


class LRU_Cache(object):

    def __init__(self, capacity = 0):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        
    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
our_cache = LRU_Cache(0)
our_cache.set(1, 1);
print(our_cache.get(1)) # return -1

## Test Case 2
our_cache = LRU_Cache(2)
our_cache.set(1, 1);
our_cache.set(1, 2);
our_cache.set(3, 3);
print(our_cache.get(1))  # return 2
print(our_cache.get(3))  # return 3
our_cache.set(2, 1);
print(our_cache.get(1))  # -1


## Test Case 3
our_cache = LRU_Cache()
our_cache.set(1, 1);
print(our_cache.get(1)) # return -1