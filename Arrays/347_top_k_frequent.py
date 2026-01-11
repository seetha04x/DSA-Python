#frequency is counted and stored in dictionary using Counter()
#using freq.items(), the num and count is accessed and pushed to min heap
#whenever more than k elements are (say k=2), ie, when 3 elements are added first element is popped which is the minimum element and 2 element are kept intact ie, the top k frequent elements

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums) 
        heap=[]
        for num, count in freq.items():
            heapq.heappush(heap, (count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count, num in heap]    
                       




        
     