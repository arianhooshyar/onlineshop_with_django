import random
from datetime import datetime, date
GAME_RANGE = int(input('pleas enter your range : '))
system_choice = random.randint(0, GAME_RANGE)
"system chose the number"
def user_choice():
    user_input = int(input('pleas enter your number : '))

    if user_input not in range(GAME_RANGE):
        print('your chice is out of the range, pleas try again...')
    return user_input
    return user_choice()
"player chose number"
def play():
    start = datetime.now()
    result = 0
    while result <5:
        user = user_choice()
        if user > system_choice:
            print('less')
            result  = result +1

        elif system_choice > user:
            print('more')
            result = result +1


        else:
            print('#' * 10)
            print('#' * 4, 'you are winner', '#' * 4)
            print('#' * 10)
            break
    else:
        print("ridiii")
    finish = datetime.now()

    total_time_yuo_played = finish -start


    play_again = input('Do you want to play again? (yes or no)\n')
    if play_again == 'yes':

        play()

    else:

        print(f'tody = {start.date()}\n')
        print(f'start time = {start.time()}\n'[:-7])
        print(f'finish time = {finish.time()}\n'[:-7])
        print(f'total time you play = {total_time_yuo_played}')

        print("good by")

if __name__ == "__main__":
  play()