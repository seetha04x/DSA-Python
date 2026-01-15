#for soln 1: binary search algorithm is used to reduce the search array and find the key element with respect to difference.
#for soln 2: here, it is like a turing machine too. The left end and right end element is added and it is compared with the target element.
#since, the array is sorted, if the sum is less than target the left index is incremented to increase the sum and if sum>target, the right pointer is decremented
#finally, the sum equals the target and the indices are returned based 1-indexing.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for i in range(len(numbers)):
        #     key=target-numbers[i]
        #     left,right=i+1,len(numbers)-1

        #     while (left<=right):
        #         mid=(left+right)//2
        #         if (numbers[mid]<key):
        #             left=mid+1
        #         elif (numbers[mid]>key):
        #             right=mid-1
        #         else:
        #             return [i+1, mid+1] 
        left,right=0,len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum<target:
                left+=1
            elif sum>target:
                right-=1
            else:
                return [left+1, right+1]



            