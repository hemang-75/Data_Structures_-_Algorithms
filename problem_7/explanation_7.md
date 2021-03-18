
## HTTPRouter using a Trie

- ### RouteTrieNode:

  The RouteTrieNode has a children dictionary and a handler

  ### Efficiency

  - insert: Time complexity : O(1), Space complexity : O(n) where n is the length of the route.

- ### RouteTrie:

  The RouteTrie has a root RouteTrieNode, with insert and find functions

  ### Efficiency

  - insert: Time complexity : O(n), Space complexity : O(n)
  - find: Time complexity : O(N\*M) where N is the length of the part of the route, M is the depth of the route.
    Space complexity : O(1)

- ### Router:

  The Router has a root RouteTrie, with add_handler and lookup and split_path functions

  ### Efficiency

  - add_handler: Time complexity : O(n), Space complexity : O(n)
  - lookup: Time complexity : O(N\*M) where N is the length of the part of the route, M is the depth of the route.
    Space complexity : O(1)
  - split_path: Time complexity : O(n), Space complexity : O(n)
