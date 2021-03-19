import datetime
from pytz import timezone
import json
import re


class Animal: # superclass
     owner_name = ""
     age = 0
     health_status = ""
     def __init__(self, owner_name, age, health_status):
       self.owner_name = owner_name
       self.age = age
       self.health_status = health_status




# an example of Inheritance.
class Dog(Animal): # child classes
     def bark(self):
       print("Dog is barking...........")
     def __init__(self, dog_name, owner_name,age, health_status):
       Animal.__init__(self, owner_name, age, health_status)
       self.dog_name = dog_name

    


class Cat(Animal): # child classes
     def meow(self):
       print("Cat is meowing.........")
     def __init__(self, owner_name,age, health_status):
       Animal.__init__(self, owner_name, age, health_status)

'''
dog1 = Dog()
dog1.bark()

dog1.owner_name = "Tommy"
print(dog1.owner_name)

cat1 = Cat()
cat1.age = 3
cat1.meow()

'''

datetime_UTC = datetime.datetime.now()
datetime_america = datetime_UTC.astimezone(timezone('America/Los_Angeles'))
print(datetime_america)

dog1 = Dog("Buddy","Sami",1,"good")
print(dog1.owner_name, dog1.dog_name, dog1.age, dog1.health_status)
dog1.bark()

cat1 = Cat("Ellen", 5, "good")
print(cat1.owner_name, cat1.age, cat1.health_status)
cat1.meow()

## websites send each other data.
## format -> JSON
## format for storing and exchanging data

azure_login_JSON = '''[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "d0a26d55-d508-4924-ba9d-8f93f8c166f1",
    "id": "a9928a73-3dce-405e-b553-5f8d0491c60e",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Azure for Students",
    "state": "Enabled",
    "tenantId": "d0a26d55-d508-4924-ba9d-8f93f8c166f1",
    "user": {
      "name": "19UCS040@lnmiit.ac.in",
      "type": "user"
    }
  }
]
## JSON -> PYTHON DICT
loaded_data = json.loads(azure_login_JSON)
print(loaded_data[0]["name"])


## PYTHON DICT -> JSON
new_dict = {
  "name" : "Sami",
  "age" : 13,
  "country" : "US"
}
print(new_dict)
dumped_data = json.dumps(new_dict)
print(dumped_data)'''

## REGULAR EXPRESSIONS
## "From : abc@xyz.com . To: sami@gmail.com. Content: Heloo yess."
## requirement - take out every email address present in this data.
## how? python -> pattern of the data that you're looking for -> Regular Expressions

text ='''
1	eric.lopez@gmail.com O+ 30 Shivam Shukla
2	eric.lund@gmail.com
3	eric.m.boehm@gmail.com
4	eric.mack@gmail.com
5	eric.mason@gmail.com
6	eric.mathews@gmail.com
7	eric.maynard@gmail.com
8	eric.mckinney@gmail.com
9	eric.meredith@gmail.com
10	eric.mintz@gmail.com
11	eric.mistry@gmail.com
12	eric.mittler@gmail.com
13	eric.moeller@gmail.com
14	eric.monica@gmail.com
15	eric.moore@gmail.com
16	eric.murrell@gmail.com
17	eric.nay@gmail.com
18	eric.neilson@gmail.com
19	eric.nelson@gmail.com
20	eric.newcomer@gmail.com
21	eric.nghiem@gmail.com
22	eric.nishant@gmail.com
23	eric.noss@gmail.com
24	eric.nyberg@gmail.com
25	eric.o.neil@gmail.com
26	eric.odonnell@gmail.com
27	eric.ogren@gmail.com
28	eric.olsen@gmail.com
29	eric.oosterhof@gmail.com
30	eric.pace@gmail.com'''
ans = re.findall("[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+" , text)
print(ans)


text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. If you’re curious about this, it’s a garbled quotation from Cicero’s De Finibus Bonorum et Malorum (On the Ends of Good and Bad), book 1, paragraph 32, which reads, “Neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit,” meaning, “There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain.” The book was popular during the Renaissance, when the passage was used in a book of type samples for that wonderful new technology, printing."

ans = re.findall("[. ,](a[a-zA-Z0-9]*)",text)
print(ans)
# Q) Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3





















            





































