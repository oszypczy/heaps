from heap import Heap
import random
import time
import gc
from matplotlib import pyplot as plt
import os


def main():
    numbers = [random.randint(1, 30000) for _ in range(100000)]
    # numbers.sort(reverse=True)
    # get_creation_heap_graphs(numbers, 'Heaps_creation_times_sorted.png')
    # get_remove_root_heap_graphs(numbers, 'Heap_remove_root_times_sorted.png')

def get_creation_heap_graphs(numbers, title):
    x_axis = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    y_axis_2 = []
    y_axis_3 = []
    y_axis_4 = []
    for data in x_axis: # 2-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(numbers[:data], 2)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_2.append(stop - start)
    for data in x_axis: # 3-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(numbers[:data],3)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_3.append(stop - start)
    for data in x_axis: # 4-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(numbers[:data],4)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_4.append(stop - start)
    plt.plot(x_axis, y_axis_2, '-',label="binary heap")
    plt.plot(x_axis, y_axis_3, '-',label="ternary heap")
    plt.plot(x_axis, y_axis_4, '-',label="4-ary heap")
    plt.legend()
    plt.title(label='Heaps creation time graphs')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('heap_graphs'):
        os.makedirs('heap_graphs')
    plt.savefig(os.path.join('heap_graphs', title), dpi=200)

def get_remove_root_heap_graphs(numbers, title):
    x_axis = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    y_axis_2 = []
    y_axis_3 = []
    y_axis_4 = []
    for data in x_axis: # 2-arny
        heap_2 = Heap(numbers.copy(), 2)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for _ in range(data):
            heap_2.remove_root()
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_2.append(stop - start)
    for data in x_axis: # 3-arny
        heap_3 = Heap(numbers.copy(), 3)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for _ in range(data):
            heap_3.remove_root()
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_3.append(stop - start)
    for data in x_axis: # 4-arny
        heap_4 = Heap(numbers.copy(), 4)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for _ in range(data):
            heap_4.remove_root()
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_4.append(stop - start)
    plt.plot(x_axis, y_axis_2, '-',label="binary heap")
    plt.plot(x_axis, y_axis_3, '-',label="ternary heap")
    plt.plot(x_axis, y_axis_4, '-',label="4-ary heap")
    plt.legend()
    plt.title(label='Heaps remove_root time graphs')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('heap_graphs'):
        os.makedirs('heap_graphs')
    plt.savefig(os.path.join('heap_graphs', title), dpi=200)

if __name__ == "__main__":
    main()