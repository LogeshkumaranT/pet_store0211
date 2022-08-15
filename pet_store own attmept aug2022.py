class pet_store:
    def enter_store(self):
        print("welcome to the pet store!")
        return '\n'
        
class Cat(pet_store):
    def __init__(self,health,age):
        self.health=health
        self.age=age

    def walk(self):
        print('the health of this cat is ',self.health)
        print('the age of this cat ',self.age)
        return'are u interested to buy?'

class Dogs(pet_store):
    def __init__(self,health,age):
        self.health=health
        self.age=age

    def walk(self):
        print('the health of this dog is ',self.health)
        print('the age of this dog ',self.age)
        return'are u interested to buy?'
    
customer1=Cat('300',3)
customer2=Dogs('300',2)

welcome=pet_store()
print(welcome.enter_store())
print(customer1.walk())
print('\n')
print(customer2.walk())
print('\n')


y=input('yes or no: ')
if (y=='yes'):
    print("sure, i will pack it")
else:
    print("nothing to bother, you can see for other pets")