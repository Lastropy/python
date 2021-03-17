class Animal: # superclass
     owner_name = ""
     age = 0
     health_status = ""




# an example of Inheritance.
class Dog(Animal): # child classes
     def bark(self):
       print("Dog is barking...........")

    


class Cat(Animal): # child classes
     def meow(self):
       print("Cat is meowing.........")


dog1 = Dog()
dog1.bark()

dog1.owner_name = "Tommy"
print(dog1.owner_name)

cat1 = Cat()
cat1.age = 3
cat1.meow()



















