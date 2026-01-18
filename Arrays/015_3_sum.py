#first, the array is sorted so that the two sum logic can be applied-(adding the left end and right end numbers and comparing them)
#for loop is used to traverse each element, and it first checks whether iteration other than first, is same as previous, then that iteration is skipped, it is bcos, if previous iteration is for i=2, then maybe a triplet will be found. then, if in the next iteration i=2 again, the same triplet will be found and appended, which leads to duplication.
#then left and right is assigned and check whether the sum equals using 0,or <0 and >0 (applying two sum logic)
#if sum equals zero, maybe we can find another triplet, so it check whether the next left is same as the current left, if so, the left is incremented to the next one, until different inorder to avoid redudant calculation, same for right too, 
#if left[i]!=left[i+1], then left++ and right-- and it works again to to find new triplet. 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            left,right=i+1, len(nums)-1
            while (left<right):
                total=nums[left]+nums[right]+nums[i]
                if (total==0):
                    res.append([nums[i],nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: 
                        left += 1 
                    while left < right and nums[right] == nums[right-1]: 
                        right -= 1
                    left += 1 
                    right -= 1
    
                elif (total>0):
                    right-=1
                else:
                    left+=1    
        return res

            