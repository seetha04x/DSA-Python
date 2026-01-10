class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i,n in enumerate(nums):
            key=target-n
            if key in hashMap:
                return [i,hashMap[key]]
            hashMap[n]=i


    
        