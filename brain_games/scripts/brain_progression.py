#!/usr/bin/env python3
import prompt
from random import randint
# import start_func

name = ''
dot_elem = '..'
counter = 0
# expression = 'What number is missing in the progression?'


def progression_generator():
    progression = []
    for i in range(1, 21, randint(1, 5)):
        progression.append(str(i))
    return progression


def progression_func():
    global counter
    while counter != 3:
        my_list = progression_generator()
        idx = randint(0, len(my_list)-1)
        correct_answer = my_list[idx]
        my_list.pop(idx)
        my_list.insert(idx, dot_elem)
        progression_str = ' '.join(my_list)
        print(f"Question: {progression_str}")
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"Your answer: '{answer}' is wrong answer;(. "
                  f"Correct answer was '{correct_answer}'. "
                  f"Let's try again, {name}!")
            counter = 0
    print(f'Congratulations, {name}!')


def main():
    global name
    print("Welcome to the Brain Games")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    progression_generator()
    progression_func()


if __name__ == '__main__':
    main()
