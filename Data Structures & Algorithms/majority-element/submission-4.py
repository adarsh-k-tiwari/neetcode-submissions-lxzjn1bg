class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key = nums[0]
        count = 0

        for num in nums:
            if count == 0 and num != key:
                count += 1
                key = num
            elif num == key:
                count += 1
            else:
                count -= 1
        
        return key