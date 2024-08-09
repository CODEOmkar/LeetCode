class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            cur_index = abs(nums[i])
            if nums[cur_index - 1] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[cur_index - 1] = -nums[cur_index - 1]
        return ans
        