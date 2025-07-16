let numbers1= [12,34,4,5,19];
numbers1.sort((a,b)=> a - b);  //always write arrow function
console.log("The numbers in ascending order are:",numbers1);

let numbers2 = [23,66,18,29,13]
numbers2.sort((a,b)=> b - a)
console.log("The numbers in descending order are:",numbers2)

let alphabets1 = ["a","b","c","d","k","p","j"]
alphabets1.sort()
console.log("The alphabets in ascending order are:",alphabets1)

let alphabets2 = ["a","b","k","u","r","q","p"]
alphabets2.sort((a,b)=>a.localeCompare.b)
console.log("The alphabets in descending order are:",alphabets2)

// mapping example
let numbers3=[1,2,3,4,5]
let ans = numbers3.map((num)=> num * 2)
console.log(ans)

// questions

let numbers4 = [1,2,3,4,5]
let ans4 = numbers4.map((num)=> num*num)
console.log(ans4)

let numbers5 = [1,2,3,4,5]
let ans5 = numbers5.map((num)=>num+10)
console.log(ans5)
































































// also a way to do so
// let alphabets2 = ["a","b","k","u","r","q","p"]
// alphabets2.reverse()
// console.log("The alphabets in descending order are:",alphabets2)