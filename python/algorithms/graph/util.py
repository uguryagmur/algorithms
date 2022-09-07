from typing import List


def find_dsu(id: int, parent: List[int]):
    if parent[id] == -1:
        return id
    parent[id] = find_dsu(parent[id], parent)
    return parent[id]


def union_dsu(id1: int, id2: int, parent: List[int]):
    s1 = find_dsu(id1, parent)
    s2 = find_dsu(id2, parent)
    if s1 != s2:
        parent[s2] = s1
