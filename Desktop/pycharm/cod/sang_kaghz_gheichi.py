import random
from sang_khaghz_gheichi_config import GAME_CHOICE, RULES, scoreboard
from datetime import datetime
print('Hello')
def get_user_choice():
    user_choice = (input('enter your choice(p, s, r) : '))
    if user_choice not in GAME_CHOICE:
        print('Oops.., your choice is out of range , pleas try again : ')
        return get_user_choice()
    return user_choice


def get_system_choice():
     return random.choice(GAME_CHOICE)



def find_winner(user, system):

    match = {user, system}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]
def up_scoreboard(result):

    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'You win'
    else:
        scoreboard['system'] += 1
        msg = 'You lose'

    print("#" * 30)
    print("#"*5, f'user: {scoreboard["user"]}', "#"*5)
    print("#"*5, f'system: {scoreboard["system"]}', "#"*5)
    print("#"*12, f'last game: {msg}', "#"*12)
    print("#" * 30)


def play():
    start = datetime.now()
    result = {'user' : 0, 'system' : 0}
    while result['user'] <3 and result['system'] <3:
       user_choice  = get_user_choice()
       system_choice = get_system_choice()
       winner = find_winner(user_choice, system_choice)
       if winner == user_choice:
           msg = 'you win'
           result['user'] +=1

       elif winner ==  system_choice:
           msg = 'you lose'
           result['system'] +=1

       else:
           msg = 'draw'

       print(f'user = {user_choice}, system = {system_choice}, result = {msg}')

    up_scoreboard(result)
    play_again = input('Do you want to play again ? (yes, no)')
    if play_again == 'yes':
        return play()
    else:
        print('Good by')
    finish = datetime.now()
    toutal_played_time = finish - start
    print(f' toutal time you played = {toutal_played_time}')



if __name__ == "__main__":
   play()