# selection-sort
A user-input selection sort in ascending and descending order with sorting process

<h1>Selection Sort</h1>

- Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
- The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted.

<h3>How does Selection Sort Algorithm work?</h3>

<img align="right" alt="Coding" width="325" src="https://github.com/davenarchives/selection-sort/assets/160004612/736a4852-d150-495d-a1bc-ac13bc3c6f48">

1. Find the minimum element in the unsorted list.
2. Swap it with the first element in the unsorted list.
3. Repeat steps 1 & 2 for the remaining unsorted portion (excluding the first element).

<h3>Advantages:</h3>

- **Simple**: Easy to understand and implement, making it good for learning.
- **Low memory**: Sorts data in-place, requiring minimal extra space.

<h3>Disadvantages:</h3>

- **Slow for large lists**: Performance gets worse (O(n^2)) as the number of elements (n) increases.
- **Not the fastest**:  Other algorithms like merge sort or quicksort are generally faster.
