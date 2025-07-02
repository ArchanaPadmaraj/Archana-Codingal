// array
names = ["archana","pooja","sarah","ashika"] 

// fetching values 
console.log("the best in math:",names[0])
console.log("the best in biology:",names[1])
console.log("the best in english:",names[3])
console.log("the best in geography:",names[2])

// changing value 
names[0]="achu"
console.log("the updated array is",names)

numbers = [10,20,30,40]
console.log("total numbers in the array is", numbers.length)

// to add numbers
numbers.push(34);
console.log(numbers);

// only removes last element
numbers.pop();
console.log(numbers);

function first(){ //6
    console.log("First Hello") //7
}

function second(){ //4
    first() //5 //8
    console.log("Second Hello") //9
}

function third(){ //2
    second() //3 //10
    console.log("Third Hello") //11
}


third() //1 //12
