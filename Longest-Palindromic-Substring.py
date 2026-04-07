1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        
4        answer = ''
5
6        def expand(left,right):
7            while left >=0 and right < len(s) and s[left]==s[right]:
8                left = left-1
9                right= right+1
10            return s[left+1:right]
11
12        for i in range(len(s)):
13                odd= expand(i,i)
14                even = expand(i,i+1)
15                
16                answer = max(answer, odd, even, key=len)
17        
18        return answer