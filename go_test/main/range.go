package main

import "fmt"

func main()  {
	nums := []int{2, 3, 4}
	sum := 0

	// only value
	for _, num := range nums{
		sum += num
	}
	fmt.Println("sum: ", sum)

	// index, value
	for i, num := range nums{
		if num == 3{
			fmt.Println("index: ", i)
		}
	}

	// map key, value
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs{
		fmt.Printf("%s -> %s\n", k, v)
	}

	// string -> unicode
	for i, c := range "go"{
		fmt.Println(i, c)
	}

}