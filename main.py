from heap import Heap
from random import randint as jd
import time
import gc
from matplotlib import pyplot as plt
import sys
import os

def main():
    # arr = [35, 24, 12, 20, 7, 9, 2, 18, 1, 3, 5, 4]
    # heap = Heap(arr, 4)
    # heap.print_heap()

    nums = [jd(1,30_000) for _ in range(10_000)]
    # get_creation_heap_graphs(nums,'Heaps_creation_times.png')
    get_remove_root_heap_graphs(nums, 'Heap_remove_root_times.png')



def get_creation_heap_graphs(numbers,title): # nar_num -> 2,3 or 4
    xd = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    x_axis = [(_*10) for _ in xd]
    y_axis_2 = []
    y_axis_3 = []
    y_axis_4 = []
    for range in x_axis: # 2-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(numbers[:range],2)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_2.append(stop - start)
    for range in x_axis: # 3-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(numbers[:range],3)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_3.append(stop - start)
    for range in x_axis: # 4-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        Heap(numbers[:range],4)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_4.append(stop - start)


    plt.plot(x_axis, y_axis_2, '-',label="binary heap")
    plt.plot(x_axis, y_axis_3, '-',label="ternary heap")
    plt.plot(x_axis, y_axis_4, '-',label="4-ary heap")
    plt.legend()
    plt.title(label='Heaps creation time graphs')
    plt.xticks(color='teal')
    plt.yticks(color='teal')
    plt.xlabel(xlabel='Collection size')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    if not os.path.exists('Heaps_plots'):
        os.makedirs('Heaps_plots')
    plt.savefig(os.path.join('Heaps_plots', title),dpi=200)


def get_remove_root_heap_graphs(numbers,title): # nar_num -> 2,3 or 4
    xd = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    x_axis = [(_*10) for _ in xd]
    y_axis_2 = []
    y_axis_3 = []
    y_axis_4 = []
    heap_2 = Heap(numbers,2)
    heap_3 = Heap(numbers,3)
    heap_4 = Heap(numbers,4)
    for range in x_axis: # 2-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()

        for n in numbers[:range]: #  _not sure_
            heap_2.remove_root()

        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_2.append(stop - start)

    for range in x_axis: # 3-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]: # remove
            heap_3.remove_root()
        stop = time.process_time()
        if gc_old: gc.enable()
        y_axis_3.append(stop - start)

    for range in x_axis: # 4-arny
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for n in numbers[:range]: # remove
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
    if not os.path.exists('Heaps_plots'):
        os.makedirs('Heaps_plots')
    plt.savefig(os.path.join('Heaps_plots', title),dpi=200)


if __name__ == "__main__":
    main()