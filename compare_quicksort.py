'''
compare_quicksort.py:
This script generates arrays of different sizes and distributions (random, sorted, reverse-sorted).
Measures the time taken by both deterministic and randomized Quicksort implementations.
The results are printed to show the performance difference across different input distributions.
'''

import time
import random
from quicksort import quicksort
from randomized_quicksort import randomized_quicksort

# Generate test cases
def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

# Compare deterministic and randomized quicksort
def compare_quicksorts():
    sizes = [1000, 5000, 10000]
    distributions = {
        "random": generate_random_array,
        "sorted": generate_sorted_array,
        "reverse_sorted": generate_reverse_sorted_array,
    }

    for size in sizes:
        print(f"\nArray size: {size}")
        for dist_name, dist_func in distributions.items():
            arr = dist_func(size)
            
            # Measure deterministic quicksort time
            det_time = measure_time(quicksort, arr.copy())
            print(f"{dist_name.capitalize()} array - Deterministic Quicksort: {det_time:.5f} seconds")
            
            # Measure randomized quicksort time
            rand_time = measure_time(randomized_quicksort, arr.copy())
            print(f"{dist_name.capitalize()} array - Randomized Quicksort: {rand_time:.5f} seconds")

if __name__ == "__main__":
    compare_quicksorts()
