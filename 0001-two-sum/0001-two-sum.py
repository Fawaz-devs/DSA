class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)) :
            diff  =  target - nums[i]
            if diff in memo :
                return [i,memo[diff]]

            memo[nums[i]] = i

        return[]