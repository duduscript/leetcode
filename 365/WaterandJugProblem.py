class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == x or z == y or z == x + y or z == 0:
            return True
        if x == 0 or y == 0:
            return False
        x,y = (y,x) if y<x else (x,y)
        tmp_x,tmp_y = x,y
        while True:
            tmp_y = y*((tmp_x - x - y)/y+1 if (tmp_x-x-y)%y!=0 else (tmp_x-x-y)/y)
            while tmp_x - tmp_y > 0:
                if tmp_x - tmp_y == z:
                    return True
                tmp_y += y
            if tmp_x == tmp_y:
                break
            tmp_x += x
        return False