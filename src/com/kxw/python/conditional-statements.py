#!/usr/bin/python

# Python中用elif代替了else if，所以if语句的关键字为：if – elif – else。
age = int(input("Age of the dog: "))
print()
if age < 0:
    print("This can hardly be true!")
elif age == 1:
    print("about 14 human years")
elif age == 2:
    print("about 22 human years")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("Human years: ", human)

###
input('press Return>')

'''在Python中没有switch – case语句。'''

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))

    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
