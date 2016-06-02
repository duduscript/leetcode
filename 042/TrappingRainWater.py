def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area = 0
    size = len(height)
    if size < 2:
        return 0
    maxHeightRight = [[0,0]] * size
    maxHeightLeft = [[0,0]]*size
    maxHeightRight[-1] = size,0
    rev = range(0, size-1)[::-1]
    for i in rev:
        if maxHeightRight[i+1][1] <= height[i+1]:
            maxHeightRight[i] = i+1,height[i+1]
        else:
            maxHeightRight[i] = maxHeightRight[i+1]
    rev = range(1,size)
    maxHeightLeft[0] = -1,0
    for i in rev:
        if maxHeightLeft[i-1][1] < height[i-1]:
            maxHeightLeft[i] = i-1,height[i-1]
        else:
            maxHeightLeft[i] = maxHeightLeft[i-1]
    for i in range(0,size):
        if maxHeightLeft[i][1] > height[i] and maxHeightRight[i][1] > height[i]:
            area += min(maxHeightRight[i][1] , maxHeightLeft[i][1]) - height[i]
    return area
