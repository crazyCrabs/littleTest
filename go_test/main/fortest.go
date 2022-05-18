package main
import "fmt"
import "strconv"
import "os"

func main(){
    var score int = 0
    var fenshu string = "A"
    student := ""
    fmt.Printf("欢迎进入成绩查询系统\n")
    ZHU: for true{
        var xuanzhe int = 0
        fmt.Println("1.进入成绩查询 2.退出程序")
        fmt.Printf("请输入序号选择:")
        fmt.Scanln(&xuanzhe)
        fmt.Printf("\n")
        if xuanzhe == 1{
             goto CHA
        }
        if xuanzhe == 2{
            os.Exit(1)
        }

    }

    CHA: for true {
        fmt.Printf("请输入学生的姓名：")
        fmt.Scanln(&student)
        fmt.Printf("请输入该学生的成绩:")
        fmt.Scanln(&score)

        switch {
            case score >= 90:fenshu = "A"

            case score >= 80&&score < 90:fenshu = "B"

            case score >= 60&&score < 80:fenshu = "C"

            default: fenshu = "D"
        }

        //fmt.Println(fenshu)
         var c string  = strconv.Itoa(score)
        switch{
            case fenshu == "A":
                fmt.Printf("%s考了%s分,评价为%s,成绩优秀\n",student,c,fenshu)
            case fenshu == "B" || fenshu == "C":
                fmt.Printf("%s考了%s分,评价为%s,成绩良好\n",student,c,fenshu)
            case fenshu == "D":
                fmt.Printf("%s考了%s分,评价为%s,成绩不合格\n",student,c,fenshu)
        }
        fmt.Printf("\n")
        goto ZHU
}
    //fmt.Println(score)
}