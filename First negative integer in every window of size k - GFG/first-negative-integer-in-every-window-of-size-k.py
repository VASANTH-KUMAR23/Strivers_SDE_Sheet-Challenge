#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    res = []
    ans = deque()
    j = 0
    i = 0
    while j < N:
        if A[j] < 0:
            ans.append(A[j])
        if j-i+1 < K:
            j += 1
        elif j-i+1 == K:
            if ans:
                res.append(ans[0])
                if A[i] == ans[0]:
                    ans.popleft()
            else:
                res.append(0)
            j += 1
            i += 1
    return res
            
    
    
    '''res = []
    for i in range(N-K+1):
        flag = 0
        for j in range(i,i+K):
            if A[j] < 0:
                res.append(A[j])
                flag = 1
                break
        if flag == 0:
            res.append(0)
    return res'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends