Book1 = {
    Name: "Pride and Prejudice",
    Author: "Jane Austen",
    Price: "250rs",
}
Book2 = {
    Name: "Wings of Fire",
    Author: "APJ Abdul Kalam",
    Price: "370rs",
}
Book3 = {
    Name: "The Great Gatsby",
    Author: "F. Scott Fitzgerald",
    Price: "500rs",
}

function printbookdetail(Book1){
    console.log(Book1.Name, "by", Book1.Author ,"is available now only for just", Book1.Price, "Buy Now!")
    console.log(Book2.Name, "by", Book2.Author ,"is available now only for just", Book2.Price, "Buy Now!")
    console.log(Book3.Name, "by", Book3.Author, "is available now only for just", Book3.Price, "Buy Now!")
}

printbookdetail (Book1)
