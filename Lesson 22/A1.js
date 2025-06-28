bottle = {
    Brand: "Milton",
    Color: "Blue",
    Capacity: "500ml",
    details: function () {
        console.log(`brand name of bottle : ${this.Brand},its color is ${this.Color} and holds ${this.Capacity}`)
    }
}
console.log("The name of the water bottle is", bottle.Brand)
console.log("The color of the water bottle is", bottle.Color)
console.log("The capacity of the water bottle is", bottle.Capacity)
bottle.details()


Book = {
    Title: "Pride and Prejudice",
    Author: "Jane Austen",
    Price: "200rs",

    details: function () {
        console.log(`the name of the book is ${this.Title}, by ${this.Author} and is now on sale for just ${this.Price}`)
    }
}
Book2 = {
    Title: "Wings of fire",
    Author: "Jane Austen",
    Price: "200rs",

    details: function () {
        console.log(`the name of the book is ${this.Title}, by ${this.Author} and is now on sale for just ${this.Price}`)
    }
}

// definition part 
function printnamedetail(obj) {
    console.log("The name of the book is", obj.Title)
    console.log("The author of the book is", obj.Author)
    console.log("The price of the book is", obj.Price)
}
printnamedetail(Book)

printnamedetail(Book2)