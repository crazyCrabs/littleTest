package main

import "fmt"


func main()  {
	// 定义长度的为数组，值传递
	b := [...]int{1,2,3,4,5,6}
	// 未定义长度为且切片
	p := []int{1,2,3,4,5,6}

	shuzu_(b)
	fmt.Println(">>> 数组", b)

	qiepian_(p)
	fmt.Println(">>> 切片", p)
}

func shuzu_(num [6]int) {
	num[0], num[len(num) - 1] = num[len(num) - 1], num[0]
}

func qiepian_(num [] int) {
	num[0], num[len(num) - 1] = num[len(num) - 1], num[0]
}