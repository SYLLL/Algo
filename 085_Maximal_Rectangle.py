class Solution(object):
    def maximalRectangle1(self, matrix):
        #idea is to use cumsum to calculate any rectangle starting from (i,j) top-left to (k,l) bottom-right
        #O(n^4) TLE
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        if m==n==1: return int(matrix[0][0])
        
        cumsum = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                cumsum[i,j] = cumsum[i-1,j] + cumsum[i,j-1] - cumsum[i-1,j-1]  + int(matrix[i][j])
        #area bounded by top-left (i,j) and bottom-right (k,l) inclusive
        maxarea = 0      
        for i in range(m):
            for j in range(n):
                for k in range(i,m):
                    for l in range(j,n):
                        area = cumsum[k,l] + cumsum[i-1,j-1] - cumsum[k,j-1] - cumsum[i-1,l]                     
                        if area == (k-i+1)*(l-j+1):
                            maxarea = max(maxarea, area)
                
        return maxarea
        
 
    def maximalRectangle2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #This solution is built on LC084's solution
        #O(n*m) 112ms
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        prev, maxa = [0]*n, 0
      
        for height in matrix:
            height = [int(height[i])*(1+prev[i]) for i in range(n)]
            prev = height
            maxa = max(self.maxRecArea(height), maxa)
            
        return maxa
    
    
    def maxRecArea(self, height):
        #LeetCode084, O(n) 44ms
        #High level idea is to find the max spread of each bar
        #we can use a stack to store left index
        #and right index is when we see a drop h[i] < h[i-1]
        
        height.append(-1)
        stack, maxa = [-1], 0
        
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                # "<" condition finds the right boundary "i-1" for all bars in the stack
                # left boundary is the index in the stack 
                h = height[stack.pop()]
                l, r = stack[-1], i-1
                w = r-l
                maxa = max(maxa, h*w)           
            else:
                stack.append(i)
        
        height.pop()
        return maxa
