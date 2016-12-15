class Solution(object):
    def split_num(self, num):
        if len(num) <= 3:
            return [int(num)]
        else:
            return [int(num[-3:])]+self.split_num(num[:-3])
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:return "Zero"
        nums,eng = self.split_num(str(num)),[]
        ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        ten2twenty = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        for i in range(len(nums))[::-1]:
            rtn = []
            hundred,ten,one = nums[i]/100,(nums[i]%100)/10,nums[i]%10
            if hundred:rtn += [ones[hundred],'Hundred']
            if ten == 1:
                rtn += [ten2twenty[one]]
            else:
                if ten != 0:rtn += [tens[ten]]
                if one != 0:rtn += [ones[one]]
            if rtn != [] and i != 0:
                rtn += [thousands[i]]
            if rtn != []:
                eng.append(' '.join(rtn))
        return ' '.join(eng)