#!/usr/bin/env python3
import prompt
from random import randint

name = ''
# import sys
#
# sys.path.append('path')
# import start_func as ss
# # # import start_func as ss
# # from .start_func import *
#
# start_expression = 'What is the result of the expression?'


def question_func():
    a = randint(0, 5)
    b = randint(0, 5)
    operators = [' + ', ' - ', ' * ']
    my_operator = operators[randint(0, len(operators) - 1)]
    question_string = str(a) + my_operator + str(b)
    return question_string


def answer_func():
    counter = 0
    while counter != 3:
        question = question_func()
        correct_answer = str(eval(question))
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct')
            counter += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


def main():
    global name
    print("Welcome to the Brain Games")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    # ss.start(start_expression)
    question_func()
    answer_func()


if __name__ == "__main__":
    main()
