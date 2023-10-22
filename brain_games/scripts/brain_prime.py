#!/usr/bin/env python
import prompt
from random import randint
name = ''


def prime_func():
    counter = 0
    while counter != 3:
        num = randint(2, 101)
        print('Question:', num)
        prime_counter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                prime_counter += 1
                if prime_counter > 2:
                    # print('not prime')
                    correct_answer = 'no'
                    break
                else:
                    # print('prime')
                    correct_answer = 'yes'
        answer = input('Answer: ')
        if answer == correct_answer:
            # global counter
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            counter = 0
    print(f'Congratulations, {name}!')


def main():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_func()


if __name__ == "__main__":
    main()
