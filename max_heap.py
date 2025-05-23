class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print_heap(self):
        for i in self.heap:
            print(i)

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        
        while True:
            right_index = self._right_child(index)
            left_index = self._left_child(index)
            
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
                
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
    
        if len(self.heap) == 1:
            return self.heap.pop()
            
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        
        return max_value
    
# Testing the methods:

my_heap = MaxHeap()
my_heap.insert(0)
my_heap.insert(1)
my_heap.insert(2)
my_heap.insert(3)
my_heap.insert(4)
my_heap.insert(5)

print('Heap after insert:')
my_heap.print_heap()

my_heap.remove()

print('\nHeap after removing:')
my_heap.print_heap()