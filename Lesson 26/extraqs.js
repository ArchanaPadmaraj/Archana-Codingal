class Car{
    constructor(color, model){
        this.color = color
        this.model = model 
    }
    start(){
        console.log("vroom vroom")
    }
    stop(){
        console.log("stopped")
    }
    details(){
        console.log(`the color of the car is ${this.color} and is the the ${this.model} model `)
    }
}
const Porsche = new Car("Black","Porsche 911 Turbo S")
Porsche.details()

class BMW extends Car{
    details(){
        console.log(`the color of the car is ${this.color} and is the ${this.model} model`)
    }
}

class Mercedes extends Car{
    details(){
        console.log(`the color of the car is ${this.color} and is the ${this.model} model`)
    }
}

const bmw = new BMW("Red","BMW M4 Coupe")
bmw.details()
bmw.start()
bmw.stop()

const mercedes = new Mercedes("White","E-Class Sedan")
mercedes.details()
mercedes.start()
mercedes.stop()

