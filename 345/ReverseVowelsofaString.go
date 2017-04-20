
import "strconv"

func reverseVowels(s string) string {
    var stack,ss []byte
    var count = 0
    for i := 0; i < len(s); i++ {
        ss = append(ss,s[i])
        if s[i] == 'a' || s[i] == 'e' || s[i] == 'o' || s[i] == 'i' || s[i] == 'u' ||
           s[i] == 'A' || s[i] == 'E' || s[i] == 'O' || s[i] == 'I' || s[i] == 'U'{
            stack = append(stack,s[i])
            count++
        }
    }
    for i := 0; i < len(s); i++ {
        if s[i] == 'a' || s[i] == 'e' || s[i] == 'o' || s[i] == 'i' || s[i] == 'u' ||
           s[i] == 'A' || s[i] == 'E' || s[i] == 'O' || s[i] == 'I' || s[i] == 'U'{
            ss[i] = stack[count-1]
            count--
        }
    }
    return string(ss)
}