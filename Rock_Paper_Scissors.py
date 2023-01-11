import random
def play():
	user = input("What's your choice?\n'r' for Rock, 'p' for Paper and 's' for Scissors: ")
	computer = random.choice(['r', 'p', 's'])
	if user == computer:
		return ("It's a Tie")
	if rules_win(user, computer):
		return ("You've won!!!")
	if rules_win(computer, user):
		return ("You've lost")
	if user != 'r' != 's' != 'p':
		return("Invalid input")
		
def rules_win (player, opponent):
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
		return True
print(play())	