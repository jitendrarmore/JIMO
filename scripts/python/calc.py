#!/usr/local/bin/python3

#import sys
while True:
  print("Options:")
  print("Enter 'add' to add two numbers")
  print("Enter 'subtract' to subtract two numbers")
  print("Enter 'multiply' to multiply two numbers")
  print("Enter 'divide' to divide two numbers")
  print("Enter 'quit' to end the program")
  user_input = raw_input(": ")

  if user_input == "quit":
    break
  elif user_input == "add":
    number1 = float(input("Kindly enter the adfirst number :" ))
    number2 = float(input("Kindly enter the secondd number :" ))
    result = number1 + number2
    print("The answer is : ", result)


  elif user_input == "subtract":
    number1 = float(input("Kindly enter the first number :" ))
    number2 = float(input("Kindly enter the secondd number :" ))
    result = number1 - number2
    print("The answer is : ", result)

  elif user_input == "multiply":
    number1 = float(input("Kindly enter the first number :" ))
    number2 = float(input("Kindly enter the secondd number :" ))
    result = number1 * number2
    print("The answer is : ", result)

  elif user_input == "divide":
    number1 = float(input("Kindly enter the first number :" ))
    number2 = float(input("Kindly enter the secondd number :" ))
    result = number1 // number2
    resultremainder = number1 % number2
    print("The answer is : ", result, "balance is :", resultremainder)

  else:
    print("Unknown input")

