# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        total_sum = sum(A)
        prefix_sum = 0
        for i in range(N):
            total_sum -= A[i]
            if prefix_sum == total_sum:
                return i+1
            prefix_sum += A[i]
        return -1
        '''for i in range(N):
            sum1 = 0
            sum2 = 0
            for j in range(i):
                sum1 += A[j]
            for k in range(i+1,N):
                sum2 += A[k]
            if sum1 == sum2:
                return i+1
        return -1'''
            



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends