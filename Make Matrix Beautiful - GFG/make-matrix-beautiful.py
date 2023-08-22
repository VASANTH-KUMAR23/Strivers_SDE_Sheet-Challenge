#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        sum_row = [0]*n
        col_sum = [0]*n
        temp = 0
        
        for i in range(n):
            for j in range(n):
                sum_row[i] += matrix[i][j]
                col_sum[i] += matrix[j][i]
            if temp < col_sum[i] or temp < sum_row[i]:
                temp = max(col_sum[i],sum_row[i])
        
        ans = 0
        for i in range(n):
            ans += temp-col_sum[i]
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends