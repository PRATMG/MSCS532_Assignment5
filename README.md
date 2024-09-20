# Assignment 5: Quicksort Algorithm Implementation, Analysis and Randomization 

## Project Overview

This repository contains the implementation of both deterministic and randomized versions of the Quicksort algorithm. The algorithms are analyzed for their performance, both theoretically and empirically, across different input distributions (random, sorted, and reverse-sorted arrays). 

### Files Included:

| Filename                          | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| [quicksort.py](./quicksort.py)     | Python script implementing the deterministic version of the Quicksort algorithm. |
| [randomized_quicksort.py](./randomized_quicksort.py) | Python script implementing the randomized version of the Quicksort algorithm.  |
| [compare_quicksort.py](./compare_quicksort.py) | Python script to compare the running time of the deterministic and randomized versions of Quicksort.  |
| [analysis.md](./analysis.md)           | A detailed report covering design choices, performance analysis, and results. |
| [README.md](./README.md)           | This file. Instructions on how to run the code and a summary of the findings. |



## How to Run the Code

### Requirements:
- Python 3.x

### Running the Code:
1. Download the source code from the provided `.py` file or copy the provided code.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `.py` file is saved.
4. Run the Python script by typing the following command:
   for windows:
   ``` bash
   python filename.py
   ```
   for MacOS (or Linux):
   ``` bash
   python3 filename.py
   ```
   Replace `<filename>` with the actual name of the Python file.

   ## Summary of Findings

### Performance Analysis:

- **Best-case Complexity:** Both deterministic and randomized Quicksort algorithms have a best-case time complexity of \( O(n log n) \) when the pivot consistently divides the array into balanced subarrays.
- **Average-case Complexity:** The average time complexity for both algorithms is also \( O(n log n) \), with randomized Quicksort reducing the chance of encountering the worst-case performance.
- **Worst-case Complexity:** The deterministic Quicksort has a worst-case time complexity of \( O(n^2) \), which occurs when the pivot divides the array into highly unbalanced partitions. Randomized Quicksort mitigates this by randomly choosing the pivot.

### Empirical Results:

The following table summarizes the running times (in seconds) of both algorithms across different array sizes and input types:

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

### Key Observations:

- **Random Arrays:** Both algorithms perform similarly, showing near-optimal \( O(n log n) \) performance.
- **Sorted Arrays:** Deterministic Quicksort performs efficiently, but Randomized Quicksort incurs slight overhead due to random pivot selection.
- **Reverse-Sorted Arrays:** Deterministic Quicksort shows a slight decline in performance due to unbalanced partitions, while Randomized Quicksort maintains consistent performance.
