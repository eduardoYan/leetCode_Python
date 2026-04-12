1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) -1
5
6        TotalArea=0
7
8        while left < right:
9            largura = right- left
10            minimoAltura = min(height[right],height[left])
11            auxTotalArea = largura * minimoAltura
12
13            TotalArea=max(auxTotalArea, TotalArea)
14
15            if height[left] < height[right]:
16                left += 1
17            else:
18                right -= 1
19
20        return TotalArea        