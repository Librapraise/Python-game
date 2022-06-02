import random
ScoreAi = 0
ScorePlayer = 0
while True:
  print('Hi player one, you can either be')
  print('r for Rock')
  print('p for Paper')
  print('s for Scissors')
  PlayerOne = input('Pick r, p, or s. ')
  Computer = random.choice(['r', 'p', 's'])
  print('The Computer chose ' + str(Computer))
  if PlayerOne == Computer:
    print('It is a tie!')
    ScoreAi = ScoreAi + 1
    ScorePlayer = ScorePlayer + 1
  elif PlayerOne == 'r' and Computer == 'p':
    print(' Computers Paper beats your rock! You lose! ')
    ScoreAi = ScoreAi + 1
   
  elif PlayerOne == 'r' and Computer == 's':
    print('Your Rock beats Computers scissors! You win!')
    ScorePlayer = ScorePlayer + 1
   
  elif PlayerOne == 'p' and Computer == 's':
    print('Computers Scissors beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
    
  elif PlayerOne == 'p' and Computer == 'r':
    print('Your Paper beats Computers rock! You Win!')
    ScorePlayer = ScorePlayer + 1
    
  elif PlayerOne == 's' and Computer == 'p':
    print('Your Scissors beats Computers paper! You Win!')
   
  elif PlayerOne == 's' and Computer == 'r':
    print('Computers Rock beats your paper! You Lose!')
    ScoreAi = ScoreAi + 1
    
  print('Do you want to keep playing?')
  print('1) Yes')
  print('2) No')
  Choice = input('Choose 1 or 2.')

  if Choice == '2':
    print('You won ' + str(ScorePlayer) + ' games and the computer won ' + str(ScoreAi) + ' games.')
    if ScorePlayer > ScoreAi:
      print('Congratulations! You win!')
    elif ScorePlayer < ScoreAi:
      print('The computer won most of the games. You lose!')
    else:
      print('Tie!')
    print('Thank you for playing!')
    break
