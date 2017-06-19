# -*- coding: utf-8 -*-

from random import randint

class priority_queue:
    def __init__(self, array):
        self.heap = array
        self.priority_queue = []
        self.heap_size = len(array)
        self._build_heap()
        self._heap_sort()


    def get_priority_queue(self):
        if len(self.priority_queue) != len(self.heap):
            self._heap_sort()

        return self.priority_queue


    def get_heap(self):
        return self._heap


    # TODO: バグってる。一回insertしても何もないが100回insertするとおかしくなる
    def insert(self, key):
        self.heap.append(key)
        self.heap_size += 1
        key_pos = len(self.heap) - 1
        parent = self._parent(key_pos)

        while key > self.heap[parent]:
            tmp = key
            self.heap[key_pos] = self.heap[parent]
            self.heap[parent] = tmp
            key_pos = parent
            parent = self._parent(key_pos)


    def _parent(self, pos):
        # child is left
        if pos % 2 != 0:
            return (pos - 1) / 2
        else:
            return (pos - 2) / 2


    def _left(self, pos):
        return pos * 2 + 1


    def _right(self, pos):
        return pos * 2 + 2


    def _heapify(self, parent):
        left = self._left(parent)
        right = self._right(parent)
        max_node = parent
        if left < self.heap_size and self.heap[left] > self.heap[max_node]:
            max_node = left

        if right < self.heap_size and self.heap[right] > self.heap[max_node]:
            max_node = right

        if max_node != parent:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[max_node]
            self.heap[max_node] = tmp
            self._heapify(max_node)


    def _build_heap(self):
        max_target_node = len(self.heap) / 2
        for i in reversed(xrange(max_target_node)):
            self._heapify(i)


    def _heap_sort(self):
        # コピー渡し
        heap_bk = list(self.heap)
        for i in reversed(xrange(1, len(self.heap))):
            tmp = self.heap[0]
            self.heap[0] = self.heap[i]
            self.heap[i] = tmp
            self.heap_size -= 1
            self._heapify(0)

        self.priority_queue = self.heap
        self.heap = heap_bk
        self.heap_size = len(self.heap)


if __name__ == '__main__':
    unsorted_list = []
    for i in range(0, 100):
        unsorted_list.append(randint(1, 1000))

    queue = priority_queue(unsorted_list)
    for i in range(0, 100):
        queue.insert(randint(1, 1000))

    prev = 0
    sorted_ist = queue.get_priority_queue()
    for i in sorted_ist: 
        try:
            assert prev <= i
            prev = i
        except AssertionError:
            print "[Exception] assertion error. prev = %d, i = %d" % (prev, i)
            print sorted_ist
            print queue.get_heap()
            break
