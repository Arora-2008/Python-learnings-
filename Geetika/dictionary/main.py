#x = {
  #  "name" : "geetika" , "age" : 18 , "city" : "garhshankar" , "course" : "btech" , "gender" : "female"
    #}



x = {
    "name" : "geetika" , 
    "age" : 18 , 
    "city" : "garhshankar" , 
    "course" : "btech" , 
    "gender" : "female",
    "marks":{
        "math":2435,
        "science":58
    }
}          


print(x["marks"]["math"]) # acessing the elements of sub dictionary


x["marks"]["math"]=30

print(x["marks"]["math"]) # acessing the elements of sub dictionary
print(x)




x["course"]="B.Tech" 
print(x["course"])
x["course from"]="skillup"

print(x)



print("------------------------------------------------------------")


x.pop("gender")
x["mobile.no"] = 1234456566
print(x)                   





