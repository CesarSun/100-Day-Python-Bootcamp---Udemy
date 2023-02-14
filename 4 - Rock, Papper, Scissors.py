import random

def print_rock():
    print("    _____")
    print("---'   __)")
    print("      (____)")
    print("      (____)")
    print("      (____)")
    print("---.__(___)")

def print_paper():
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("         _______)")
    print("        _______)")
    print("---.__________)")

def print_scissors():
    print("    _______")
    print("---'   ____)____")
    print("          ______)")
    print("       __________)")
    print("      (____)")
    print("---.__(___)")

def print_hand(hand):
    hands = ["Rock", "Paper", "Scissors"]
    print(hands[hand])

def get_player_hand():
    while True:
        answer = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or q to quit.\n")
        if answer.lower() == "q":
            return None
        elif answer not in ["0", "1", "2"]:
            print("Invalid input. Please try again.")
        else:
            return int(answer)

def get_computer_hand():
    return random.randint(0, 2)

def print_hands(player_hand, computer_hand):
    print("You chose:")
    print_hand(player_hand)
    print("Computer chose:")
    if computer_hand == 0:
        print_rock()
    elif computer_hand == 1:
        print_paper()
    else:
        print_scissors()

def print_result(player_hand, computer_hand):
    if player_hand == computer_hand:
        print("Tie!")
    elif (player_hand == 0 and computer_hand == 2) or (player_hand == 1 and computer_hand == 0) or (player_hand == 2 and computer_hand == 1):
    #elif (player_hand - computer_hand) % 3 == 1: "Essa condição eu aprendi"
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:
        player_hand = get_player_hand()
        if player_hand is None:
            print("Thanks for playing!")
            break

        computer_hand = get_computer_hand()
        print_hands(player_hand, computer_hand)
        print_result(player_hand, computer_hand)

if __name__ == "__main__":
    print('Welcome to the Rock Paper Scissors game!')
    play_game()
