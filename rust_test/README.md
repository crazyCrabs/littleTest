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
- 循环使用 loop while for，for可以循环一个范围 `for i in 0..5`,`for i in 0..=5`.如果你想要得到数组，可以使用`vecy[range]`  `vector[0..4]`，`break` 来退出且可以显示的返回一个值
- Option<T>来支持可选的值 Some(T) None
- match关键字来分别指定Some和None的操作，Some(&值)来特定化情况的输出
- if let 可以在没有完整模式的时候简化 match，等同于python中if 跟海象表达式一起使用
- unwrap 默认返回 Some 里的值，如果是 None 将会 panic 并退出程序，expect类似只是返回自定义的错误提示, unwrap_or(T)有值就返回成员，没值就返回T
- Result<T,E>来处理错误的情况 Ok(&T) Err(&T)
- rust作用域与c一致，用{}来定义块级作用域，变量转移以后之前定义的变量就会失效
- 数字类型自带复制属性而字符串，向量或其他复杂类型没有copy特征而是移动
- 在变量前面加上&可以实现变量的借用，但是不能改变原来的值，如果要实现改变原来的值则需要用到&mut
- 'a这样的字符称为生命周期，这个生命周期可以指定该变量的引用不能长于生命周期
- `trait` 在rust中使用trait来定义一组特定方法的行为，这样才能方便的重用其它开发者的代码, `impl Trait for Type` 利用impl来实现trait, 对外界各种类型实现该特殊的方法
- `derive` 派生特征，`Debug`特征运行使用`{:?}`输出.`Display`特征使用`{}`输出，rust会自动根据`std::fmt::Display`按照一定的格式输出值.`PartialEq`用于比较数据是否相等
- 迭代器 `Iterator` 主要实现`next()`方法
- `mod`用来在单个文件中定义模块，`pub`用来指定模块的公共性, 使用`::`符号引用模块
- 箱是编译单元，是 Rust 编译器可以运行的最小代码量。
- `#[test]`添加在函数之前就可以使用`cargo test`来进行单元测试，`#[should_panic]`用来定义测试这个宏应该失败才可以,`#[ignore]`忽略这个测试宏


# 关键字
- fn 定义函数
- let 定义变量，默认不可变
- mut 变量可变