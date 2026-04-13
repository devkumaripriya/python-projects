'''
WORKFLOW OF PROJECT:
1-Input from user(Rock,paper,scissor)
2-Computer choice(Computer will choose randomly not conditionally)
3- Result Print

Cases:
A-Rock
Rock - Rock = tie
Rock - Paper =Paper win
Rock - scissor= Rock win

B-Paper
Paper - paper= tie
Paper- Rock =Paper Win
Paper-Scissor=Scissor win


C - Scissor
Scissor -Scissor = tie
Scissor-Rock=Rock win
Scissor-Paper=Scissor Win
'''
import random 
item_list=["Rock","Paper","Scissor "]

user_choice= input("Enter Your move =Rock, Paper,Scissor :")
comp_choice = random.choice(item_list)

print(f"User choice ={user_choice},Computer choice ={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same:=Match Tie")

elif user_choice =="Rock":
    if comp_choice=="paper":
        print("Paper covers Rock = Computer win")
    else:
        print("Rock smashes Scissor = You Win")
        
elif user_choice =="Paper":
    if comp_choice=="Scissor":
        print("Scissor cuts paper,Computer win")
    else:
        print("Paper Covers Rock,You Win")
        
elif user_choice =="Scissor":
    if comp_choice =="paper":
        print("Scissors Cuts the Paper,You Win")
    else :
        print("Rock Smashes the scissors,Computer win")