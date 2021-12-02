# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : I referred to the video


# Your code here along with comments explaining your approach
'''
Approach:
1. Maintain a count and a running-sum table.
2. Create hashmap with key of unique r-sum and the value is the count of that r-sum.
3. Add the r-sum base case in the hashmap {0: 1} 
4. iterate the rSum table. 
4.1 For each value, calculate rSum - k, if (rSum - k) is not in hashmap, add the rSum value to hashmap with the count 1, if rsum value already in hashmap, increment the count value by 1
4.2 If (rSum - k) is already in hashmap, increase the count with with value of rsum in hashmap, and add the rSum value into hashmap
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #base cases
        if nums == None or len(nums) == 0: return -1
        
        hashMap = {}
        rSum, count = 0, 0
        
        #r-sum base case
        hashMap[0] = 1
        
        #create r-sum table
        for i in range(len(nums)):
            #r-sum table
            rSum += nums[i]
            
            if (rSum - k) in hashMap:
                count += hashMap[rSum - k]
            
            if rSum in hashMap:
                hashMap[rSum] += 1
            else:
                hashMap[rSum] = 1
            
        return count
