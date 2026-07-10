class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i in range(len(nums)) :
            difference  =  target -  nums[i] 
            if difference in memory :
                return [i,memory[difference]]
            memory[nums[i]] = i

