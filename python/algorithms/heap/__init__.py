from .max_heap import MaxHeap
from .min_heap import MinHeap
from typing import Any, List, Optional, Union


def create_heap(
    data: Optional[List[Any]] = None, is_max: bool = False
) -> Union[MaxHeap, MinHeap]:
    return MaxHeap(data) if is_max else MinHeap(data)
