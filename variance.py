#  File:       variance.py
#  Purpose:    Example : Statistics
#  Programmer: Amal Shehu
#  Course:     Codecademy
#  Date:       Tuesday 30th August 2016, 05:25 PM

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print (grade)


def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return (total)


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
