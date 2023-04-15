from heap import Heap

def main():
    arr = [35, 24, 12, 20, 7, 9, 2, 18, 1, 3, 5, 4]
    heap = Heap(arr, 4)
    heap.print_heap()

if __name__ == "__main__":
    main()