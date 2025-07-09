// var - redeclaration (creating a new box) and reassigning
// let - reassigning only --> if you want to use var in curly bracket and if you want to reassign value 
// const 

if(true){
    var a = 10
    var a = 11
    a = 12
    console.log("inside if block:",a)
}
console.log("outside if block:",a)

if(true){
    let a = 10
    a = 12
    console.log("inside if block:",a)
}

if(true){
    const a = 10
    console.log("inside if block:",a)
}
