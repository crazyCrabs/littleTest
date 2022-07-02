package main

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

type user struct {
	ID   int
	Name string
}

var users = []user{
	{ID: 1, Name: "John"},
	{ID: 2, Name: "Smith"},
	{ID: 3, Name: "Dark"},
	{ID: 4, Name: "Lucky"},
}

func main() {
	r := gin.Default()
	r.GET("/user", listUsers)
	r.GET("/user/:id", getUser)
	r.POST("/user", createUser)
	r.DELETE("/user/:id", deleteUser)
	r.PATCH("/user/:id", patchUser)
	r.Run(":8080")
}

func listUsers(c *gin.Context) {
	c.JSON(200, users)
}

func getUser(c *gin.Context) {
	id := c.Param("id")
	var _user user
	found := false

	for _, v := range users {
		if strings.EqualFold(id, strconv.Itoa(v.ID)) {
			_user = v
			found = true
			break
		}
	}

	if found {
		c.JSON(200, _user)
	} else {
		c.JSON(404, gin.H{
			"message": "用户不存在",
		})
	}
}

func createUser(c *gin.Context) {
	name := c.DefaultPostForm("name", "")
	if name != "" {
		u := user{ID: len(users) + 1, Name: name}
		users = append(users, u)
		c.JSON(http.StatusCreated, users)
	} else {
		c.JSON(http.StatusOK, gin.H{
			"message": "请输入用户名称",
		})
	}
}

func deleteUser(c *gin.Context) {
	id := c.Param("id")
	index := -1
	for i, v := range users {
		if strconv.Itoa(v.ID) == id {
			index = i
			break
		}
	}
	if index > 0 {
		users = append(users[:index], users[index+1:]...)
		c.JSON(http.StatusOK, users)
	} else {
		c.JSON(http.StatusNotFound, gin.H{
			"message": "用户不存在"})
	}
}

func patchUser(c *gin.Context) {
	id := c.Param("id")
	fmt.Println(">>> id: ",id)
	for i, u := range users {
		if strconv.Itoa(u.ID) == id {
			name := c.DefaultPostForm("name", u.Name)
			fmt.Println(">>> name: ",name)
			users[i].Name = name
			fmt.Println(users)
			c.JSON(http.StatusOK, users)
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{
		"message": "用户不存在"})
}
