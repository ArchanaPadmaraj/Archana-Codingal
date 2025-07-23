const student = {
    name: "student",
    age: 15,
    subjects: ["Math","Science"]
}

const JSONstudentstring = JSON.stringify(student)
console.log("JSON format:",JSONstudentstring)

const JSONstudentobject = JSON.parse(JSONstudentstring)
console.log("object form:", JSONstudentobject)