import random
from os import system

system('title '+'Rock Scissoer Paper Shadnaz')

#Ask how many times
times=int(input("How many times do you want to play? "))
#score
score_computer=0
score_user=0
game_list=["rock","scissoer","paper"]

for i in range(0,times):
    #Choose weapon from user
    user_weapon=input("Please choose your weapon [rock,scissor,paper]: ")

    #Choose weapon from computer
    random_number=random.randint(0,2)
    computer_weapon=game_list[random_number]
    # print('Computer weapon is {}'.format(computer_weapon))
    print(f'Computer weapon is {computer_weapon}')

    #Compare wepons
    if user_weapon=='rock' and computer_weapon=='paper':
        score_computer+=1
        print('You lost')
    elif user_weapon=='rock' and computer_weapon=='scissor':
        score_user+=1
        print('You win')
    elif user_weapon=='rock' and computer_weapon=='rock':
        print('The game equalised')
    elif user_weapon=='scissor'and computer_weapon=='paper':
        score_user+=1
        print("You win")
    elif user_weapon=='scissor'and computer_weapon=='scissor':
        print("The game equalised")
    elif user_weapon=='scissor'and computer_weapon=='rock':
        score_computer+=1
        print("You lost")
    elif user_weapon=='paper'and computer_weapon=='paper':
        print("The game equalised")
    elif user_weapon=='paper'and computer_weapon=='scissor':
        score_computer+=1
        print("You lost")
    elif user_weapon=='paper'and computer_weapon=='rock':
        score_user+=1
        print("You win")

#Show who wins
if score_user>score_computer:
    print("\n\tYou won!!!" )
elif score_computer>score_user:
    print("\n\tYou lost!!!!!!")
else:
    print("\n\tEquised")

print(f'Computer {score_computer} - {score_user} You')    