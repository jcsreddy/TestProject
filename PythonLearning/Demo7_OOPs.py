class Person():

    def welcome(self):
        print("Hello python")

    def hello_world(self):
        print("Hello world")

#this funciton is outside of the class so when we call this function we don't need to refer through an object
def hello_sekhar():
    print("Hello sekhar")


p = Person()
p.welcome()
p.hello_world()
hello_sekhar()
print(p.welcome)
print(hello_sekhar)