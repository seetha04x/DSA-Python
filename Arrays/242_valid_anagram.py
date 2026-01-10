#created a hashmap usimg dictionary to store an element and its occurrence
#the first string is mapped to the dictionary
#then second string is compared like in a turing machine for palindrome(cancelling out)
#if all are cancelled out(count=0), then the strings are anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        hash={}
        for i in s:
            hash[i]=hash.get(i,0)+1
        for i in t:
            hash[i]=hash.get(i,0)-1    
        for count in hash.values():
            if (count!=0):
                return False
        return True            

        
