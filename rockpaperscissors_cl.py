import random

choices = {'rock': 1,
            'paper': 2,
            'scissors': 3}
computerChoiceList = [1,2,3]
# 1:rock 2:paper 3:scisors

computerChoice = random.choice(computerChoiceList)

getChoice = input("enter your choice:\n 1 - rock \n 2 - paper \n 3 - scissors \n")
userChoice = choices.get(getChoice)

diff = userChoice - computerChoice

if  diff in [1,-2] :
        print("player wins")
elif diff in [-1,2]:
    print('computer wins')
else:
    print('tie')
