package main

import (
	"fmt"
	"time"
)

func washVegetables() <-chan string {
	out := make(chan string)
	go func() {
		time.Sleep(5 * time.Second)
		out <- "蔬菜洗好了"
	}()
	return out
}

func boilWater() <-chan string {
	out := make(chan string)
	go func() {
		time.Sleep(5 * time.Second)
		out <- "水煮开了"
	}()
	return out
}

func main() {
	vegetableCh := washVegetables()
	waterCh := boilWater()
	fmt.Println("休息会儿，等蔬菜和水煮开了")
	time.Sleep(2 * time.Second)
	vegetables := <-vegetableCh
	water := <-waterCh
	fmt.Println("蔬菜和水煮开了，开始烹饪", vegetables, water)
}
