#defining a function
def project1():
    print("I am a function")
    
#project1()
#print(project1())

#function that takes in arguments
def project2(arg1, arg2):
    print(arg1,"",arg2)

#function that returns a value
def cube(x):
    return x*x*x


#project2(10, 20)
#print(project2(10, 20))
#cube(2)
#print(cube(2))

#function with default value for an argument
def power(num, x=1):
    result =1;
    for i in range(x):
        result=result* num
    return result
print(power(2))
print(power(2,3))