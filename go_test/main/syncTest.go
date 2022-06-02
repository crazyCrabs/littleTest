package main

import (
	"fmt"
	"sync"
	"time"
)

var sum = 0

// var mutex = sync.Mutex{}
// var rMutex = sync.RWMutex{}
var mutex sync.Mutex
var rMutex sync.RWMutex

func add(i int) {
	mutex.Lock()
	defer mutex.Unlock()
	sum += i
}

func readNum() int {
	rMutex.RLock()
	defer rMutex.RUnlock()
	b := sum
	return b
}

func run() {
	var wg sync.WaitGroup
	wg.Add(110)

	for i := 0; i < 100; i++ {
		go func() {
			// 计数器减一
			defer wg.Done()
			add(10)
		}()
	}

	for i := 0; i < 10; i++ {
		go func() {
			defer wg.Done()
			fmt.Println(i, " 和为：", readNum())
		}()
	}
	// 等待计数器为0
	wg.Wait()
}

func doOnce() {
	var one sync.Once
	onceBody := func() {
		fmt.Println("do once")
	}
	done := make(chan bool)
	for i := 0; i < 10; i++ {
		go func() {
			one.Do(onceBody)
			done <- true
		}()
	}
	for i := 0; i < 10; i++ {
		<-done
	}
}

func race() {
	cond := sync.NewCond(&sync.Mutex{})
	var wg sync.WaitGroup
	wg.Add(11)
	for i := 0; i < 10; i++ {
		go func(num int) {
			defer wg.Done()
			fmt.Println(num, "号已经准备就绪")
			cond.L.Lock()
			cond.Wait()
			fmt.Println(num, "号已经开始跑了。。。")
			cond.L.Unlock()
		}(i)
	}

	// 等到所有的子线程都准备好了
	time.Sleep(2 * time.Second)
	go func() {
		defer wg.Done()
		fmt.Println("裁判已经就位,准备发令")
		fmt.Println("比赛开始，开始跑步")
		// Signal，唤醒一个等待时间最长的协程
		// Broadcast，唤醒所有等待的协程。
		cond.Broadcast()
	}()

	wg.Wait()
}

func main() {
	// // 直接使用sleep来等待子线程完成任务 不友好
	// for i := 0; i < 100; i++ {
	// 	go add(10)
	// }

	// for i := 0; i < 10; i++ {
	// 	go fmt.Println(i, " 和为：", readNum())
	// }
	// time.Sleep(2 * time.Second)
	// fmt.Println("和为：", sum)

	// 使用sync.WaitGroup来优化sleep时间
	run()
	fmt.Println(time.Second)

	// Once test
	fmt.Println(">>>> do once test")
	doOnce()

	// NewCond test
	fmt.Println(">>>> cond test")
	race()
}
