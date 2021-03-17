# an example of Inheritance.
class Dog: # child classes
     owner_name = ""
     age = 0
     health_status = ""
     def bark(self):
       print("Dog is barking...........")

    


class Cat: # child classes
     owner_name = ""
     age = 0
     health_status = ""
     def meow(self):
       print("Cat is meowing.........")


dog1 = Dog()
dog1.bark()

dog1.owner_name = "Tommy"
print(dog1.owner_name)

cat1 = Cat()
cat1.age = 3
cat1.meow()



















