class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x,y = 0,len(height)-1
        MAX = 0
        while x != y:
            MAX = max(MAX,min(height[x],height[y])*(y-x))
            if height[x] < height[y]:
                x += 1
            else:
                y -= 1
        return MAX