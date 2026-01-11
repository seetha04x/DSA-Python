#the logic is  to multiply the array of left products and right products
#a left array is created and using for loop, each position i stores the product of numbers before it (product =product*num[i])
#for right product, the for loop is reversed and the products are found(product of numbers after it) which are directly multiplied with left array
#the left array is then returned
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        product1=1
        for i in range(len(nums)):
            left.append(product1) 
            product1*=nums[i]           
        product2=1
        for i in range(len(nums)-1,-1,-1):         
                left[i]*=product2
                product2*=nums[i]

        return left             
                              
        