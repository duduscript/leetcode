import "sort"

type pairs [][]int

func (s pairs) Len() int{
    return len(s)
}

func (s pairs) Less(i,j int) bool{
    return s[i][0]<s[j][0]||(s[i][0]==s[j][0]&&s[i][1]<s[j][1])
}

func (s pairs) Swap(i,j int) {
    s[i],s[j] = s[j],s[i]
}

func maxEnvelopes(envelopes [][]int) int {
    table := make([]int,len(envelopes))
    for i := 0; i < len(envelopes); i++ {
        table[i] = 1
    }
    sort.Sort(pairs(envelopes))
    for i := 0; i < len(envelopes); i++ {
        for j := i+1; j < len(envelopes); j++ {
            if envelopes[i][0] < envelopes[j][0] && envelopes[i][1] < envelopes[j][1] && table[j] < table[i]+1{
                table[j] = table[i] + 1
            }
        }
    }
    max := 0
    for i := 0; i < len(table); i++ {
        if max < table[i] {
            max = table[i]
        }
    }
    return max
}