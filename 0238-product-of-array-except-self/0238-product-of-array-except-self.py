class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        answer = [1] * n

        # Left / Prefix product
        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix = prefix * nums[i]

        # Right / Suffix product
        suffix = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]

        return answer
        