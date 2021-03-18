
## Finding the Square Root of an Integer

### Reasoning

To find the floor of the sqrt of a number `N`, we are searching for a number `x` in the range `(0, N)` which should satisfy the condition `x^2 = N` or `(x^2 < N) and ((x+1)^2 > N)` and since the range `(0, N)` is sorted, we can use a version of binary search such that :

- sqrt will be `None` if the number is negative 
- first we start with the number itself as `x` and if it meets the condition above then it is the answer, otherwise if `(x^2 > N)` then the next `x = x/2`, if `(x^2 < N)` then `x` is between its current value and its previous value.

### Efficiency

- Time Complexity: As our algorithem halves the search range every iteration and performs O(1) calculations on every iteration so our Time complexity is `O(log(n))`.

- Space Complexity: Space Complexity is O(1) since we only use the same amount of memory (four variables only `(curr_num, prev_num, curr_square, next_square)`) regardles of the input


