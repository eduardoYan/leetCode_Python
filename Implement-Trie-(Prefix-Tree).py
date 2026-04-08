1class Trie:
2
3    def __init__(self):
4        self.root = {} 
5
6    def insert(self, word: str) -> None:
7        node = self.root
8
9        for char in word:
10            if char not in node:
11                node[char] = {}
12            node = node[char]
13
14        node["#"] = True 
15
16    def search(self, word: str) -> bool:
17        node = self.root
18
19        for char in word:
20            if char not in node:
21                return False
22            node = node[char]
23        
24        return "#" in node 
25
26    def startsWith(self, prefix: str) -> bool:
27        node = self.root
28
29        for char in prefix:
30            if char not in node:
31                return False
32            node = node[char]
33
34        return True
35
36
37# Your Trie object will be instantiated and called as such:
38# obj = Trie()
39# obj.insert(word)
40# param_2 = obj.search(word)
41# param_3 = obj.startsWith(prefix)