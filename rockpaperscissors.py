import random

user_action = input("Enter rock, paper, or scissors:")
possible_actions = ["rock","paper","scissors"]
computer_action = random.choice(possible_actions)
lose_insult_list = ["wow u lost to a computer", "how r u gonna lost to a machine","stop losing"]
win_insults = ["the computer let u win, you\'re welcome"]
print(f"\nYou chose {user_action} and your opponent chose {computer_action}")  

if user_action == computer_action: 
    print("its a tie")
elif user_action == "rock":
    if computer_action == "paper":
        print(random.choice(lose_insult_list))
    else:
        print(random.choice(win_insults))
elif user_action == "paper":
    if computer_action == "rock":
        print(random.choice(win_insults))
    else:
        print(random.choice(lose_insult_list))
elif user_action == "scissors":
    if computer_action == "rock":
        print(random.choice(lose_insult_list))
    else:
        print(random.choice(win_insults))