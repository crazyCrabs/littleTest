package main

import "fmt"

type Phone interface {
    call(param string) string
    takephoto()
}

type Huawei struct {
}

func (huawei Huawei) call(param string) string{
    fmt.Println("i am Huawei, i can call you!", param)
    return "damon"
}

func (huawei Huawei) takephoto() {
    fmt.Println("i can take a photo for you")
}

func main(){
    var phone Phone
    phone = new(Huawei)
    phone.takephoto()
    r := phone.call("wawajiji")
    fmt.Println(r)
}