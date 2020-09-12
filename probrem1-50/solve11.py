class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_water = 0
        while True:
            if right == left:
                break
            w_h =  min(height[left], height[right])
            w_w = right - left
            if max_water < w_h*w_w:
                max_water = w_h*w_w
            if w_h == height[left]:
                left += 1
            else:
                right -= 1
        return max_water