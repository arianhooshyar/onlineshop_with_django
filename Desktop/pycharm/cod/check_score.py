import datetime
from datetime import date
def score():
    score = []
    result = []
    lesson1 = int(input(' enter your number of lesson1 : '))
    if lesson1 != -1:
       score.append(lesson1)

    if lesson1 > 10 :
        result.append(f'lesson1 is pass by : {lesson1}')
    else:
        result.append(f'lesson1 is faild by : {lesson1}')

    lesson2 = int(input(' enter your number of lesson2 : '))
    if lesson2 != -1:
        score.append(lesson2)
    if lesson2 > 10:
        result.append(f'lesson2 is pass by : {lesson2}')
    else:
        result.append(f'lesson2 is faild by : {lesson2}')

    lesson3 = int(input(' enter your number of lesson3 : '))
    if lesson3 != -1:
        score.append(lesson3)
    if lesson3 > 10:
        result.append(f'lesson3 is pass by : {lesson3}')
    else:
        result.append(f'lesson3 is faild by : {lesson3}')

    lesson4 = int(input(' enter your number of lesson4 : '))
    if lesson4 != -1:
        score.append(lesson4)
    if lesson4 > 10:
        result.append(f'lesson4 is pass by : {lesson4}')
    else:
        result.append(f'lesson4 is faild by : {lesson4}')

    lesson5 = int(input(' enter your number of lesson5 : '))
    if lesson5 != -1:
        score.append(lesson5)
    if lesson5 > 10:
        result.append(f'lesson5 is pass by : {lesson5}')
    else:
        result.append(f'lesson5 is faild by : {lesson5}')

    lesson6 = int(input(' enter your number of lesson6 : '))
    if lesson6 != -1:
        score.append(lesson6)
    if lesson6 > 10:
         result.append(f'lesson6 is pass by : {lesson6}')
    else:
        result.append(f'lesson6 is faild by : {lesson6}')

    lesson7 = int(input(' enter your number of lesson7 : '))
    if lesson7 != -1:
        score.append(lesson7)
    if lesson7 > 10:
        result.append(f'lesson7 is pass by : {lesson7}')
    else:
        result.append(f'lesson7 is faild by : {lesson7}')

    lesson8 = int(input(' enter your number of lesson8 : '))
    if lesson8 != -1:
        score.append(lesson8)
    if lesson8 > 10:
        result.append(f'lesson8 is pass by : {lesson8}')
    else:
        result.append(f'lesson8 is faild by : {lesson8}')

    lesson9 = int(input(' enter your number of lesson9 : '))
    if lesson9 != -1:
        score.append(lesson9)
    if lesson9 > 10:
        result.append(f'lesson9 is pass by : {lesson9}')
    else:
        result.append(f'lesson9 is faild by : {lesson9}')

    print(score)
    print(result)



def BIO():
    First_name = input('enter first name : ')
    Last_name = input('enter last name : ')
    Age = input('enter Age : ')
    Gread = input('enter Gread')
    print(f'First_name = {First_name}')
    print(f'Last_name = {Last_name}')
    print(f'Age = {Age}')
    print(f'Gread = {Gread}')


def report_cart():


    BIO()
    score()




if __name__ == '__main__':
    report_cart()

