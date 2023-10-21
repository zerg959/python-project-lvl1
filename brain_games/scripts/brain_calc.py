#!/usr/bin/env python3

from random import randint
import prompt
import start_func


start_expression = 'What is the result of the expression?'

# counter = 0


# def start():
#     print("Welcome to the Brain Games")
#     global name
#     name = prompt.string("May I have your name? ")
#     print(f'Hello, {name}!')
#     print('What is the result of the expression?')


def question_func():
    a = randint(0, 5)
    b = randint(0, 5)
    operators = [' + ', ' - ', ' * ']
    my_operator = operators[randint(0, len(operators)-1)]
    question_string = str(a) + my_operator + str(b)
    return question_string


def answer_func():
    counter = 0
    while counter != 3:
        question = question_func()
        correct_answer = str(eval(question))
        print(f'Question: {question}')
        answer = input('Your_answer: ')
        if answer == correct_answer:
            print('Correct')
            counter += 1
            # print(f'Question: {question}')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {start_func.name}!")
            # print(f'Question: {question}')
            # answer = int(input('Your_answer:'))
    print(f'Congratulations, {start_func.name}!')


def main():
    start_func.start(start_expression)
    question_func()
    answer_func()


if __name__ == "__main__":
    main()
