class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = False
        pointer=0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                pointer=i
                break
        if pointer==0:
            return True
        for i in range(pointer+1,n):
            if nums[i]<nums[i-1]:
                return False
        return nums[0]>=nums[-1]
        