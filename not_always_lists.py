# consider using arrays for large lists of numbers

# collections.deque is a more efficient FIFO data structure

# 'set' if the code frequently checks whether an item is present
## sets are optimized for fast membership checking, and are also iterable
## but they aren't sequences

## array.array if a list only contains numbers is way more efficient 
## than lists
## support all mutable sequence operations
## as well additional methods for fast loading and saving
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

