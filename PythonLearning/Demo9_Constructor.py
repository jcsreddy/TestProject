class Person:
    def __init__(self, fname, lname):             #Constructor, self is the current instance of the class
        print("Hello python", fname, lname)

        self.f = fname
        self.l = lname

        print(self.f, self.l)

    def sum(self, num1, num2):
        self.a =num1
        self.b=num2

        return self.a+self.b


p = Person("Sekhar", "Reddy")        #Constructor will get invoked once you create an object
print(p.sum(10, 10))

