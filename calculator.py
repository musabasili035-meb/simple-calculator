print("simple calculator")
x=float(input("enter first number: "))
y=float(input("Enter second number: "))

# Mathematical operations signs
print("choose operation: ")
print("+ addition")
print("- substruction")
print("* product")
print("/ division")

# Mathematical operations
sum=x+y
mult=x*y
sub=x-y
div=x/y

z=input("operator: ")
if z=="+":
 print("summation is: ", sum)
elif z=="-":
 print("Difference is: ",sub)
elif z=="*":
 print("Product is: ",mult)
elif z=="/":
 print("Division is: ",div)

else:
 print("invalid operator")



