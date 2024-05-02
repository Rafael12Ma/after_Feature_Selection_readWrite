# from art import logo
import random

import time


def play_game():
  print("                  Welcome to Rafael's Blackjack Game!")

  # print(logo)
  cards = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  flag = "y"
  print("_________________________________________________________")
  name = input("What is your name? ")
  sum = 0

  randomCard = random.choice(cards)
  player_list = [randomCard]
  index = 0
  queue = 1

  while flag == "y":
    print(f"\n {queue})")
    queue += 1
    randomCard = random.choice(cards)
    player_list.append(randomCard)

    # paiktis
    for i in player_list:
      if index > 0:
        sum = player_list[-1] + sum
        break
      else:
        sum = sum + i
    print(f"\n\n{name} got {player_list[index]}")
    time.sleep(0.6)
    index += 1
    if index < 2:
      print(f"and {player_list[index]}")
      time.sleep(0.6)
      index += 1
    print(f"Your total is : {sum}")
    time.sleep(0.6)

    if sum < 21:
      flag = input("You want onother card? Type 'y' for yes and 'n'for no.\n")
    elif sum == 21:
      flag = "n"
      print("\nYou won!")
      if (player_list[0] + player_list[1]) == 21:
        print("You got a Blackjack!")
    elif sum > 21:
      print("\n You lost! You went over 21.")
      flag = "n"

  # COMPUTER
  if sum < 22:
    print("\n\n\n\n\nComputer's Turn")
  time.sleep(0.2)
  print(".\n")
  time.sleep(0.2)
  print(".\n")
  time.sleep(0.2)
  print(".\n")
  time.sleep(0.2)

  queuec = 1
  sumc = 0
  indexc = 0

  while sumc < 18 and sum < 22:
    print(f"\n {queuec})")
    time.sleep(0.6)
    queuec += 1
    computer_list = [random.choice(cards)]
    for i in computer_list:
      if indexc > 0:
        sumc = computer_list[-1] + sum
        break
      else:
        sumc = sumc + i
    print(f"\nComputer got {computer_list[indexc]}")
    time.sleep(0.6)
    index += 1
    print(f"Computer's total is : {sumc}\n\n")
    time.sleep(0.6)
  if sum < 22 and sumc < 22:
    if sum > sumc:
      print("You won!")
    elif sum == sumc:
      print("It's a draw!")
    else:
      print("You lost!")

    print("Game over!")
  elif sum < 22 and sumc > 21:
    print(f"{name} won this round!")
  else:
    print("Computer won this round!")


while input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()