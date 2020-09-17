def helloworld():
    print('hello world...')
helloworld()
# callable(helloworld())

def sum(num1,num2):     # num2=0 will be used as default value if we don't provide num2 in sum function
    result = num1 + num2
    print("Result is..", result)
    return result

result=sum(4,5)
finalresult = 6+result
print(finalresult)

def mul(num1, num2):
    prodresult=num1*num2
    print("Product is..", prodresult)

mul(5,6)
