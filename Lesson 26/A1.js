class Laptop{
    constructor(ram,core){
        this.ram= ram
        this.core= core
    }
    details(){
        console.log(`the laptop has ${this.ram} ram with ${this.core} core`)
    }
}
const Lap = new Laptop("8GB","i3")
Lap.details()

class Hp extends Laptop{
    details(){
        console.log(` HP laptop has ${this.ram} ram with ${this.core} core`)
    }
}
// since it is child class, no need to write constructor again since it is extending parent class
class Dell extends Laptop{
     details(){
        console.log(` Dell laptop has ${this.ram} ram with ${this.core} core`)
    }
}

const pavillion = new Hp("8GB","i5")
pavillion.details()

const dell = new Dell("10GB","i7")
dell.details()
