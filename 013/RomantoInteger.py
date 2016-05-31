def romanToInt(s):
        l = ['M','D','C','L','X','V','I']
        val = [1000,500,100,50,10,5,1]
        var = {}
        for i in range(0,len(l)):
            var[l[i]] = i,val[i]
        foo = 0
        pos = -1
        for i in range(0,len(s)):
            if pos%2 == 0 and pos == var[s[i]][0]+2:
                foo += var[s[i]][1]
                foo -= var[s[i-1]][1]*2
                pos = -1
            elif pos%2 == 0 and pos == var[s[i]][0]+1:
                foo += var[s[i]][1]
                foo -= var[s[i-1]][1]*2
                pos = -1
            else:
                foo += var[s[i]][1]
                pos = var[s[i]][0]
        return foo