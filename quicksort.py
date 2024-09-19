'''
quicksort.py: Implements the deterministic version of Quicksort.
Pivot is selected as the middle element of the array.
Recursively sorts subarrays.
'''
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Deterministic pivot selection (middle element)
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


# Test deterministic quicksort
if __name__ == "__main__":
    test_array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", test_array)
    print("Sorted array:", quicksort(test_array))
