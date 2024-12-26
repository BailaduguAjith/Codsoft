import random
user_choice= int(input("enter your choice: type 0 for rock, 1 for paper, 2 for scissor:"))
computer_choice=random.randint(0,2)
print("compuer chose:")
print("computer_choice")
if computer_choice == user_choice:
    print("it's a draw.")
elif computer_choice > user_choice:
    print("you lose.")
elif computer_choice > user_choice:
    print("you win.")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice == 0 and computer_choice == 2:
    print("your win")