package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(5)

	// select + chan 来实现让携程退出
	stopCh := make(chan bool)
	go func() {
		defer wg.Done()
		watchDog(stopCh, "【监控dog】")
	}()
	time.Sleep(time.Second * 5)
	stopCh <- true
	// wg.Wait()

	// Context来实现携程退出
	ctx, _ := context.WithCancel(context.Background())

	// 测试多context
	ctx2, stop2 := context.WithCancel(ctx)
	ctx3, stop3 :=context.WithCancel(ctx)

	go func() {
		defer wg.Done()
		watchDogWithContext(ctx, "【Context监控bird】")
	}()

	go func() {
		defer wg.Done()
		watchDogWithContext(ctx2, "【Context监控bird2】")
	}()

	go func() {
		defer wg.Done()
		watchDogWithContext(ctx3, "【Context监控bird3】")
	}()

	// 测试Context的值传递
	valContext := context.WithValue(ctx2, "userId", "123")
	go func() {
		defer wg.Done()
		getUser(valContext)
	}()

	time.Sleep(time.Second * 5)
	// stop() // 发出停止指令
	stop2()
	stop3()
	wg.Wait()
}

func watchDog(stopCh chan bool, name string) {
	// for 开启死循环
	for {
		select {
		case <-stopCh:
			fmt.Println(name, "接收到停止信息，stopping")
			return
		default:
			fmt.Println(name, "正在监控。。。")
		}
		time.Sleep(time.Second)
	}
}

func watchDogWithContext(ctx context.Context, name string) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println(name, "即将停止")
			return
		default:
			fmt.Println(name, "正在监控")
		}
		time.Sleep(time.Second)
	}
}

func getUser(ctx context.Context) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println("用户信息已经获取完成，携程退出")
			return
		default:
			userId := ctx.Value("userId")
			fmt.Println("【获取用户】， 用户id：", userId)
		}
		time.Sleep(time.Second)
	}
}
