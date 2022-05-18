package main

import "fmt"

func Factorial(n int) int {
	if n < 2 {
		return n
	}
	return Factorial(n-2) + Factorial(n-1)
}

func main()  {
	var i int
	for i=0;i<10;i++ {
		fmt.Printf("%d\t", Factorial(i))
	}
}