
## Dutch National Flag Problem

### Reasoning

since we only have 3 values, all we need to do is put the 2's at the end and 0 at the start and the array will be sorted, we can do that by having an index for the zeros at the start of the array `m_idx`, index for the twos at the end `n_idx`, and an index to iterate through the array with `idx`, while `idx` is less than `n_idx` then we haven't walked the whole array once yet:

- so we keep checking if `n_idx` is over a 2 we reduce it by 1
- otherwise if `idx` is over a 0 we swap it with `m_idx` and move them both 1 forward
- otherwise if `idx` is over a 2 we swap it with `n_idx` and reduce `n_idx` by 1
- or if `idx` is over a 1 we just move `idx` forward.

and by the end the 2's will be at the end, the zeros at the start and the 1's in the middle.

### Efficiency

- Time Complexity: we only loop through the array once, and do O(1) operations in each loop, so the time complexity is `O(n)`.

- Space Complexity: all the operations on the array are inplace, we only use 3 variables for the indices, so the complexity is `O(1)`
