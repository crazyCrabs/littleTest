package main

import "fmt"

func main() {
   var numbers []int
   printSlice("初始化 numbers: ", numbers)
   
   /* 允许追加空切片 */
   numbers = append(numbers, 0)
   printSlice("增加0 numbers: ", numbers)
   
   /* 向切片添加一个元素 */
   numbers = append(numbers, 1)
   printSlice("增加1 numbers: ", numbers)
   
   /* 同时添加多个元素 */
   numbers = append(numbers, 2,3,4)
   printSlice("增加多个元素 numbers: ", numbers)

   /* 创建切片 numbers1 是之前切片的两倍容量*/
   numbers1 := make([]int, len(numbers), (cap(numbers))*2)

   /* 拷贝 numbers 的内容到 numbers1 */
   copy(numbers1,numbers)
   printSlice("拷贝numbers的numbers1: ", numbers1)  
}

func printSlice(info string, x []int){
   fmt.Printf(info+"len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}