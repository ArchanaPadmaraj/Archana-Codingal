friends = ["ashika","sarah","meroma","jovita","akhina"]
console.log("my first friend:",friends[3],"and", friends[4])
console.log("my current best friend:", friends[1])
console.log("my most funny friend:", friends[0])
console.log("my most reliable friend:", friends[3])
console.log("my most talented friend friend:", friends[4])
console.log("my coolest friend:", friends[2])

numbers = [4,5,34,30,19,23]
console.log("there are",numbers.length,"numbers in the current array")

numbers.push(37,38,81)
console.log(numbers)
console.log("there are",numbers.length,"numbers in the updated array")

numbers.pop()
console.log(numbers)
console.log("there are now",numbers.length,"numbers in the again updated array")

numbers.pop();
console.log(numbers);

function first(){ 
    console.log("Hi") 
}

function second(){ 
    first()
    console.log("How are you?") 
}

function third(){ 
    second() 
    console.log("Bye") 
}


third() 