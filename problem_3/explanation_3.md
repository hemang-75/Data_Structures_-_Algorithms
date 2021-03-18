
## Rearrange Array Elements

### Reasoning

- As we know that the elements in input can only be [0-9] , we can create an array of size 10 with each index representing an element and loop through the input to count the frequency of each number. we then loop through the frequency array from last index to the first, and at each index we add digits to the numbers until the frequency is 0 and then we return a tuple made up of the two numbers.

### Efficiency

- Time Complexity: Here we create the size 10 frequencey array - O(1), then we iterate through the input list once to count the frequencies of each digit O(n), then we loop through the frequency array O(1), performing at most O(n) operations through each iteration.So the time complexity is `O(n)`.

- Space Complexity: A size 10 array and 3 other values and a size 2 tuple only, regardless of the input
  therefore our space complexity is `O(1)`.
