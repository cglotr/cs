import "container/heap"

type MedianFinder struct {
	lf *HeapMin
	rg *HeapMin
}

func Constructor() MedianFinder {
	return MedianFinder{
		lf: &HeapMin{},
		rg: &HeapMin{},
	}
}

func (this *MedianFinder) AddNum(num int) {
	if this.lf.Len() < 1 || num <= -(*this.lf)[0] {
		heap.Push(this.lf, -num)
	} else {
		heap.Push(this.rg, num)
	}

	if this.lf.Len() > this.rg.Len()+1 {
		v := -(heap.Pop(this.lf).(int))

		heap.Push(this.rg, v)
	}

	if this.rg.Len() > this.lf.Len() {
		v := heap.Pop(this.rg).(int)

		heap.Push(this.lf, -v)
	}

	return
}

func (this *MedianFinder) FindMedian() float64 {
	if this.lf.Len() > this.rg.Len() {
		return float64(-(*this.lf)[0])
	}

	return float64(-(*this.lf)[0]+(*this.rg)[0]) / 2
}

type HeapMin []int

func (h *HeapMin) Len() int {
	return len(*h)
}

func (h *HeapMin) Less(i, j int) bool {
	return (*h)[i] < (*h)[j]
}

func (h *HeapMin) Swap(i, j int) {
	tmp := (*h)[i]
	(*h)[i] = (*h)[j]
	(*h)[j] = tmp
}

func (h *HeapMin) Push(v any) {
	*h = append(*h, v.(int))
}

func (h *HeapMin) Pop() any {
	old := *h
	v := old[len(*h)-1]
	*h = old[0 : len(*h)-1]
	return v
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
