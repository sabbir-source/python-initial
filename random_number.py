import random

def computer_choice():
    return random.randrange(1,10)
def player_computer_choice(player,computer):
    if player == computer:
        print("it's tie")
    elif player != computer:
        print('Oops! try once')
def play_game():
   player_choice = int(input('enter your random number :'))
   if player_choice not in (1 ,10):
       return "pls write between 1, 10"
   x = computer_choice()
   print(f'Player : {player_choice}')
   print(f'Computer : {x}')

   return player_computer_choice(x,player_choice)

#RUN THE GAME
if __name__ == "__main__":
  print(play_game())
