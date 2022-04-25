#integers, strings, boolean, dictionaries, sequences
myint = 4
myfloat = 3.3
mystr = "This is my name"
mybool = False
mylist = [0,1,2,3,4,5]
mytuple= (0,1,2)
mydict= {"one": 1, "two": 2}


print (myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

#You can redclare variables
myint = "this is a new string"
print(myint)

#use [] to access a member of a sequence type
print(mylist[3])
print(mytuple[0])

#use slices to get part of a sequence
print(mylist[3:5])

#use slices to reverse a sequence
print(mylist[::-1])

#dictionaries are accessed via keys
print(mydict["one"])