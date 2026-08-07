class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        b = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[b] = nums[i]
                b = b + 1

        for i in range(b, len(nums)):
            nums[i] = 0