#!/usr/bin/env python3

print("Letter Grade Converter")
Continue = "y"
while Continue.lower() == "y":
    grade = int(input("\nEnter a Numerical Grade: "))
    if grade >= 88:
        letter_grade = "A"
    elif grade >= 80 and grade <88:
        letter_grade = "B"
    elif grade >= 67 and grade <80:
        letter_grade = "C"
    elif grade >= 60 and grade <67:
        letter_grade = "D"
    else:
        letter_grade = "F"
        
    print("Letter Grade: " + letter_grade)
    Continue = input("\ncontinue (y/n)?")
        
print("Bye !")
