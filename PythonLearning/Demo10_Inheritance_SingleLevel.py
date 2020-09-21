class Base:
    name="sekhar"
    def baseMethod(self):
        print("I am in Base Method")

class Child_1:
    def childMethod1(self):
        print("I am in Child Method 1")

class Child_2(Base):            #Here we are inheriting the base method
    company = "IBM"
    def childMethod2(self):
        print("I am in Child Method 2")

b=Base()
b.baseMethod()
c1=Child_1()
c1.childMethod1()
c2=Child_2()
c2.childMethod2()
c2.baseMethod()
print(c2.name)
print(c2.company)
