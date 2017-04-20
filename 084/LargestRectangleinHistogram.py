class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack,rtn = [],0
        heights.append(0)
        for i in xrange(len(heights)):
            while len(stack) and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                w = i - stack[-1] - 1 if len(stack) else i
                rtn = max(rtn,w*heights[tmp])
            stack.append(i)
        return rtn