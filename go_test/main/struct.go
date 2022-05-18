package main

import "fmt"

// 首字母大写相当于 public
// 首字母小写相当于 private
type Books struct {
	title string
	author string
	subject string
	book_id int
}

func change_title(book *Books, title string)  {
	book.title = title
}

// 结构体作为参数为值传递
func main()  {
	fmt.Println(Books{"go", "go", "go", 1})
	fmt.Println(Books{title: "go", author: "go", subject: "go", book_id: 1})
	fmt.Println(Books{title: "go", author: "go"})

	var book1 Books
	var book2 Books

	book1.title = "go 1"
	book1.author = "----"
	book1.subject = "xxxx"
	book1.book_id = 1

	book2.title = "go 2"
	book2.author = "----"
	book2.subject = "xxxx"

	fmt.Println("book1", book1)
	fmt.Println("book2", book2)

	// 把结构体当做参数
	change_title(&book1, "wawaawa")
	fmt.Println("修改title之后的book1", book1)
}