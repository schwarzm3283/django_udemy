# class Dog():
#
#     # CLASS OBJECT ATTRIBUTE
#     species = 'mammal'
#
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog(breed = 'lab', name = 'Sammy')
# # otherdog = Dog(breed = 'huskie')
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)
# # print(otherdog.breed)


# class Animal():
#
#     def __init__(self):
#         print("Animal Created")
#
#     def whoAmI(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating")
#
#
# class Dog(Animal):
#
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
#     def bark(self):
#         print("woof")
#
#
#
#
# myd = Dog()
# myd.whoAmI()
# myd.eat()
# myd.bark()

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

b = Book("Python", "jose", 200)
print(b)
