## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.word_end = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        for key in self.children:
            if self.children[key].word_end:
                result.append(suffix+key)
            result += self.children[key].suffixes(suffix+key)
        return result
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for w in word:
            current_node.insert(w)
            current_node = current_node.children[w]
        current_node.word_end = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for m in prefix:
            if m in current_node.children:
                current_node = current_node.children[m]
            else:
                return None
        return current_node
    

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",
    "poet", "path", "pathology", "poem",
]

for word in wordList:
    MyTrie.insert(word)
    
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
#            print('\n'.join(prefixNode.suffixes()))
            print(prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('No Input/prefix')

f("a")
#expected output: ['nt', 'nthology', 'ntagonist', 'ntonym']
print('---------------------------------------')

f("ant")
#expected output: ['hology', 'agonist', 'onym']
print('---------------------------------------')

f("tr")
#expected output: ['ie', 'igger', 'igonometry', 'ipod']
print('---------------------------------------')

f("fun")
#expected output: ['ction']
print('---------------------------------------')

f("trigger")
#expected output: []
print('---------------------------------------')

f("po")
#expected output: ['et', 'em']
print('---------------------------------------')

f("")
#expected output: No Input/prefix

