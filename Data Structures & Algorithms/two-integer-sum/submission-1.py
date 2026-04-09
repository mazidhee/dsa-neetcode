class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 2 <= len(nums) <= 1000:
            pair = {}
            for i in range(len(nums)):
                j = target - nums[i]
                if j not in pair:
                    pair[nums[i]] = i
                else:
                    return [pair[j], i]
        return []

