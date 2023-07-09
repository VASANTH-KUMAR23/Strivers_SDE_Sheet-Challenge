# User function Template for Python3
import math
class Solution:
    def heapHeight(self, N, arr):
        # code here
        return math.ceil(math.log2(N+1))-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.heapHeight(N, arr))

# } Driver Code Ends