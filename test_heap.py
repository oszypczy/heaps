import pytest as pt
from heap import Heap

def test_heap_2_init():
    heap = Heap([35, 24, 12, 20, 7, 9,2], 2)
    assert heap.arr[6] == 2
    assert heap.arr[0] == 35
    assert heap.arr[4] == 7

def test_heap_3_init():
    heap = Heap([35, 24, 12, 20, 7, 9,2], 3)
    assert heap.arr[4] == 7
    assert heap.arr[0] == 35
    assert heap.arr[3] == 20

def test_heap_4_init():
    heap = Heap([35, 24, 12, 20, 7, 9,2], 4)
    assert heap.arr[6] == 2
    assert heap.arr[0] == 35
    assert heap.arr[4] == 7

def test_heap_2_remove_root():
    heap = Heap([35, 24, 12, 20, 7, 9,2], 2)
    assert heap.arr[0] == 35
    assert heap.arr[1] == 24
    assert heap.arr[3] == 20
    heap.remove_root()
    assert heap.arr[0] == 24
    assert heap.arr[1] == 20


def test_heap_3_remove_root():
    heap = Heap([35, 24, 12, 20, 7, 9,2], 3)
    assert heap.arr[0] == 35
    assert heap.arr[1] == 24
    assert heap.arr[3] == 20
    heap.remove_root()
    assert heap.arr[0] == 24
    assert heap.arr[1] == 9

def test_heap_4_remove_root():
    heap = Heap([35, 24, 12, 20, 7, 9,2], 4)
    assert heap.arr[0] == 35
    assert heap.arr[1] == 24
    assert heap.arr[3] == 20
    heap.remove_root()
    assert heap.arr[0] == 24
    assert heap.arr[1] == 9
    heap.remove_root()
    assert heap.arr[0] == 20
    assert heap.arr[1] == 9



