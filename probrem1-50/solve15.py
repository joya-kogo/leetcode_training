class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and ( nums[i-1] == nums[i] ):
                pass
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j < k and ( nums[j] == nums[j-1] ):
                        j += 1
                    while j < k and ( nums[k] == nums[k+1] ):
                        k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
        return set(ans)