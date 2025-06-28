    const randomNum = Math.random();
    console.log(`random number between 0 and 1 is"${randomNum}`);

    const randomint = Math.floor(Math.random()*10)+1;
    console.log(`random number between 1 and 10 is" ${randomint}`);


    let a = "archana"
    let ans = a.toUpperCase();
    console.log(ans);

    for (let i=1; i<=10; i++){
        console.log("for value of i as", i)
    }

    let i = 1
    while(i<=10){
        console.log("using while loop, value of i:",i)
        i++
    }

    const day = "Monday";
switch(day){
    case "Monday":
    console.log("Start of the week!")
     break;
      case "Tuesday" :
    console.log("Its only Tuesday!")
     break;
      case "Friday":
    console.log("Almost the weekend!")
     break;
    default:
    console.log("Its a regular day")
}