## حمل مكتبه matplotlib
## pip install matplotlib
## عشان الكود يرن ويظهر line chart

import time
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def quicksort(arr):
    a = arr.copy()
    
    def _quicksort(items, low, high):
        if low < high:
            p_idx = _partition(items, low, high)
            _quicksort(items, low, p_idx - 1)
            _quicksort(items, p_idx + 1, high)
            
    def _partition(items, low, high):
        rand_pivot = random.randint(low, high)
        items[rand_pivot], items[high] = items[high], items[rand_pivot]
        
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quicksort(a, 0, len(a) - 1)
    return a

def benchmark_algorithm(algorithm_fn, data):
    start_time = time.perf_counter()
    algorithm_fn(data)
    end_time = time.perf_counter()
    return end_time - start_time

def run_experiments():
    sizes = [100, 500, 1000, 2500, 5000]
    
    algorithms = {
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quicksort': quicksort,
        'Python Built-in (Timsort)': lambda arr: sorted(arr.copy())
    }
    
    results_random = {alg: [] for alg in algorithms}

    print("--- Starting Sorting Benchmark Lab Experiments ---\n")
    
    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]
        print(f"Array size n = {size}:")
        
        for name, fn in algorithms.items():
            exec_time = benchmark_algorithm(fn, data)
            results_random[name].append(exec_time)
            print(f"  - {name:27}: {exec_time:.6f} seconds")
        print("-" * 45)

    plt.figure(figsize=(10, 6))
    for name, times in results_random.items():
        plt.plot(sizes, times, marker='o', label=name)
        
    plt.title('Sorting Benchmark Lab - Performance Comparison (Random Data)')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_experiments()