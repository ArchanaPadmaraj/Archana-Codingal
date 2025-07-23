let a = new Promise((res,rej)=>{
    if(true){
        res("your request has been accepted")
    }
    else{
        rej("your request has been denied")
    }
})
a.then((data)=>console.log(data))
.catch((err)=>console.log(err))