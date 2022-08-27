from algorithms.heap import create_heap, MinHeap, MaxHeap, max_heap
from typing import Union


def assert_heap_structure_is_satisfied(heap: Union[MinHeap, MaxHeap], is_max: bool = False):
    index = 0
    while True:
        if not index*2+1 < len(heap._heap):
            break
        elif not index*2+2 < len(heap._heap):
            assert (heap[index] > heap[index*2+1] if is_max else heap[index] < heap[index*2+1])
            break
        else:
            assert (heap[index] > heap[index*2+1] if is_max else heap[index] < heap[index*2+1])
            assert (heap[index] > heap[index*2+2] if is_max else heap[index] < heap[index*2+2])
            index += 1


def test_heap_creation_from_data():
    data = [3, 5, 6, 8, 9, 10]
    min_heap = create_heap(data)
    assert_heap_structure_is_satisfied(min_heap)
    

def test_max_heap_creation_from_data():
    data = [3, 5, 6, 8, 9, 10]
    max_heap = create_heap(data, is_max=True)
    assert_heap_structure_is_satisfied(max_heap, is_max=True)

def test_heap_insertion():
    data = [3, 5, 6, 8, 9, 10]
    min_heap = create_heap(data)
    min_heap.insert(4)
    assert min_heap._heap == [3, 5, 4, 8, 9, 10, 6]

    data = [2, 5, 6, 11, 12, 14, 17, 19, 21, 23]
    min_heap = create_heap(data)
    min_heap.insert(7)
    assert_heap_structure_is_satisfied(min_heap)
    min_heap.insert(1)
    assert_heap_structure_is_satisfied(min_heap)
    assert min_heap.get_top() == 1

    data = [2, 5, 6, 11, 12, 14, 17, 19, 21, 23]
    max_heap = create_heap(data, is_max=True)
    max_heap.insert(7)
    assert_heap_structure_is_satisfied(max_heap, is_max=True)
    max_heap.insert(88)
    assert_heap_structure_is_satisfied(max_heap, is_max=True)
    assert max_heap.get_top() == 88

def test_heap_deletion():
    data = [3, 5, 6, 8, 9, 10]
    min_heap = create_heap(data)
    min_heap.delete(5)
    assert min_heap._heap == [3, 8, 6, 10, 9]

    data = [2, 5, 6, 11, 12, 14, 17, 19, 21, 23]
    min_heap = create_heap(data)
    min_heap.delete(6)
    assert_heap_structure_is_satisfied(min_heap)
    min_heap.delete(2)
    assert_heap_structure_is_satisfied(min_heap)
    assert min_heap.get_top() == 5

    data = [2, 5, 6, 11, 12, 14, 17, 19, 21, 23]
    max_heap = create_heap(data, is_max=True)
    max_heap.delete(6)
    assert_heap_structure_is_satisfied(max_heap, is_max=True)
    max_heap.delete(23)
    assert_heap_structure_is_satisfied(max_heap, is_max=True)
    assert max_heap.get_top() == 21