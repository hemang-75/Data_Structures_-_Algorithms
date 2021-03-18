
## Search in a Rotated Sorted Array

### Reasoning

To search for a number in an array which is sorted and then rotated, one can use a modified version of binary search as they only need to change the conditions in which one search one half or the other after testing the middle.So
instead of testing if the target is greater than or smaller than the middle, one should test the halves of the array:

- first we test the middle, if it's the target then we return the middle index.
- otherwise we check one side, if it's ordered (i.e : value at last index greater than the one at the middle for the right side) we test if the target value is between the two values at the edges, otherwise if it's not ordered (then it's the rotated half) we test that the target value is greater than the start or smaller than the end.
- otherwise it must be in the other half or doesn't exist.

### Efficiency

- Time Complexity: Since we are using binary search with a few extra conditional statements of complexity O(1), then our time comlexity remains the same as binary search's `O(log(n))`.

- Space Complexity: O(1) per recursive iteration, since we do about log(n) iterations then it's of the order `O(log(n))`.
