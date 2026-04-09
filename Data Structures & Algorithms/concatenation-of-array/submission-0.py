class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # the number/length of the array is unknown
        #I am to create an array that is twice the length of the input array
        # the first thought process i have is to append the list to the end of the input list

        ans = []
        for n in nums:
            ans.append(n)

         # a better method would be to extend the list instead
        ans.extend(nums)
        return ans
        
        