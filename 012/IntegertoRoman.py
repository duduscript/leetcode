def isnine(pos1,pos2):
   return pos1*5+pos2 == 9
def isfour(pos1,pos2):
    return pos2 == 4
def getstr(num,l,pos):
    if isnine(num[pos],num[pos+1]):
        return l[pos+1] + l[pos-1]
    elif isfour(num[pos],num[pos+1]):
        return l[pos+1] + l[pos]
    else:
       return num[pos]*l[pos] + num[pos+1]*l[pos+1]
class Solution(object):
    def intToRoman(self,s):
        nums = [s/1000,s/500%2,s/100%5,s/50%2,s/10%5,s/5%2,s%5]
        l = ['M','D','C','L','X','V','I']
        return nums[0]*l[0] + getstr(nums,l,1) + getstr(nums,l,3) + getstr(nums,l,5)