class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        tre = len(nums)/2

        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
            
            if map[i] > tre:
                return i
        