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
    def __init__ (self,profession):
        self.profession=profession

class child(parent):
    def __init__ (self,behaviour,interest,profession):
        super().__init__(profession)
        self.behaviour=behaviour
        self.interest=interest


geetika=child("soft","singing","Doctor")
print(geetika.interest)
print(geetika.behaviour)
print(geetika.profession)