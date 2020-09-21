class Person():

    def welcome(self):
        print("Hello python")

    def sum(self,num1,num2):
        print(num1+num2)

#this funciton is outside of the class so when we call this function we don't need to refer through an object
def hello_sekhar():
    print("Hello sekhar")

p=Person()
Person.welcome(p)       #p will be passed to the self, self means instance of the current class
Person.welcome(Person)
p.sum(4,5)