import game_data
import art
import random

# Function to show comparing items
def chosen_list(item):
    for i in item:
        if i != "follower_count":
            value.append(item[i])
        else:
            followers = item[i]
    return followers

# Function for comparing followers
def compare(guess_word):
    if guess_word == "A":
        if nun_of_follower1 > nun_of_follower2:
            return True
        else:
            return False
    else:
        if nun_of_follower1 < nun_of_follower2:
            return True
        else:
            return False

# Printing a logo
print(art.logo)

score = 0
b_in_a = {}
game = True
while game:

    # 1st value
    if score == 0:
        choice1 = random.choice(game_data.data)
    else:
        choice1 = b_in_a
    value = []
    nun_of_follower1 = chosen_list(choice1)
    print(f"CompareA: {value[0]}, {value[1]}, {value[2]}.")

    # Printing a VS symbol
    print(art.vs)

    # 2nd value
    choice2 = random.choice(game_data.data)
    if choice2 == choice1:
        choice2 = random.choice(game_data.data)
    value = []
    nun_of_follower2 = chosen_list(choice2)
    print(f"CompareB: {value[0]}, {value[1]}, {value[2]}.")

    # Asking which is true
    your_guess = input("Who has more followers. 'A' or 'B':\n").upper()
    right_wrong = compare(your_guess) #comparing

    # playing game
    print("\n" * 20)
    print(art.logo)
    if right_wrong:
        score+=1
        b_in_a = choice2
        print(f"You are right. Current Score: {score}")
    else:
        print(f"Sorry you are wrong. Final Score: {score}")
        game = False