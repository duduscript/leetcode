func isPerfectSquare(num int) bool {
    var l,r int
    l = 1
    r = num+1
    for l < r {
        mid := (l+r)/2
        if mid*mid > num {
            r = mid
        } else if mid*mid < num {
            l = mid+1
        } else {
            return true
        }
    }
    return false
}