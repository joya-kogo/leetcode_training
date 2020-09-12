class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_ans = 100000
        for i in range(len(nums)-2):
            if i > 0 and ( nums[i-1] == nums[i] ):
                pass
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if abs(min_ans - target) > abs(three_sum - target):
                    min_ans = three_sum
                if nums[i] + nums[j] + nums[k] == target:
                    return (nums[i]+nums[j]+nums[k])
                elif three_sum - target < 0:
                    j += 1
                else:
                    k -= 1
        return min_ans
        