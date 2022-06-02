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

func downloadFile(filename string) string {
	time.Sleep(time.Second)
	return filename+" cc 测试"
}

func main()  {
	// go 并发
	go say("world")
	say("hello")

	fmt.Println("------------------chan 测试-----------------------")
	// 通道 chan
	s := []int{7, 2, 8, -9, 4, 0}
	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c
	fmt.Println("x, y", x, y)

	fmt.Println("----------select 测试----------")
	fistChan := make(chan string)
	secondChan := make(chan string)
	thirdChan := make(chan string)

	go func ()  {
		fistChan <- downloadFile("fist.txt")
	}()

	go func ()  {
		secondChan <- downloadFile("second.txt")
	}()

	go func () {
		thirdChan <- downloadFile("third.txt")
	}()

	select {
		case res := <- fistChan:
			fmt.Println(res)
		case res := <- secondChan:
			fmt.Println(res)
		case res := <- thirdChan:
			fmt.Println(res)
	}

}