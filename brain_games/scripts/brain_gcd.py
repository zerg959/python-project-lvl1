#!/usr/bin/env python3
import prompt
from random import randint
name = ''


def gcd():
    counter = 0
    while counter != 3:
        num_1, num_2 = randint(1, 100), randint(1, 100)
        divisors_1, divisors_2 = [], []
        great_common_divisor = []
        for i in range(1, num_1+1):
            if num_1 % i == 0:
                divisors_1.append(i)
            if num_2 % i == 0:
                divisors_2.append(i)
        for elem in divisors_1:
            if elem in divisors_2:
                great_common_divisor.append(elem)
        correct_answer = max(great_common_divisor)
        print('Question:', num_1, num_2)
        answer = input('Yours answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            counter += 1
        else:
            print(f'{answer} is wrong answer;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            counter = 0
    print(f'Congratulations, {name}!')


def main():
    global name
    print("Welcome to the Brain Games")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers')
    gcd()


if __name__ == "__main__":
    main()
