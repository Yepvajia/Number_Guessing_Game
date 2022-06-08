import os
import random as rn

def clear():
    command = 'clear' # Use 'clear' for Unix Terminals
    if os.name in ('nt', 'dos'):  # Use 'cls' for Windows Shell
        command = 'cls'
    os.system(command)

levels = [
  ["\n1. Very Easy:", "Unlimited Tries"],
  ["\n2. Easy:", "Five Tries (5)"],
  ["\n3. Medium:", "Five Tries (5)"], 
  ["\n4. Difficult:", "Eight Tries (8)"], 
  ["\n5. Very Difficult:", "Nine Tries (9)"], 
  ["\n6. QUIT:", "Leave The Game"]
]
triesOdds = {
  "1" : [True, 10, 2],
  "2" : [5, 10, 2],
  "3" : [5, 100, 5],
  "4" : [8, 500, 5],
  "5" : [9, 1000, 10],
  "6" : "QUIT",
  "QUIT" : "QUIT"
}

def game():
  while True:
    clear()
    for row in levels:
      print("{: <20} {: <20}".format(*row))
    choice = input("\nPick a difficulty using the number: ")
    dif = triesOdds.get(choice)
    if dif == "QUIT":
      break
    
    try:
      tries = dif[0]
      odds = dif[1]
      epsilon = dif[2]
      target = rn.randrange(odds)
    except:
      clear()
      input("bro...\n\nthat wasn't even an option ")
      continue


    clear()
    while tries > 0:
      if tries == 1 and type(tries) != bool:
        clear()
        print("You Just Have One Try Left, Make It Count")
      elif type(tries) == bool:
        clear()
        print("You Don't Have To Worry About Time Anymore,\nYou Will Run Out Of Tries When The Universe Dies")
      else:
        clear()
        print(f"You Have {tries} Tries Left")
      
      print("{: <20} {: <20}".format("\n'QUIT' To Quit", "'RESTART' to Restart\n"))
      guess = input(f"Guess a number between 0 and {odds}: ")

      if guess == "QUIT":
        return
      elif guess == "RESTART":
        break

      try:
        guess = int(guess)
      except:
        clear()
        input("bro...\n\nthat wasn't even an option ")
        continue

      if guess == target:
        clear()
        print("Despite The Odds You Did, You Mad Man")
        print("{: <20} {: <20}".format("\n'QUIT' To Quit", "'RESTART' to Restart\n"))
        giveup = input(">_ ")
        if giveup == "QUIT":
          return
        break
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
      if type(tries) != bool:
        tries -= 1
      clear()
    if tries == 0:
      clear()
      input("GAME OVER")
    else:
      clear()
      input("Back To The Top ") 

game()