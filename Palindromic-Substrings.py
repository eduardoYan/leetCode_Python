1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        count =0
4        def expand(left,right):
5            res=0
6            while left >=0 and right < len(s) and s[left]==s[right]:
7                res = res+1
8                right = right +1
9                left = left -1
10            return res
11
12        for i in range(len(s)):
13                count = count + expand(i,i)
14                count = count + expand(i,i+1)
15        return count