## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        
        suffix_list = []
        
        # Add word for suggestion in recursive call
        if self.is_word and suffix != '':
            suffix_list.append(suffix)
        
        # Stop condition of recursive call
        if len(self.children) == 0:
            return suffix_list
        
        for char in self.children:
            suffix_list.extend(self.children[char].suffixes(suffix=suffix+char))
            
        return suffix_list

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        cur_node = self.root
        
        for char in word:
            cur_node.insert(char)
            cur_node = cur_node.children[char]
        
        cur_node.is_word = True
        
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node = self.root
        
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        
        return cur_node


def test_trie(trie, wordList):
    # Insert words into trie
    for word in wordList:
        trie.insert(word)

    # Test 1: Basic Functionality
    prefix = "ant"
    expected_suffixes = ["hology", "agonist", "onym"]
    assert sorted(trie.find(prefix).suffixes()) == sorted(expected_suffixes)
    print(f"Test with prefix '{prefix}' passed!")
    
    # Test 2: Prefix Not in Trie
    prefix = "xy"
    assert trie.find(prefix) == False
    print(f"Test with prefix '{prefix}' passed!")

    # Test 3: Full Word as Prefix
    prefix = "trie"
    expected_suffixes = []
    assert sorted(trie.find(prefix).suffixes()) == sorted(expected_suffixes)
    print(f"Test with prefix '{prefix}' passed!")

    # Test 4: Empty Trie
    empty_trie = Trie()
    prefix = "ant"
    assert empty_trie.find(prefix) == False
    print(f"Test with prefix '{prefix}' on an empty trie passed!")

    # Test 5: Edge Cases
    prefix = ""
    expected_suffixes = wordList  # Since entire words are the suffixes if prefix is empty
    assert sorted(trie.find(prefix).suffixes()) == sorted(expected_suffixes)
    print(f"Test with empty prefix passed!")
    
    prefix = "a" * 1000  # Very long string
    assert trie.find(prefix) == False
    print(f"Test with very long prefix passed!")

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

test_trie(MyTrie, wordList)