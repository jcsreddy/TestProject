def print_value(**kwargs):
    print(kwargs)
    print(kwargs["Location"])

print_value(name="Sekhar", Location='Bangalore', Pincode=560034)


#Arbitrary KeyWord Arguments will use Dictionary

def hello_world(number, *args, **kwargs):
    print(number)
    print(args)
    print(kwargs)
    print(kwargs["city"])


hello_world(3, 2, 6, name='sekhar', city='bangalore')       #here number will be taken as 3, args will be 2,6