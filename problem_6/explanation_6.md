
## Max and Min in a Unsorted Array

### Reasoning

In this problem since we know that the input list has at one element or more we can start by assuming the first element is the min and max, then we loop through the entire list and for each element we test if it's smaller then min, then assign it is value to min, otherwise if it is larger than max assign it's value to max.
At the end of iteration through the array we have both the min and the max.

### Efficiency

- Time Complexity: we are iterating once through the entire array, making O(1) operations at each iteration, and then returning min and max,
  so the time complexity is `O(n)`.

- Space Complexity: `O(1)` since we only use 2 variables regardless of the input.
