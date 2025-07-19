// standard
function standard (a,b){
    return a + b
    
}
console.log(standard(2,5))

// arrow
const arrowadd = (a,b) => a + b 
console.log(arrowadd(6,5))

// type conversion 
// string to number 

let string = "187"
let num = Number(string)
console.log(num+10)

let number = 30
let string1 = String(number)
console.log(string1 + " is a string")

let bool = false
console.log(Number(bool))

// try and catch -- error message, useful in large data backends
try{
    let json = '{"Name":"Jason"}'
    let user = JSON.parse(json)
    console.log(user.name)

    let invalidJson = '{Name:"Jason"}'
    JSON.parse(invalidJson);
}
catch(error){
console.log("an error has occured that is:", error.message)
}


string = "Hello123"
let regex = /\d/
console.log(regex.test(string))

let string10 = "i love javascript"
let pattern = /javascript/
console.log(pattern.test(string10)) 