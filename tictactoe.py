print("Rows go from left to right; meaning row numbers go up to down (I.E, the top-most row is 1 and the bottom-most row is 3).\nColumns go up to down meaning column numbers go left to right; left-most column being 1 and right-most column being 3.\n")

def reset_board():
  global first_row
  global second_row
  global third_row
  first_row = ['[ ]','[ ]','[ ]']
  second_row = ['[ ]','[ ]','[ ]']
  third_row = ['[ ]','[ ]','[ ]']

game_over = False
x = '[X]'
o = '[O]'
is_taken = True
replay = True

reset_board()

def replay_func():
  global replay
  global game_over
  play_again = input("Would you like to play again?: ")
  if play_again == 'no' or play_again == 'No' or play_again == 'n':
    replay = False
  elif play_again == 'yes' or play_again == 'Yes' or play_again == 'y':
    game_over = False
    reset_board()
  else:
    print("Answer must be yes or no")

def win_checker():
  global game_over
  all_rows = first_row + second_row + third_row
  for spot in range(0,3):
    if all_rows[spot] == all_rows[spot+3] == all_rows[spot+6] and all_rows[spot] != '[ ]':
      game_over = True
  for spot in range(0,len(all_rows),3):
    if set(all_rows[spot:spot+3]) == {'[X]'} or set(all_rows[spot:spot+3]) == {'[O]'}:
      game_over = True
  if all_rows[0] == all_rows[4] == all_rows[8] and all_rows[0] != '[ ]':
    game_over = True
  if all_rows[6] == all_rows[4] == all_rows[2] and all_rows[6] != '[ ]':
    game_over = True
  elif '[ ]' not in all_rows:
    print("")

def row_checker(num, choice, rownum, player):
  global is_taken
  column = 0
  if int(choice) == num:
    column = input("which number column will your spot be?: ")
    while column.isnumeric() == False:
      print("Must be a number")
      column = input("which number column will your spot be?: ")
    while int(column) <= 0 or int(column) > 3:
      print("Must be from 1 to 3 dumbass")
      column = input("which number column will your spot be?: ")
    if rownum[int(column)-1] != '[ ]':
      print("This spot is already taken, dipshit")
    else:
      rownum[int(column)-1] = player
      is_taken = False

def player_decision(X_or_O):
  while is_taken == True:
    row = input('Which number row will your spot be?: ')
    while row.isnumeric() == False:
      print("Must be a number")
      row = input('Which number row will your spot be?: ')
    while int(row) <= 0 or int(row) > 3:
      print("Number must be from 1 to 3")
      row = input('Which number row will your spot be?: ')
    row_checker(1,row,first_row,X_or_O,)
    row_checker(2,row,second_row,X_or_O,)
    row_checker(3,row,third_row,X_or_O,)
  print(" ".join(first_row))
  print(" ".join(second_row))
  print(" ".join(third_row))

while replay == True:
  print(" ".join(first_row))
  print(" ".join(second_row))
  print(" ".join(third_row))
  while game_over == False:
    player_decision(x)
    is_taken = True
    
    win_checker()
    if game_over == True:
      print('X wins')
      break
    player_decision(o)
    win_checker()
    if game_over == True:
      print('Circle wins')
    is_taken = True
  replay_func()
