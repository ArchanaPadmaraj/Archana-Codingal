// example - callback function 

function sum1(a,b,c){
    console.log(a+b)
    c()
}

function greet(){
    console.log("hello this is callback")
}

sum1(10,20,greet)


// example 2

function sum(a,b){
    console.log(a+b)
}

function calculator(a,b,callback){
    return callback (a, b)
}
calculator(2,3,sum) 