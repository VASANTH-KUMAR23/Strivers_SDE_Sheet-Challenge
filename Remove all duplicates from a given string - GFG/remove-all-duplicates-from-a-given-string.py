#User function Template for python3
class Solution:
	def removeDuplicates(self,str):
	    # code here
	    hash = {}
	    temp = ''
	    for char in str:
	        if not hash.get(char,False):
	            temp += char
	            hash[char] = True
	    return temp
	    
	    '''for i in str:
	        if i in hash:
	            hash[i] += 1
	        else:
	            hash[i] = 1
	    #print(hash)
	    res = ''
	    for key,value in hash.items():
	        res += key
	    return res'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends