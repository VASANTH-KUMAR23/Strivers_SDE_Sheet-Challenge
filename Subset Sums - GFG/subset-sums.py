#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
	    def find(sum1,ind,res):
		    if ind == N:
		        res.append(sum1)
		        return 
		    find(sum1+arr[ind],ind+1,res)
		    find(sum1,ind+1,res)
		    
		 
	    res = []
		find(0,0,res)
		res.sort()
		return res
		    
	
		
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends