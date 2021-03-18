
## Autocomplete with Tries

- ### TrieNode:

  Here the TrieNode needs to state whether it's a word end and it has a dictionary of children TrieNodes.

  ### Efficiency

  - insert : Time complexity : O(1), Space complexity : O(1)
  - suffixes: Time complexity : O(M\*N) where M is the number of children per Node, while N is the depth of the Trie tree.
     Space complexity: O(M\*N) with M being the length of a word (number of letters), and N the Number of words in the tree.

- ### Trie:

  A Trie has a root TrieNode, with insert and find functions

  ### Efficiency

  - insert: Time complexity : O(n), Space complexity : O(n)
  - find: Time complexity : O(n) where n is the length of the prefix.
    Space complexity : O(1)

