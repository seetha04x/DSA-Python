#created a hashMap using set to store all unique elements.
#the array elements are traversed and if the element is found in hashMap, then duplicate elements exists.
#if not, the element is added to hashMap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash=set()
        for i in nums:
            if i in hash:
                return True
            hash.add(i)    
        return False        
            

            
