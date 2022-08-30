from typing import Any, List, Optional


class MaxHeap:
    def __init__(self, data: Optional[List[Any]] = None) -> None:
        self._heap = list()
        if data:
            for e in data:
                self.insert(e)

    def insert(self, data) -> None:
        self._heap.append(data)
        index = len(self._heap) - 1
        while True:
            if index == 0:
                break

            if self._heap[index] > self._heap[(index - 1) // 2]:
                swap_list_elements(self._heap, index, (index - 1) // 2)

            index = (index - 1) // 2

    def delete(self, data) -> None:
        index: int = self._heap.index(data)
        swap_list_elements(self._heap, index, len(self._heap) - 1)
        self._heap.pop()
        while True:
            if not index * 2 + 1 < len(self._heap):
                break
            elif not index * 2 + 2 < len(self._heap):
                if self._heap[index] < self._heap[index * 2 + 1]:
                    swap_list_elements(self._heap, index, index * 2 + 1)
            else:
                max_index, min_elem = max(
                    [
                        (index * 2 + 1, self._heap[index * 2 + 1]),
                        (index * 2 + 2, self._heap[index * 2 + 2]),
                    ],
                    key=lambda x: x[1],
                )
                if self._heap[index] < min_elem:
                    swap_list_elements(self._heap, index, max_index)
                index = max_index

    def get_top(self) -> Any:
        return self._heap[0]

    def __getitem__(self, index: int) -> Any:
        return self._heap[index]


def swap_list_elements(array: list, swap_index_1: int, swap_index_2: int):
    temp = array[swap_index_1]
    array[swap_index_1] = array[swap_index_2]
    array[swap_index_2] = temp
