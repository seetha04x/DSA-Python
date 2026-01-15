#for soln 1:here the concept is similar to turing machine for plaindrome. the copy of string with only lowercase alphanumeric charachters is created into a list.
#left is initialised as starting index and right is placed at the end.
#each charachter is checked for equality and when it evaluates to false, the d=fucntion exits, otherwise the left is incremented and right is decremented 
#for soln 2: a copy of string is created by only adding lowercase alphanumeric charachters
#then using slice operator s[::-1] for reversal is used to check for equality btwn the copy of string and original string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[ch for ch in s.lower() if ch.isalnum()]
        left=0
        right=len(s)-1

        while (left<right):
            if (s[left]==s[right]):
                left+=1
                right-=1
            else:
                return False
        return True            
                
        # text=""
        # s=s.lower()
        # for ch in s:
        # 	if (ch.isalnum()):
        #         text+=ch
        # return (text==text[::-1])   


        