# Heap Data Structures Implementation

This project contains Python implementations of both Max Heap and Min Heap data structures.

## Files

1. `heaps.py` - Contains both `MaxHeap` and `MinHeap` class implementations

## Classes

### MaxHeap
A complete implementation of a max heap data structure where the largest element is always at the root.

**Methods:**
- `insert(value)` - Inserts a value into the heap while maintaining the heap property
- `remove()` - Removes and returns the maximum value from the heap
- `_sink_down(index)` - Internal method to maintain heap property after removal
- `print_heap()` - Prints all elements in the heap
- Helper methods: `_left_child`, `_right_child`, `_parent`, `_swap`

### MinHeap
A complete implementation of a min heap data structure where the smallest element is always at the root.

**Methods:**
- `insert(value)` - Inserts a value into the heap while maintaining the heap property
- `remove()` - Removes and returns the minimum value from the heap
- `_sink_down(index)` - Internal method to maintain heap property after removal
- Helper methods: `_left_child`, `_right_child`, `_parent`, `_swap`

## Usage Example

```python
# MaxHeap example
my_max_heap = MaxHeap()
my_max_heap.insert(3)
my_max_heap.insert(1)
my_max_heap.insert(4)
my_max_heap.remove()  # Returns 4 (the max value)

# MinHeap example
my_min_heap = MinHeap()
my_min_heap.insert(3)
my_min_heap.insert(1)
my_min_heap.insert(4)
my_min_heap.remove()  # Returns 1 (the min value)