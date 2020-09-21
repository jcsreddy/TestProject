class classParent:
    def methodA(self):
        print("I am in Parent Class")

class classChild(classParent):
    def methodA(self):
        super().methodA()
        print("I am in Child Class")

class classSibling(classChild):
    def methodA(self):
        classParent.methodA(self)       #calling parent / blass from sibling
        super().methodA()               #super from classSibling is the classChild and hence we display methodA() in classChild
        print("I am in Sibling Class")

# p=classParent()
# p.methodA()
# c=classChild()
# c.methodA()
s=classSibling()
s.methodA()
