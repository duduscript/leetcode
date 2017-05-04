import "sort"

func coinChange(coins []int, amount int) int {
    if amount == 0 {return 0}
    table := make([]int,amount+1)
    for i := 1; i <= amount; i++ {
        table[i] = 2<<31-1
        for j := 0; j < len(coins); j++ {
            if i - coins[j] >= 0 && table[i-coins[j]] + 1 < table[i] {
                table[i] = table[i-coins[j]] + 1
            }
        }
    }
    if table[amount] == 2<<31-1 { return -1 }
    return table[amount]
}