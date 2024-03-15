import check_input
import random
## Name: Justin Pongos & Louis Pavlovsky
## Date: 01/29/2024
def main():
## Desc: Shell Game, a game where a user is meant to bet and guess on the
positiion of the ball. The user starts off with a hundred points and depending if
the guess is correct the money bet will be added to or subtracted from the user's
total. If there is no money you lose and the game is over.
print("-Shell Game-\nFind the ball to double your bet!")
player_money = 100
is_playing = True
# Loop till the player decides to quit the game or is out of money
while is_playing:
print (f"\nYou have ${player_money}.")
player_bet_amount = check_input.get_int_range("Bet amount? ", 1, player_money)
solution_number = random.randint(1, 3)
print(" ___ ___ ___\n\
/ \\ / \\ / \\\n\
/ 1 \\ / 2 \\ / 3 \\\n\
------- ------- ------- ")
player_guess = check_input.get_int_range("Make a guess: ", 1, 3)
# Solution_list will hold the result of the random number generator for
printing purpose
solution_list = ['x', 'x', 'x']
solution_list[solution_number - 1] = 'o'
print(f" ___ ___ ___\n\
/ \\ / \\ / \\\n\
/ {solution_list[0]} \\ / {solution_list[1]} \\ / {solution_list[2]} \\\n\
------- ------- ------- ")
if (solution_number == player_guess):
print("Congratulations!\n")
player_money += player_bet_amount
else:
print("Sorry... you lose.")
player_money -= player_bet_amount
if (player_money <= 0):
print("You're out of money! Game" + "\n" +
"over.")
return 0
is_playing = check_input.get_yes_no("Play again? (Y/N): ")
main()
