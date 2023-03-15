from math import *
import useful_tools
from student import Student
from questions import Questions
from chef import Chef
from chinesechef import ChineseChef

print("Hello World")
#
# # Variables and Data Types
# isMale = False
# print(isMale)
#
# # Strings
# phrase = "Learn Python"
# print(phrase.upper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[1])
# print(phrase.index("L"))
# print(phrase.replace("Learn", "Learning"))
# print(phrase)
#
# # Numbers
# print(-28.02)
# num = 5
# print(num)
# print(str(num) + " is my favourite number.")
# negNum = -10
# print(abs(negNum))
# print(pow(negNum, 2))
# print(max(2, 10))
# print(min(2, 10))
# print(round(5.2))
# print(round(5.6))
#
# print(floor(4.7))
# print(ceil(4.2))
# print(sqrt(10))
#
# Getting Input From Users
# name = input("Enter your name. ")
# age = input("Enter your age. ")
# print("\nHello " + name + "! You are " + age)
#
# Basic Calculator
# num1 = input("Enter a Number:")
# num2 = input("Enter second Number:")
#
# result = int(num1) + float(num2)
# print(result)
# print(type(result))
#
# # Lists
# friends = ["Amit", "Sudharshan", "Ambreen", "Ashutosh", "Ashish"]
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[1:3])
# friends[1] = "Suddu"
# print(friends[1])
#
# # List Functions
#
# luckyNumbers = [4, 8, 10, 15, 35]
# friends.append("Harsh")
# friends.insert(5, "Shivangi")
# print(friends)
# friends.remove("Shivangi")
# print(friends)
# friends.pop()
# print(friends)
# # friends.extend(luckyNumbers)
# print(friends)
# # friends.clear()
# # print(friends)
#
# print(friends.index("Amit"))
# # print(friends.index("Shivangi"))
# print(friends.count("Amit"))
# friends.sort()
# print(friends)
#
# luckyNumbers.reverse()
# print(luckyNumbers)
#
# friends2 = friends.copy()
# print(friends2)
#
# # Tuples
# ####### immutable
# coordinates = (4, 5)
# # coordinates[1] = 7
# print(coordinates[0])
#
#
# # Functions
# # Function names should be all lower case letters, and use underscore to separate the words
# def sayhi(name, age):
#     print("Hello " + name + "! you are " + str(age))
#
#
# sayhi("Shruti", 25)
# sayhi("Smruti", 22)
#
#
# # Return statements
# def cube(num):
#     return num * num * num
#
#
# result = cube(4)
# print(result)
#
# # If statements
# isFemale = False
# isTall = True
#
# if isFemale:
#     print("You are a Female")
# else:
#     print("You are not a Female")
#
# if isFemale or isTall:
#     print("You are a Female or tall or both")
# else:
#     print("You are neither a Female nor tall")
#
# if isFemale and isTall:
#     print("You are a tall Female")
# else:
#     print("You are either not a Female or not tall or both")
#
# if isFemale and isTall:
#     print("You are a tall Female")
# elif isFemale and not isTall:
#     print("You are a short Female")
# elif not isFemale and isTall:
#     print("You are not a Female but are tall")
# else:
#     print("You are not a Female and not tall")
#
#
# # If statements and comparisons
# def maxnumber(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print("Enter three numbers.")
# n1 = input(print("\nFirst Number:"))
# n2 = input(print("\nSecond Number:"))
# n3 = input(print("\nThird Number:"))
#
# print(type(n1))
# print(maxnumber(int(n1), int(n2), int(n3)))
#
# # A Better Calculator
# print("\nEnter Two Numbers.")
# m1 = input(str.format("\nFirst Number: \n"))
# m2 = input(str.format("\nSecond Number: \n"))
#
# op = input(str.format("Select Operation:\n1. Add\n2. Subtract \n3. Multiply\n4. Divide\n5. Mod \n"))
#
# if op == "1" or op == "Add" or op == "add":
#     print(float(m1) + float(m2))
# elif op == "2" or op == "Subtract" or op == "subtract":
#     print(float(m1) - float(m2))
# elif op == "3" or op == "Multiply" or op == "multiply":
#     print(float(m1) * float(m2))
# elif op == "4" or op == "Divide" or op == "divide":
#     print(float(m1) / float(m2))
# elif op == "5" or op == "Mod" or op == "mod":
#     print(float(m1) % float(m2))
# else:
#     print("\nInvalid Operation.")
#
# # Dictionary
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     11: "November",
#     12: "December",
# }
#
# print(monthConversions["Feb"])
# print(monthConversions.get("Feb"))
# print(monthConversions.get(12))
# print(monthConversions[11])
# print(monthConversions.get("num", "not a valid key"))
#
# # while loop
# i = 0
# while i < 4:
#     print(i)
#     i += 1
#
# print("Done")
#
# # A Guessing Game
#
# secret_word = "animal"
# guess_count = 0
# guess_limit = 3
# guess = ""
# out_of_guesses = False
#
# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess:")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if not out_of_guesses:
#     print("You Win!")
# else:
#     print("Out of guesses, YOU LOSE!")
#
# # For Loops
#
# for letter in "Shruti Kadam":
#     print(letter)
#
# cousins = ["Pranav", "Yadnesh", "Prajakta", "Omkar"]
# for cousin in cousins:
#     print(cousin)
#
# for i in range(5):
#     print(i)
#
# for i in range(2,6):
#     print(i)
#
# for i in range(len(cousins)):
#     print(cousins[i])
#
# # Exponent Function
#
# print(2 ** 3)
#
#
# def exponent_function(base, pow):
#     result = 1
#     for i in range(pow):
#         result = result * base
#     return result
#
#
# base_num = int(input("Enter Base"))
# pow_num = int(input("Enter Power"))
#
# print(exponent_function(base_num, pow_num))
#
# # 2D Lists and Nested Loops
#
# number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(number_grid[1][0])
#
# for row in number_grid:
#     for column in row:
#         print(column)
#
# # Build a translator
#
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "S"
#             else:
#                 translation = translation + "s"
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(translate(input("Enter a phrase: ")))
#
# # Try/Except
#
# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)
#
# # Reading a file
# flatmates_file = open("D:\Python\Flatmates.txt", "r")
# print(flatmates_file.readable())
#
# # print(flatmates_file.readline())
# # print(flatmates_file.readline())
# # #print(flatmates_file.readlines())
# # print(flatmates_file.readlines()[2])
#
# for flatmate in flatmates_file.readlines():
#     print(flatmate)
#
# flatmates_file.close()
#
# # Writing to a file
# # a - appends the file
# # w - write into new file or overwrites the file
#
# flatmate_file = open("D:\Python\Flatmates.txt", "a")
# flatmate_file.write("\nKunal - shares room B")
# flatmate_file.close()
#
# outsiders_file = open("D:\Python\Outsiders.txt", "w")
# outsiders_file.write("Aditya - shares room A\nKunal - shares room B")
# outsiders_file.close()
#
# index_file = open("D:\Python\index.html", "w")
# index_file.write("<p>This is HTML</p>")
# index_file.close()
#
# # Modules and pip
# # pip is a pacakge installer for python
# # pip is used to install python modules, it's a package manager
# # allows managing packages like to install update uninstall modules
# # pip install python-docx
# # easy_install python-docx
#
# # pip install modulename
# # pip uninstall modulename
#
# print(useful_tools.roll_dice(6))
#
# # Classes and Objects
#
# student1 = Student("Shruti", "Computer Science", 7, False)
# print(student1.name)
# print(student1.gpa)
#
# student2 = Student("Smruti", "Pharmacy", 8 , False)
# print(student2.name)
#
# # Multiple Choice Quiz
#
# questions_list = ["What color are apples? \n(a) Red/Green \n(b) Orange \n(c) Yellow\n",
#                   "What color are bananas? \n(a) Red \n(b) Blue \n(c) Yellow\n",
#                   "What color are strawberries? \n(a) Red \n(b) Orange \n(c) Black\n"]
#
# questions = [Questions(questions_list[0], "a"),
#              Questions(questions_list[1], "c"),
#              Questions(questions_list[2], "a")]
#
#
# def run_quiz(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.quest)
#         if answer == question.answer:
#             score += 1
#     print("you got " + str(score) + "/" + str(len(questions)) + " correct answers.")
#
#
# run_quiz(questions)
#
# # Object Functions
#
# print((student1.on_honor_roll()))
# print((student2.on_honor_roll()))
#
# #  Inheritance
#
# myChef = Chef()
# myChef.make_special_dish()
#
# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()
# myChineseChef.make_salad()

# import re
#
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)


from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./UneditedImages"
pathOut = "./EditedImages"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    # ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
