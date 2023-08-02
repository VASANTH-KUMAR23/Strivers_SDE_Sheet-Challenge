#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        def find(step,n,dp):
            if step == n:
                return 1
            if step > n:
                return 0
            if dp[step] != -1:
                return dp[step]
            dp[step] = (find(step+1,n,dp) + find(step+2,n,dp) + find(step+3,n,dp))%1000000007
            return dp[step]
        
        dp = [-1]*(n+3)
        #dp[n] = 1
        #dp[n+1] = 0
        #dp[n+2] = 0
        return find(0,n,dp)
        
        
        #using recursion
        '''def find(step,n):
            if step == n:
                return 1
            if step > n:
                return 0
            return find(step+1,n) + find(step+2,n) + find(step+3,n)
        return find(0,n)'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends