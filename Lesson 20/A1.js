function greet(a,b){
    console.log("Hello", a)
    console.log("Hello" , b)
}
greet("Archana" , "Pooja")
// argument - (real value) --> calling, parameter - (not real value )---> defining (replaces a variable with greet variable, while calling is just writing the name in the place where we wrote a)
// it will not work if we write console log a outside the curly bracket, because a is bounded to inside the curly bracket, it is not defined. so always write console log inside curly bracket, or you have to write the function

function sum(a,b){
    return a + b
}
ans=sum(10,20)
console.log(ans)
// this is just a simulation on how to use return, and console. You can use both, granted that console is easier but you should know how to do both 

function difference(a,b){
return a - b
}
result=difference(20,30)
console.log(result)