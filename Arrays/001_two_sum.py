#hash map is created
#enumerate function used to store indices and values of num
#key is found, and the logic is to find the key in the hashmap
#the key is matched to the elements before it,if key is found, the indices(value) are returned 
#if not found the element is added to hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i,n in enumerate(nums):
            key=target-n
            if key in hashMap:
                return [i,hashMap[key]]
            hashMap[n]=i


    
        
