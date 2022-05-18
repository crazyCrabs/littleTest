package main

import "fmt"

const MAX int = 3
// 指针数组
func main()  {
	// for循环给指针数组赋值
	a := []int{10, 100, 1000}
	var i int
	var ptr [MAX]*int

	for i=0; i < MAX; i++{
		ptr[i] = &a[i] /*整数地址赋值给指数指针*/
	}

	for i=0; i < MAX;i++{
		fmt.Printf("a[%d]=%d\n", i, *ptr[i])
	}

	fmt.Println("---------------------------------")

	// 使用range遍历给指针数组赋值
	number := [3]int{5, 6, 7}
    var ptrs [3]*int //指针数组
    for i := range number {
        ptrs[i] = &number[i]
    }
    for i, x := range ptrs {
        fmt.Printf("指针数组：索引:%d 值:%d 值的内存地址:%d\n", i, *x, x)
    }
}