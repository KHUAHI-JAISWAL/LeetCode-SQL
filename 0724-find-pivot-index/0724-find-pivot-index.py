class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        #Brute Force: in every index find  sum of left and right side after then chenk both are equal or not

        # Best Approach — Prefix Sum (time -o(n) and space o(1))
        

        
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
        