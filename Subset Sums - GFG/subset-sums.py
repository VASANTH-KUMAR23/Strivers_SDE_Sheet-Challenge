#User function Template for python3
class Solution:
    def subsetSums(self, arr, n):
        # code here
        res = []
        
        def subsets_sum(arr,n,sum1,index):
            nonlocal res
            if index>=n:
                res.append(sum1)
                return
            #for not taking first index
            subsets_sum(arr,n,sum1,index+1)
            #for taking first index
            sum1 = sum1+arr[index]
            subsets_sum(arr,n,sum1,index+1)
            sum1 = sum1-arr[index]
            
        subsets_sum(arr,n,0,0)
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