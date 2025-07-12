class Books{
    constructor(name,author,date){
        this.name = name
        this.author = author
        this.date = date
    }
    details(){
        console.log(`The book${this.book} was written by ${this.author} and first published in ${this.date}`)
    }
}

class PAP extends Books{
    details(){
        console.log(`The book${this.book} was written by ${this.author} and first published in ${this.date}`)
    }
}

class TLP extends Books{
    details(){
        console.log(`The book${this.book} was written by ${this.author} and first published in ${this.date}`)
    }
}

class DVC extends Books{
    details(){
        console.log(`The book${this.book} was written by ${this.author} and first published in ${this.date}`)
    }
}

class TAGR extends Books{
    details(){
        console.log(`The book${this.book} was written by ${this.author} and first published in ${this.date}`)
    }
}

const PrideandPrejudice = new PAP ("Pride and Prejudice","Jane Austen","January 28, 1813")
PrideandPrejudice.details()

const Thelittleprince = new TLP ("The Little Prince","J Antoine de Saint-Exupéry","April 6, 1943")
Thelittleprince.details()

const Davinicicode = new DVC ("The Da Vinci Code","Dan Brown ","March 18, 2003")
Davinicicode.details()

const ThinkandGrowRich = new TAGR ("Think and Grow Rich","Napoleon Hill","1937.")
ThinkandGrowRich.details()