import os
import random as rn

# Checks os to clear terminal
def clear():
    command = 'clear' # Use 'clear' for Unix Terminals
    if os.name in ('nt', 'dos'):  # Use 'cls' for Windows Shell
        command = 'cls'
    os.system(command)

# Creates array of strings for difficulty 
levels = [
  ["\n1. Very Easy:", "Unlimited Tries"],
  ["\n2. Easy:", "Five Tries (5)"],
  ["\n3. Medium:", "Five Tries (5)"], 
  ["\n4. Difficult:", "Eight Tries (8)"], 
  ["\n5. Very Difficult:", "Nine Tries (9)"], 
  ["\n6. QUIT:", "Leave The Game"]
]
# Creates dictionary of arrays for #tries, random number odds, and epsilon for closeness
triesOdds = {
  "1" : [True, 10, 2],
  "2" : [5, 10, 2],
  "3" : [5, 100, 5],
  "4" : [8, 500, 5],
  "5" : [9, 1000, 10],
  "6" : "QUIT",
  "QUIT" : "QUIT"
}
# Main game function
def game():
  # Create meta loop
  while True:
    clear()
    # Prints out the text from levels array in nice columns 
    for row in levels:
      print("{: <20} {: <20}".format(*row))
    # Get input for difficulty
    choice = input("\nPick a difficulty using the number: ")
    # Gets value for key 'choice'
    dif = triesOdds.get(choice)
    # If 'QUIT' is ever selected, break out of meta/function
    if dif == "QUIT":
      break
    
    # If the input is not one of the options available then restart from the top
    try:
      # Otherwise make all of the variables needed for the game
      tries = dif[0]
      odds = dif[1]
      epsilon = dif[2]
      target = rn.randrange(odds)
    except:
      clear()
      input("bro...\n\nthat wasn't even an option ")
      continue


    clear()
    # Create game loop
    while tries > 0:
      # Checks what difficulty was selected and prints text accordingly 
      if tries == 1 and type(tries) != bool:
        clear()
        print("You Just Have One Try Left, Make It Count")
      elif type(tries) == bool:
        clear()
        print("You Don't Have To Worry About Time Anymore,\nYou Will Run Out Of Tries When The Universe Dies")
      else:
        clear()
        print(f"You Have {tries} Tries Left")
      
      # Nice columns and input for 'guess'
      print("{: <20} {: <20}".format("\n'QUIT' To Quit", "'RESTART' to Restart\n"))
      guess = input(f"Guess a number between 0 and {odds}: ")

      if guess == "QUIT":
        return
      elif guess == "RESTART":
        break

      # Checks if guess is a number at all, if not restart try
      try:
        guess = int(guess)
      except:
        clear()
        input("bro...\n\nthat wasn't even an option ")
        continue
      
      # Checks for win
      if guess == target:
        clear()
        print(f"Congratulations!!! The Correct Number Was Indeed {target}!")
        print("{: <20} {: <20}".format("\n'QUIT' To Quit", "'RESTART' to Restart\n"))
        giveup = input(">_ ")
        if giveup == "QUIT":
          return
        break
      # Otherwise give feedback to player on how far the guess was above/below the 'target'
      else:
        isClose = abs(target - guess) <= epsilon
        if target > guess and isClose:
          clear()
          input("Close! Your guess was a little too low. ")
        elif target < guess and isClose:
          clear()
          input("Close! Your guess was a little too high. ")
        elif target > guess:
          clear()
          input("Your guess was a too low. ")
        elif target < guess:
          clear()
          input("Your guess was a too high. ")
      # Decrement 'tries' if tries are not infinite 
      if type(tries) != bool:
        tries -= 1
      clear()
    # Checks if game was lost
    if tries == 0:
      clear()
      input("GAME OVER")
    # Otherwise standard restart message
    else:
      clear()
      input("Back To The Top ") 

# Calls main game function
game()