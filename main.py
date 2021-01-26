from art import logo
from replit import clear
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def compare(player_score, computer_score):
  if player_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif player_score == 0:
    return "Win with a Blackjack"
  elif player_score > 21:
    return "You went over 21. You lose"
  elif computer_score > 21:
    return "Computer went over 21. You win."
  elif player_score > computer_score:
    return "You Win!"
  else:
    return "You Lose!"

def calculate_score(cards):
  # Blackjack
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # When sum exceeds 21, ace should be treated as 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def play_game():
  print(logo)
  player = []
  computer = []
  game_over = False
  for _ in range(2):
    player.append(deal_card)
    computer.append(deal_card)

  while not game_over:
    player_score = calculate_score(player)
    computer_score = calculate_score(computer)

    def display(player, computer):
      print(f"  Your cards: {player}, current score: {player_score}")
      print(f"  Computer's first card: {computer[0]}")

    def display_final(player, computer):
      print(f"  Your final hand: {player}, final score: {player_score}")
      print(f"  Computer's final hand: {computer}, final score: {computer_score}")

    display(player, computer)

    if player_score == 0 or computer_score == 0 or player_score > 21:
      game_over = True
    else:
      choice = input("Type 'y' to get another card, type 'n' to pass.")
      if choice == 'y':
        player.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)

  display_final(player, computer)
  print(compare(player_score, computer_score))

new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
if new_game == 'y':
  clear()
  play_game()
