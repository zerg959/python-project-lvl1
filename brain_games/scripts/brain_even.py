#!/usr/bin/env python3

from random import randint

import prompt

name = ''


def odd_or_even():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    answer_even = 'yes'
    answer_odd = 'no'
    while counter != 3:
        question = randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            if answer == answer_even:
                print('Correct!')
                counter += 1
            else:
                counter = 0
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{answer_even}.'")
                print(f"Let's try again, {name}!")
        if question % 2 == 1:
            if answer == answer_odd:
                print('Correct!')
                counter += 1
            else:
                counter = 0
                print(f"'{answer}' is wrong answer;(. "
                      f"Correct answer was '{answer_odd}.'")
                print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


def main():
    odd_or_even()


if __name__ == "__main__":
    main()
