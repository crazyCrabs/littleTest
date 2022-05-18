package main

import "fmt"

func main()  {
	add_func := add(1,2)
	fmt.Println(add_func())
	fmt.Println(add_func())
	fmt.Println(add_func())

	fmt.Println("***********************")
	add1_func := add1(1, 2)
	fmt.Println(add1_func(1, 1))
	fmt.Println(add1_func(0, 0))
	fmt.Println(add1_func(2, 2))

	fmt.Println("***********************")
	add2_func := add2(1, 2)
	fmt.Println(add2_func(1, 1))
	fmt.Println(add2_func(0, 0))
	fmt.Println(add2_func(2, 2))
}

func add(x1, x2 int) func ()(int, int)  {
	i := 0
	return func() (int, int)  {
		i++
		return i, x1+x2
	}
}

// 闭包中带参数
func add1(x1, x2 int) func(x3, x4 int)(int, int, int) {
	i := 0
	return func(x3, x4 int)(int, int, int)  {
		i++
		return i, x1+x2, x3+x4
	}
}

func add2(x1, x2 int) func(int, int)(int, int, int)  {
	i := 0
	return func(x3, x4 int)(int, int, int)  {
		i++
		return i, x1+x2, x3+x4
	}
}