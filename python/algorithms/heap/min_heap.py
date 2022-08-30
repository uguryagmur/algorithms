from typing import Any, Optional


class MinHeap:
    def __init__(self, data: Optional[list] = None) -> None:
        self._heap = list()
        for e in data:
            self.insert(e)

    def insert(self, data) -> None:
        self._heap.append(data)
        index = len(self._heap) - 1
        while True:
            if index == 0:
                break

            if self._heap[index] < self._heap[(index - 1) // 2]:
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
                if self._heap[index] > self._heap[index * 2 + 1]:
                    swap_list_elements(self._heap, index, index * 2 + 1)
                break
            else:
                min_index, min_elem = min(
                    [
                        (index * 2 + 1, self._heap[index * 2 + 1]),
                        (index * 2 + 2, self._heap[index * 2 + 2]),
                    ],
                    key=lambda x: x[1],
                )
                if self._heap[index] > min_elem:
                    swap_list_elements(self._heap, index, min_index)
                index = min_index

    def get_top(self) -> Any:
        return self._heap[0]

    def __getitem__(self, index: int) -> Any:
        return self._heap[index]


def swap_list_elements(array: list, swap_index_1: int, swap_index_2: int):
    temp = array[swap_index_1]
    array[swap_index_1] = array[swap_index_2]
    array[swap_index_2] = temp
