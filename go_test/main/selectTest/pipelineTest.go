package main

import (
	"fmt"
	"sync"
)

func buy(n int) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for i := 0; i < n; i++ {
			out <- fmt.Sprint("配件", i)
		}
	}()
	return out
}

func build(in <-chan string) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for v := range in {
			out <- fmt.Sprint("组装(", v, ")")
		}
	}()
	return out
}

func pack(in <-chan string) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for v := range in {
			out <- fmt.Sprint("打包(", v, ")")
		}
	}()
	return out
}

func merge(ins ...<-chan string) <-chan string {
	var wg sync.WaitGroup
	out := make(chan string)

	p := func (in<-chan string)  {
		defer wg.Done()
		for v := range in {
			out <- v
		}
	}

	wg.Add(len(ins))

	// 扇入需要启动多个goroutine用于处于多个channel中
	for _, in := range ins {
		go p(in)
	}

	// 等待所有的输入数据ins处理完，在关闭out
	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func main() {
	cos := buy(5)
	out := build(cos)
	res := pack(out)
	for v := range res {
		fmt.Println(v)
	}

	// 扇出扇入模式
	coms := buy(100)
	p1 := build(coms)
	p2 := build(coms)
	p3 := build(coms)
	p := merge(p1, p2, p3)
	packs := pack(p)
	for v := range packs {
		fmt.Println(v)
	}
}
