
import math
radius = float(input("Enter the radius of the garden "))

A = math.pi * math.pow(radius, 2)

C = 2 * math.pi * radius

Sr_A = math.sqrt(A)

uA = math.floor(A)
dA= math.ceil(A)

print (f"Area of the garden: {A}, square meters ")
print (f"Circumference of the garden: {C}, square meters ")
print (f"Square root of the garden: {Sr_A}")
print (f"Area rounded up: {uA}")







