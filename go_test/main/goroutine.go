package main

import (
	"fmt"
	"time"
)


func say(s string)  {
	fmt.Println(time.Millisecond)
	fmt.Printf("%d\n", time.Millisecond)
	for i:=0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func sum(s []int, c chan int)  {
	sum := 0
	for _, v := range s {
		sum += v
	}
	c <- sum // 把值发送到通道
}

func main()  {
	// go 并发
	go say("world")
	say("hello")

	// 通道 chan
	s := []int{7, 2, 8, -9, 4, 0}
	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c
	fmt.Println("x, y", x, y)
}