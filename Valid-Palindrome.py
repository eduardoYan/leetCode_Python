1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        filtered =''
4
5        for char in s:
6            if char.isalnum():
7                filtered +=char.lower()
8        
9        left =0
10        right = len(filtered) -1
11
12        while left < right:
13            if filtered[left] == filtered[right]:
14                left = left +1
15                right = right -1
16            else:
17                return False
18        
19        return True