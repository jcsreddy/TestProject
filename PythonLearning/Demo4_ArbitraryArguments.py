def print_value(*args):
    print(args)

    for name in args:
        print(name)


print_value("C", "C++", "C#", "Java", "Python")

#output will be in form of tuple -- ('C', 'C++', 'C#', 'Java', 'Python')

def sum_of_all_num(*args):
    print(sum(args))

def min_of_all_num(*args):
    print(min(args))

def max_of_all_num(*args):
    print(max(args))

sum_of_all_num(5, 10, 15, 20)
min_of_all_num(5, 10, 15, 20)
max_of_all_num(5, 10, 15, 20)