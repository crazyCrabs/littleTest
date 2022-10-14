pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    }
    a / b
}

pub fn sub(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic]
    fn it_works() {
        let result = div(10, 2);
        assert_eq!(result, 5);

        let result = div(6, 3);
        assert_eq!(result, 2);

        let result = div(10, 0);
        assert_eq!(result, 2);
    }

    #[test]
    fn sub_test(){
        assert_eq!(sub(9, 2), 7);
        assert_eq!(sub(6, 9), -3);
    }
}
