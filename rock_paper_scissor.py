import random
counter_play=0
counter_win_user=0
counter_win_computer=0
play_count=int(input("How many times do you want to play? "))
while(counter_play<play_count):
    user_input=int(input("Enter Rock=0 / Paper=1 / Scissor=2: "))
    computer_input=random.randint(0,2)
    if(user_input==0 and computer_input==2) or (user_input==1 and computer_input==0) or (user_input==2 and computer_input==1):
        counter_win_user+=1
        print(computer_input, "User won  ","User Score= ",counter_win_user,"\tComputer Score= ",counter_win_computer)
        counter_play+=1    
    elif(user_input==0 and computer_input==0) or (user_input==1 and computer_input==1) or (user_input==2 and computer_input==2):
        print(computer_input, "Equal  ","User Score= ",counter_win_user,"\tComputer Score= ",counter_win_computer)
        counter_play+=1
    elif(user_input==0 and computer_input==1) or (user_input==1 and computer_input==2) or (user_input==2 and computer_input==0):
        counter_win_computer+=1
        print(computer_input, "Computer won  ","User Score= ",counter_win_user,"\tComputer Score= ",counter_win_computer)
        counter_play+=1
    else:
        print("Out of Range  ","User Score= ",counter_win_user,"\tComputer Score= ",counter_win_computer)
if counter_win_user>counter_win_computer:
    print("User won the game")
elif counter_win_user<counter_win_computer:
    print("Computer won the game")
else:
    print("The game equalised")