'''
1. Least Recently Used Cache

Least Recently Used (LRU) cache is a type of cache in which we remove the least recently used entry when the cache memory reaches it's limit.
For this first problem I designed a data structure known as Least Recently Used (LRU) cache. I have to use appropriate data structure(s) to implement the cache.

- In case of a cache hit, your get() operation should return the appropriate value.
- In case of a cache miss, your get() should return -1.
- While putting an element in the cache, put() / set() operation must insert the element. If the cache is full, I need to remove the least recently used entry first and then insert the element.

All operations must take O(1) time.
'''

from collections import OrderedDict


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        try:
            get_v = self.cache.pop(key)
            self.cache[key] = get_v
            return get_v

        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return

        if key in self.cache:  # Update priority due to access
            self.cache.pop(key)
            self.cache[key] = value

        else:  # Add to cache
            if len(self.cache) < self.capacity:  # Still space on cache
                self.cache[key] = value

            else:  # No space available on cache
                self.cache.popitem(last=False)
                self.cache[key] = value


# Test Case

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because key 3 was thrown out
our_cache.set(7, 7)
print(our_cache.get(4))  # 4 is thrown out