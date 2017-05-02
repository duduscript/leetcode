func countNumbersWithUniqueDigits(n int) int {
    if n == 0 {
        return 1
    }
    bar := 9
    for i := 1; i < n; i++ {
        bar *= (10-i)
    }
    return bar + countNumbersWithUniqueDigits(n-1)
}