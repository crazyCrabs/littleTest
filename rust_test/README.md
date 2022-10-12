# 要点
- 每个rs文件中都必须要有main函数
- rustc 编译为可执行文件
- 整数分为i和u,分别代表有符号和无符号
- 浮点数包括f36,f64，默认f64
- 定义字符要注意，char 需要使用单引号，而字符串&str要使用双引号
- 结构和枚举的首字母大写
- 不使用return关键字返回值的时候不能写分号
- 数组同python中的list一致不过大小固定 let a = [5; 5]; [T;size]，索引越界时编译就会报错
- 使用vec!宏来定义矢量，矢量大小可变 let a = vec![5;5]; 索引越界的时候编译不会出错但在运行时候就会报错
- 使用std::collections::HashMap 中的 HasHMap::new()来定义哈希表
- 使用insert方法来添加元素, get方法来获取元素,使用map-like操作insert,HashMap.get(KEY)的话，还没有KEY时会返回None, removes方法移除元素
- 循环使用 loop while for，for可以循环一个范围 for i in 0..5,for i in 0..=5.如果你想要得到数组，可以使用vecy[range]  vector[0..4]，break 来退出且可以显示的返回一个值
- Option<T>来支持可选的值 Some(T) None
- match关键字来分别指定Some和None的操作，Some(&值)来特定化情况的输出
- if let 可以在没有完整模式的时候简化 match，等同于python中if 跟海象表达式一起使用
- unwrap 默认返回 Some 里的值，如果是 None 将会 panic 并退出程序，expect类似只是返回自定义的错误提示, unwrap_or(T)有值就返回成员，没值就返回T
- Result<T,E>来处理错误的情况 Ok(&T) Err(&T)


# 关键字
- fn 定义函数
- let 定义变量，默认不可变
- mut 变量可变