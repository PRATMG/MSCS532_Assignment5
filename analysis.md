# Report: Assignment 2: Quicksort Algorithm Implementation and Analysis

**Course:** Algorithms and Data Structures (MSCS-532-A01)  
**Student:** Prakash Tamang    
**Date:** 09/18/2024

---

## 1. Introduction
This report details the implementation and analysis of both deterministic and randomized Quicksort algorithms. Quicksort is a highly efficient sorting algorithm that uses the divide-and-conquer strategy to recursively sort subarrays. In this report, we explore the theoretical time complexities of the algorithm, provide a comparison between the deterministic and randomized versions, and empirically analyze their performance on various types of input data.

---

## 2. Design Choices

### 2.1 Deterministic Quicksort
The deterministic version of Quicksort in this project uses a fixed strategy to select the pivot. Specifically, the middle element of the array is chosen as the pivot at each recursive step. This approach is simple to implement and often leads to good average performance for unsorted input arrays. 

- **Pivot Selection:** The middle element of the array was chosen to avoid poor performance in cases of already sorted or reverse-sorted arrays, which can cause the worst-case scenario if the first or last element is selected as the pivot.
- **Partitioning Strategy:** The array is partitioned into elements smaller than, equal to, and greater than the pivot. These subarrays are then recursively sorted.
- **Base Case:** The recursion ends when the subarray contains zero or one element, in which case no sorting is required.

[Link to deterministic Quicksort implementation](./quicksort.py)

### 2.2 Randomized Quicksort
In the randomized version of Quicksort, the pivot is chosen randomly at each recursive step to reduce the likelihood of encountering the worst-case time complexity. This randomization ensures that even if the input is in sorted or reverse-sorted order, the likelihood of poor partitioning is significantly reduced.

- **Pivot Selection:** A random element from the subarray is selected as the pivot.
- **Partitioning Strategy:** As with the deterministic version, the array is divided into elements smaller than, equal to, and greater than the pivot.
- **Base Case:** The base case remains the same as in deterministic Quicksort.

[Link to randomized Quicksort implementation](./randomized_quicksort.py)

---

## 3. Performance Analysis

### 3.1 Time Complexity Analysis

- **Best-case Time Complexity:**  
  In the best case, the pivot splits the array into two equal parts at every step, leading to the recurrence:
  T(n) = 2T(n/2) + O(n)

This solves to \( O(n log n) \). The best-case scenario occurs when the pivot consistently divides the array evenly (Cormen et al., 2022, p. 188).

- **Average-case Time Complexity:**  
On average, the pivot will divide the array into two roughly equal parts, resulting in a time complexity of \( O(n log n) \). This is because the recurrence relation for the average case remains similar to the best-case recurrence (Cormen et al., 2022, p. 189).

- **Worst-case Time Complexity:**  
The worst-case time complexity is \( O(n^2) \), which occurs when the pivot consistently divides the array into highly unbalanced partitions (e.g., when the input is already sorted or reverse-sorted). The recurrence for this case is: T(n) = T(n-1) + O(n)

which solves to \( O(n^2) \) (Cormen et al., 2022, p. 188).

### 3.2 Space Complexity
Quicksort has a space complexity of \( O(log n) \) due to the recursion stack depth in the average and best cases. However, in the worst case, the recursion depth can reach \( O(n) \) if the array is consistently unbalanced. In both deterministic and randomized versions, no additional memory is required for the array, except for the space used by the recursion stack (Cormen et al., 2022, p. 188).

---

## 4. Empirical Analysis

### 4.1 Testing Approach
Both Quicksort implementations were tested on arrays of different sizes and distributions, including:
1. **Random arrays:** The most general case.
2. **Sorted arrays:** Represents the worst-case scenario for deterministic Quicksort.
3. **Reverse-sorted arrays:** Another worst-case scenario for deterministic Quicksort.

[Link to run time analysis implementation](./compare_quicksort.py)

---

### 4.2 Results
The randomized version of Quicksort consistently performed better on sorted and reverse-sorted arrays, as expected. The deterministic version experienced significant slowdowns in these cases, while the randomized version maintained near \( O(n log n) \) performance.

### 4.2 Results
The table below shows the running times (in seconds) of both deterministic and randomized Quicksort implementations for different array sizes and input distributions (random, sorted, and reverse-sorted arrays).

| Array Size | Array Type       | Deterministic Quicksort (s) | Randomized Quicksort (s) |
|------------|------------------|-----------------------------|--------------------------|
| 1000       | Random           | 0.00123                     | 0.00144                  |
| 1000       | Sorted           | 0.00077                     | 0.00136                  |
| 1000       | Reverse Sorted   | 0.00080                     | 0.00139                  |
| 5000       | Random           | 0.00635                     | 0.00732                  |
| 5000       | Sorted           | 0.00471                     | 0.00803                  |
| 5000       | Reverse Sorted   | 0.00486                     | 0.00754                  |
| 10000      | Random           | 0.01271                     | 0.01448                  |
| 10000      | Sorted           | 0.00999                     | 0.01823                  |
| 10000      | Reverse Sorted   | 0.01167                     | 0.01598                  |

### 4.3 Discussion
The results show that for random arrays, the performance of deterministic and randomized Quicksort is quite similar, with both performing efficiently in \( O(n log n) \) time. However, for sorted and reverse-sorted arrays, the randomized version performs slightly worse due to the overhead of selecting a random pivot. Interestingly, deterministic Quicksort performs better for sorted arrays, but randomization helps avoid worst-case scenarios in general cases.

### 4.3 Discussion
The empirical results confirm that randomizing the pivot reduces the likelihood of encountering the worst-case scenario. Even for already sorted and reverse-sorted arrays, the randomized Quicksort maintains its \( O(n log n) \) performance due to the unpredictable pivot selection.

---

## 5. Conclusion

Both deterministic and randomized Quicksort algorithms are highly efficient under normal conditions, with an average-case time complexity of \( O(n log n) \). However, the deterministic version suffers in the worst-case scenario when the input is already sorted or reverse-sorted. The randomized version mitigates this issue by randomly selecting the pivot, ensuring that the probability of encountering the worst-case scenario is significantly reduced. This makes the randomized Quicksort more robust across a wider range of input distributions.

---

## 6. References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). The MIT Press.




