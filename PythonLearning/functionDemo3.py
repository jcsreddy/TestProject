def check_even_number(list1):
    even_number = []

    for x in list1:
        if x % 2 == 0:
            even_number.append(x)
        else:
            pass
    return even_number


result = check_even_number([1,2,3,5,6,8,9, 10])
print(result)

print(len(result))