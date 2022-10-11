#[derive(PartialEq, Debug)]
// Declare Car struct to describe vehicle with four named fields
struct Car {
    color: String,
    motor: Transmission,
    roof: bool,
    age: (Age, u32),
}

#[derive(PartialEq, Debug)]
// Declare enum for Car transmission type
enum Transmission { Manual, SemiAuto, Automatic }

#[derive(PartialEq, Debug)]
enum Age {New, Used}


fn car_quality (miles: u32) -> (Age, u32) {
    if miles > 0 {
        (Age::Used, miles)
    }
    else {
        (Age::New, miles)
    }
}


fn car_factory(color: String, motor: Transmission, roof: bool, miles: u32) -> Car {
    if car_quality(miles).0 == Age::Used {
        if roof {
            println!("Preparing a used car: {:?}, {}, Hard top, {} miles", motor, color, miles);
        } else {
            println!("Preparing a used car: {:?}, {}, Convertible, {} miles", motor, color, miles);
        }
    } else {
        if roof {
            println!("Building a new car: {:?}, {}, Hard top, {} miles", motor, color, miles);
        } else {
            println!("Building a new car: {:?}, {}, Convertible, {} miles", motor, color, miles);
        }
    }

    Car {
        color: color,
        motor: motor,
        roof: roof,
        age: car_quality(miles)
    }
}

fn main() {
    // Create car color array
    let colors = ["Blue", "Green", "Red", "Silver"];

    // Declare the car type and initial values
    let mut car: Car = Car {
        color: colors[0].to_string(),
        motor: Transmission::Manual,
        roof: false,
        age: car_quality(0),
    };
    let mut engine: Transmission = Transmission::Manual;

    // Car order #1: New, Manual, Hard top
    car = car_factory(String::from(colors[0]), engine, true, 0);

    // Car order #2: Used, Semi-automatic, Convertible
    engine = Transmission::SemiAuto;
    car = car_factory(String::from(colors[1]), engine, false, 100);

    // Car order #3: Used, Automatic, Hard top
    engine = Transmission::Automatic;
    car = car_factory(String::from(colors[2]), engine, true, 200);
}