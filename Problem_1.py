'''
1. Least Recently Used Cache

Least Recently Used (LRU) cache is a type of cache in which we remove the least recently used entry when the cache memory reaches it's limit.
For this first problem I designed a data structure known as Least Recently Used (LRU) cache. I have to use appropriate data structure(s) to implement the cache.

- In case of a cache hit, your get() operation should return the appropriate value.
- In case of a cache miss, your get() should return -1.
- While putting an element in the cache, put() / set() operation must insert the element. If the cache is full, I need to remove the least recently used entry first and then insert the element.

All operations must take O(1) time.
'''