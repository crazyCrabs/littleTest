package main

import "fmt"

func main() {
/* 定义局部变量 */
	var a int = 100
	var b int= 200

	fmt.Printf("交换前 a 的值 : %d\n", a )
	fmt.Printf("交换前 b 的值 : %d\n", b )

	/* 调用函数用于交换值
	* &a 指向 a 变量的地址
	* &b 指向 b 变量的地址
	*/
	swap(&a, &b);

	fmt.Printf("交换后 a 的值 : %d\n", a )
	fmt.Printf("交换后 b 的值 : %d\n", b )

	// ------分割线------
	fmt.Println("分割线，方法二直接使用类似python的交换")
	var c int = 100
	var d int= 200
	c, d = d, c
 
	fmt.Printf("交换后 c 的值 : %d\n", c )
	fmt.Printf("交换后 d 的值 : %d\n", d )
}

func swap(x *int, y *int) {
	var temp int
	temp = *x /* 保存 x 地址的值 */
	*x = *y /* 将 y 赋值给 x */
	*y = temp /* 将 temp 赋值给 y */
}