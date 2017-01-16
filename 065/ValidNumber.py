class Solution(object):
    def zero(self, s):
        if len(s) == 0:
            return False
        elif s.startswith('.'):
            return self.two(s[1:],0)
        elif s[0].isdigit():
            return self.one(s[1:])
        else:
            return False
    def one(self, s):
        if len(s) == 0:
            return True
        elif s[0].isdigit():
            return self.one(s[1:])
        elif s.startswith('e'):
            return self.four(s[1:])
        elif s.startswith('.'):
            return self.two(s[1:],1)
        else:
            return False
    def two(self, s, frm):
        if len(s) == 0:
            return frm == 1
        elif s[0].isdigit():
            return self.three(s[1:])
        elif s.startswith('e') and frm == 1:
            return self.four(s[1:])
        else:
            return False
    def three(self, s):
        if len(s) == 0:
            return True
        elif s[0].isdigit():
            return self.three(s[1:])
        elif s.startswith('e'):
            return self.four(s[1:])
        else:
            return False
    def four(self, s):
        if len(s) == 0:
            return False
        elif s[0].isdigit():
            return self.five(s[1:])
        elif s.startswith('-') or s.startswith('+'):
            return self.six(s[1:])
        else:
            return False
    def five(self, s):
        if len(s) == 0:
            return True
        elif s[0].isdigit():
            return self.five(s[1:])
        else:
            return False
    def six(self, s):
        if len(s) != 0 and s[0].isdigit():
            return self.five(s[1:])
        else:
            return False
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or s == '.':
            return False
        elif s[0] == ' ':
            return self.isNumber(s[1:])
        elif s[-1] == ' ':
            return self.isNumber(s[:-1])
        elif s.startswith('-') or s.startswith('+'):
            return self.zero(s[1:])
        elif s[0].isdigit():
            return self.one(s[1:])
        elif s.startswith('.'):
            return self.two(s[1:],-1)
        else:
            return False