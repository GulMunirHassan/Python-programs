"""Q1: Write a Python Program to print the following string in specific format"""
print("Question No. 1")
print("Twinkle,twinkle,little star,\n\tHow I wonder what you are!"
      "\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky."
      "\nTwinkle,twinke,little star,\n\tHow I wonder what you are")

"""Q2: Write a Python Program to get the python version you are using"""
print("\nQuestion No. 2")
import sys
print("Python Version You are using: ")
print(sys.version)

"""Q3: Write a Python Program to display current date and time"""
print("\nQuestion No. 3")
import datetime
print("Current Date and Time is: ",datetime.datetime.now())

"""Q4: Write a Python Program which accepts the radius of a circle from the user and compute the area"""
print("\nQuestion No. 4")
radius=int(input("Enter the Radius of the Circle: "))
area=3.14*(radius*radius)
print("Area of the Circle is: ",area)

"""Q5: Write a Python program which accepts the users first and last name and print them in reverse
 order with a space between them."""
print("\nQuestion No. 5")
first_name=input("Enter your First Name: ")
last_name=input("Enter Your Last_Name: ")
print("name in Reverse Order: ",last_name," ",first_name)

"""Q6: Write a python program which takes two inputs from user and print them addition"""
print("\nQuestion No. 6")
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print("Addition= ",num1+num2)