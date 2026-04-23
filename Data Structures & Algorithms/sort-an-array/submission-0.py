class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]


        s_left = self.sortArray(left)
        s_right = self.sortArray(right)

        sorted_list = []
        cur_l = 0
        cur_r = 0

        while cur_l < len(s_left) and cur_r < len(s_right):
            if s_left[cur_l] < s_right[cur_r]:
                sorted_list.append(s_left[cur_l])
                cur_l += 1
            else:
                sorted_list.append(s_right[cur_r])
                cur_r += 1

        sorted_list.extend(s_left[cur_l:])
        sorted_list.extend(s_right[cur_r:])

        return sorted_list
            