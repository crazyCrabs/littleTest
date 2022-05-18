package main

import "fmt"

func main()  {
	var countryMap map[string]string
	countryMap = make(map[string]string)

	countryMap[ "France" ] = "巴黎"
    countryMap[ "Italy" ] = "罗马"
    countryMap[ "Japan" ] = "东京"
    countryMap[ "India " ] = "新德里"

	for country := range countryMap{
		fmt.Println(country, "首都是", countryMap[country])
	}

	capital, ok := countryMap["china"]
	if(ok) {
		fmt.Println(capital)
	} else {
		fmt.Println("not found")
	}

	// delete member
	delete(countryMap, "Japan")
	fmt.Println("删除后")
	for country := range countryMap{
		fmt.Println(country, "首都是", countryMap[country])
	}

}