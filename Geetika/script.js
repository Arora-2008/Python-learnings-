info={
    "name":"harpreet kaur",
    "fatherName":"Kuldeep kumar",
    "motherName":"Suman",
    "course":"BCA",
    "rollNo":3236563,
    "collegeName":"GRD College in roper",
    "result":{
        "hindi":56,
        "punjabi":89
    },
    "fees":{
        "ins1":8000
    }
}
console.log(info["result"]["punjabi"])


info["result"]["punjabi"]=0 //updat the pujabi marks
console.log(info["result"]["punjabi"])

info.gender="femaile"// adding new value



delete info["fees"]

console.log(info)





























// name="mahi"
// age=56
// console.log(`my name is ${name}`)

// console.log("my name is", name,"+ my age is", age)


// fn="mahi"
// sn="singh"
// console.log(fn+" "+sn)



