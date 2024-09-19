'''
randomized_quicksort.py: Implements the randomized version of Quicksort.
Pivot is selected randomly from the subarray.
Reduces the likelihood of worst-case performance for sorted or reverse-sorted arrays.
'''

import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Randomly selecting a pivot
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quicksort(left) + middle + randomized_quicksort(right)


# Test randomized quicksort
if __name__ == "__main__":
    test_array = [3, 6, 8, 10, 12, 2, 1]
    print("Original array:", test_array)
    print("Sorted array:", randomized_quicksort(test_array))
