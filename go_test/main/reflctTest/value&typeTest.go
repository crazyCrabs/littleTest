package main

import (
	"fmt"
	"reflect"
	"encoding/json"
	"unsafe"
)

func simpleUse() {
	i := 3
	iv := reflect.ValueOf(i)
	it := reflect.TypeOf(i)
	fmt.Printf("value = %d type = %v\n", iv, it)
}

func getOriginNum() {
	i := 3
	iv := reflect.ValueOf(i)
	i1 := iv.Interface().(int)
	fmt.Println(i1)
}

func setNewNum(originValue int, newValue int64) {
	iv := reflect.ValueOf(&originValue)
	iv.Elem().SetInt(newValue) // 通过Elem拿取变量的地址，通过新值改变
	fmt.Println(originValue)
}

type person struct {
	Name string
	Age  int
}

func setNewStructField(p person, newName string, newAge int64) {
	/* 传递一个 struct 结构体的指针，获取对应的 reflect.Value；
	通过 Elem 方法获取指针指向的值；
	通过 Field 方法获取要修改的字段；
	通过 Set 系列方法修改成对应的值。*/
	ppv := reflect.ValueOf(&p)
	ppv.Elem().Field(0).SetString(newName)
	ppv.Elem().Field(1).SetInt(newAge)
	fmt.Printf("modified person %v\n", p)
}

func (p person) String() string {
	return fmt.Sprintf("Name is %s,Age is %d", p.Name, p.Age)
}

func foreachPersonField(p person) {
	pt := reflect.TypeOf(p)

	for i := 0; i < pt.NumField(); i++ {
		fmt.Println("字段： ", pt.Field(i).Name)
	}
	for i := 0; i < pt.NumMethod(); i++ {
		fmt.Println("字段： ", pt.Method(i).Name)
	}
}

func json2Struct(p person) {
	jsonb, err := json.Marshal(p)
	if err == nil {
		fmt.Println(string(jsonb))
	}

	//json to struct
	respJSON := "{\"Name\":\"李四\",\"Age\":40}"
	json.Unmarshal([]byte(respJSON), &p)
	fmt.Println(p)
}

func (p person) Print(prefix string) {
	fmt.Printf("%s Name: %s, Age id: %d\n", prefix, p.Name, p.Age)
}

func reflectPersonMethod(p person, prefix string) {
	pv := reflect.ValueOf(p)
	mPrint := pv.MethodByName("Print")
	args := []reflect.Value{reflect.ValueOf(prefix)}
	mPrint.Call(args)
}

func main() {
	// ValueOf TypeOf
	simpleUse()

	// 在获取原来的值
	getOriginNum()

	// 用新值替换原来的值
	setNewNum(3, 66)

	// 用反射来修改结构的原始值
	setNewStructField(person{Name: "ltj", Age: 200}, "ltj1", 222)

	// 获取结构体的字段和方法
	foreachPersonField(person{Name: "ltj", Age: 200})

	// json struct 互相转换
	json2Struct(person{"ltj", 20})

	// 反射调用一个对象的方法
	reflectPersonMethod(person{"ltj", 20}, "login: ")
	fmt.Println(unsafe.Sizeof(true))

	fmt.Println(unsafe.Sizeof(int8(0)))

	fmt.Println(unsafe.Sizeof(int16(10)))

	fmt.Println(unsafe.Sizeof(int32(10000000)))

	fmt.Println(unsafe.Sizeof(int64(10000000000000)))

	fmt.Println(unsafe.Sizeof(int(10000000000000000)))

	fmt.Println(unsafe.Sizeof(string("飞雪无情")))

	fmt.Println(unsafe.Sizeof([]string{"飞雪u无情","张三"}))
}
