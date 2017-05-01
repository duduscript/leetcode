import "container/heap"
type IntHeap [][]int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i][1] > h[j][1] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.([]int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func topKFrequent(nums []int, k int) []int {
    imap := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        imap[nums[i]]++
    }
    hp := &IntHeap{}
    heap.Init(hp)
    for key,value := range imap {
        heap.Push(hp,[]int{key,value})
    }
    var foo []int
    for i := 0; i < k; i++{
        foo = append(foo,heap.Pop(hp).([]int)[0])
    }
    return foo
}