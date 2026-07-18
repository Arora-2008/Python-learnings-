# data={ "student1":{"name":"geetika","course":"B.tech"} 
#       , "student2":{"name":"riya","course":"B.sc"} , "student3":{"name":"siya","course":"M.sc"} , "student4":{"name":"rohan","course":"B.A"} , "student5":{"name":"rohit","course":"M.A"} }
# print(data)
# with open ("data.txt","w") as d:
#     d.write([data])
# mahi={
#     "name":"mahi singh",
#     "course":"BTECH",
#     "gender":"male"
# }
# geetika={
#     "name":"geetika arora",
#     "course":"BTECH",
#     "gender":"female"
# }
# riya={
#    "name":"riya grover",
#     "course":"BTECH",
#     "gender":"female"
# }
# siya={
#     "name":"siya",
#     "course":"BTECH",
#     "gender":"female"
# }
# rohan={
#     "name":"rohan singh",
#     "course":"M.A",
#     "gender":"male"
# }

# print(data)
# with open ("data.txt","w") as x:
#     x.write(data)

class BTECH:
    course="BTECH"
    university="LPU"


    def __init__ (self,gender,name,rollno):
        self.gender=gender
        self.name=name
        self.rollno=rollno







mahi=BTECH("male","mahi singh",12)
riya=BTECH("female","riya grover",46)

print(mahi.rollno)





# mahi=BTECH()
# geetika=BTECH()


# print(mahi.course)



















# class cars:
#     noOfWeels=4
#     Fule="Pertrol"
#     Origion="India"
#     Safty="5 Star"


# class Mahindra (cars):
#     brandName="Mahindra"
#     def __init__(self, Capacity, Milage, colour):
#         self.Capacity=Capacity
#         self.Milage=Milage
#         self.colour=colour

# class Tata (cars):
#     brandName="Tata"
#     def __init__(self, Capacity, Milage, colour):
#         self.Capacity=Capacity
#         self.Milage=Milage
#         self.colour=colour

# thar=Mahindra("4 lok",50,"Red")

# print(thar.colour)






















# class father:
#     support="infinty"
#     def output (slef):
#         print("hi")

# class child(father):
#     pass


# mahi=child()
# print(mahi.support)
# mahi.output()


















# class father:
#     def language(slef):
#         print("pujabi")
    

# class mother:
#      def language(slef):
#         print("English")


# class child (mother,father):
#     pass


# mahi=child()
# mahi.language()








class parent :
    def __init__ (self,behaviour,profession):
        self.behaviour=behaviour
        self.profession=profession

class child(parent):
    def __init__ (self,behaviour,interest):
        self.behaviour=behaviour
        self.interest=interest


geetika=child("soft","singing")
print(geetika.interest)
print(geetika.behaviour)