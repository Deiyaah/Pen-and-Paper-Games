import random
import mysql.connector as sql
import pymysql.cursors
while True:
    print('''

        ========================================================================= 
                      ______                         ____     ______   
             /\      |      |  ******      /\      |      \  |                               
            /  \     |      | |           /  \     |       | |         
           /____\    |______| |          /____\    |       | |____      
          /      \   |   \    |         /      \   |       | |                           
         /        \  |    \   |        /        \  |       | |               
        /          \ |     \   ****** /          \ | ____ /  |______     
            
        ========================================================================= ''')
    print('\nChoose the game you want to play:')
    print('1. Rock-Paper-Scissors(R)','\n2. Hangman(H)','\n3. Tic-Tac-Toe(T)')
    print('\nEnter E to exit Arcade')
    print('\n')

    archade=input('Enter your choice')
    if(archade=='R')or(archade=='r')or(archade=='Rock-Paper-Scissors')or(archade=='H')or(archade=='h')or(archade=='Hangman')or (archade=='T')or(archade=='t')or(archade=='Tic-Tac-Toe'):
    
        if((archade=='R')or(archade=='r')or(archade=='Rock-Paper-Scissors')):
          print('''
        =================================================================================================================================================== 
         ______                            ______               ______   ______   ______         _____                   _____   _____             _____    
        |      |  ******  ****** |   /    |      |     /\      |      | |        |      |       /       ******  *****   /       /         ******  |     |                       
        |      | |      | |      |  /     |      |    /  \     |      | |        |      |      |        |         |    |        |        |      | |     | 
        |______| |      | |      | /  ___ |______|   /____\    |______| |____    |______|  ___  \____   |         |     \____    \____   |      | |_____|  
        |   \    |      | |      | \      |         /      \   |        |        |   \               \  |         |          \        \  |      | |  \         
        |    \   |      | |      |  \     |        /        \  |        |        |    \               | |         |           |        | |      | |   \         
        |     \   ******  ****** |   \    |       /          \ |        |______  |     \        _____/  ******  *****   _____/   _____/   ******  |    \    
                    
        ===================================================================================================================================================
                    
                    ''')
          print('\n---------   ROCK-PAPER-SCISSORS   ---------')
          print('\nRULES OF THE GAME \n \nUser inputs Rock(R)/Paper(P)/Scissors(S) and computer randomly chooses from the same. ')
          print('\nThe outcome of the game is determined by the 3 simple rules:')

          print('\n1.Rock wins against Scissors \n2.Scissors wins against Paper \n3.Paper wins against Rock \n ')


          while True:
              compwin=0
              mywin=0
              user_input=input('Enter your choice: ')

              if(user_input=='Rock'or user_input=='Scissors' or user_input=='Paper'):
                  a=['Rock','Paper','Scissors']
                  comp_choice=random.choice(a)
                  print('Your choice is','|',user_input,'|')
                  print('\nThe computer chooses','|',comp_choice,'|')
                  
                  if((user_input==comp_choice)):
                      print('\nIt is a tie!')
                  
                  elif(user_input=='Rock'or user_input=='R'):
                      if(comp_choice=='Paper'):
                          print('\nComputer wins! \nBetter luck next time!')
                          compwin+=1
                      else:
                          print('\nYou are the winner! \nYou rocked it!')
                          mywin+=1
                  
                  elif((user_input=='Scissors')):
                      if(comp_choice=='Rock'):
                          print('\nComputer wins! \nBetter luck next time!')
                          compwin+=1
                      else:
                          print('\nYou are the winner! \nAmazing')
                          mywin+=1

                  elif(user_input=='Paper'):
                      if(comp_choice=='Scissors'):
                          print('\nComputer wins! \nBetter luck next time!')
                          compwin+=1
                      else:
                          print('\nYou are the winner! \nYou smashed it!')
                          mywin+=1
                          
                  conn=sql.connect(host="localhost",
                                   user="root",
                                   password="squareroot",
                                   db="mysql")
                  if conn.is_connected():
                      print('================================================================')
                      print ('\nPython and MySQL successfully connected')
                      cur=conn.cursor()

                  sq = ('INSERT INTO rps (compwins, mywins,mychoice,compchoice) VALUES (%s, %s, %s, %s)')
                  val = [compwin,mywin,user_input,comp_choice]  
                  cur.execute(sq, val)
                  conn.commit()
                  
                  print('================================================================')    
                  s=input('\nDo you want statistics-Y/N? ')
                  if(s=='Y'):
                      cur.execute('SELECT * FROM rps')
                      myresult = cur.fetchall()
                      print('\nCwin|','Mywin|','Mychoice|','Comchoice')
                      for x in myresult:
                        print(x)
                      
                      cur.execute('select sum(compwins) from rps')
                      myresult = cur.fetchall()
                      for x in myresult:
                        print('\nTotal wins by computer',x)
                      
                      cur.execute('select sum(mywins) from rps')
                      myresult = cur.fetchall()
                      for x in myresult:
                        print('\nMy total wins',x)
                  
                  else:
                      print('Okay! Np')
                      
                  print('================================================================')
                  conti=input('\nDo you want to play Rock-Paper-Scissors again?: y/n ')
                  if(conti=='No' or conti=='n' or conti=='N'):
                      print('\nRock-Paper-Scissors Game exited')
                      break
                  else:
                      continue
              else:
                  print('================================================================')
                  print('\nInput not valid. \nCheck your spelling!')
                


        elif((archade=='H')or(archade=='h')or(archade=='Hangman')):
          import random
          print('''
                    ===========================================================================
          
                    |       |      /\      |\     |  ---   |\          /|      /\      |\     |
                    |       |     /  \     | \    | |      | \        / |     /  \     | \    |
                    |_______|    /____\    |  \   | |    - |  \      /  |    /____\    |  \   |
                    |       |   /      \   |   \  | |    | |   \    /   |   /      \   |   \  |
                    |       |  /        \  |    \ | |    | |    \  /    |  /        \  |    \ |
                    |       | /          \ |     \|  \___/ |     \/     | /          \ |     \|
                    
                    ===========================================================================
                    ''')
               
          print('\nRULES OF THE GAME \n \nThere will be a secret word. \nUser will be given 10 tries to randomly guess letters.   ')
          print('\nIf you guess the word before the ten tries, you win')
          print('Else, the man gets hanged and you lose.')
              

          def get_word():
              choice=input('\nChoose level of difficulty \n1.Easy \n2.Hard \nEnter your choice: ')
              if((choice=='easy')or(choice=='e')):
                  print('\nYour word difficulty is | easy |')
                  fname=open("/Users/mymac/Desktop/PROJECT/easy.txt")
                  yo=fname.readlines()
                  word=[]
                  for i in yo:
                      word=i.split()
                  return random.choice(word)
                  
              else:
                  print('\nYour word difficulty is | hard |')
                  hard=['jazz','python','apologize','situation','republic','awkward','rhythm','jelly','captain','cycle','kiosk',
                        'zombie','strange','quiz','panther','avengers','galaxy','winter','soldier','guardian','infinity','phase',
                        'disney','universe']
                  word=random.choice(hard)
         
              return word.lower()

                  
          def hangman():
              alphabet='abcdefghijklmnopqrstuvwxyz'
              word=get_word()
              letters_guessed=[]
              words_guessed=''
              failed_guess=''
              tries=10
              guessed=False

              print('\nThis word contains',len(word),'letters')
              print(len(word)*'*')
              

              while((guessed==False)and(tries>=0)):
                  print('You have',tries,'tries')
                  print('')
                  guess=input('Enter a letter').lower()

                  if(len(guess)==1):
                      if(guess not in alphabet):
                          print('\nPlease enter an alphabet.')
                      elif(guess in letters_guessed):
                          print('================================================================')
                          print('\nEnter a different letter. This one has already been guessed.')
                      elif(guess in word):
                          print('================================================================')
                          print('\nYou have correctly guessed the letter.Good job!')
                          letters_guessed.append(guess)
                      elif(guess not in word):
                          print('================================================================')
                          print('\nThe given word does not contain this letter.\nTry again.')
                          letters_guessed.append(guess)
                          tries-=1
                      else:
                          print('\nWhat even?')
                          
                  elif(len(guess)==len(word)):
                      if(guess==word):
                          print('================================================================')
                          print('\nBravo!!You have cracked it! \nYou have guessed the word!!')
                          letters_guessed.append(guess)
                          words_guessed=word
                          guessed=True
                      else:
                          print('================================================================')
                          print('\nOops! You have made a mistake. \tTry again')
                          tries-=1
                          print(' ')
                          
                  else:
                      print('================================================================')
                      print('\nEnter letter by letter or the whole word!')
                      

                  progress=''
                  if(guessed==False):
                      for letter in word:
                          if letter in letters_guessed:
                              progress+=letter
                          else:
                              progress+='*'
                      print('')
                      print(progress)
                      
                  if progress==word:
                      print('================================================================')
                      print('\nGame Over. \nThe word has been guessed. YAY')
                      words_guessed=word
                      guessed=True
                      
                  elif tries==0:
                      print('================================================================')
                      print('You have run out of tries and were unable to guess the word. \nHence, you lose. \nBetter luck next time.')
                      print('\nThe word was',word)
                      failed_guess=word
                      break
              
              import mysql.connector as sql
              conn=sql.connect(host="localhost",
                               user="root",
                               password="squareroot",
                               db="mysql")
              if conn.is_connected():
                  print('================================================================')
                  print ('\nPython and MySQL successfully connected')
              cur=conn.cursor()
              
              sql = ('INSERT INTO hangman (wordgss,failgss) VALUES (%s, %s)')
              val = [words_guessed,failed_guess]  
              cur.execute(sql, val)
              conn.commit()
              
              sta=input('\nDo you want statistics-Y/N? ')
              
              if(sta=='Y'):
                  cur.execute('SELECT * FROM hangman')
                  myresult = cur.fetchall()
                  print('\nWrdgss|','Failgs')
                  for x in myresult:
                      print(x)
              else:
                  print('Okay!')
                  
              again()

          def again():
              print('================================================================')
              re=input('\nDo you want to play Hangman again? Y/N').lower()
              if re=='y' or re=='yes':
                  hangman()
              else:
                  print('\nHangman Game exited')
                  pass
                  
          hangman()
          
            
        elif((archade=='T')or(archade=='t')or(archade=='Tic-Tac-Toe')):
          print('''
                   ==========================================================================================
                   
                    *******  *******  *******     *******      /\      *******     *******  *******  *******
                       |        |     |              |        /  \     |              |    |       | |
                       |        |     |       ___    |       /****\    |       ___    |    |       | |____
                       |        |     |              |      /      \   |              |    |       | |
                       |        |     |              |     /        \  |              |    |       | |
                       |     *******  *******        |    /          \ *******        |     *******  *******
                       
                   ========================================================================================== ''')
          
          import mysql.connector as sql
          print('\n---------   TIC-TAC-TOE   ---------')
          print('\nRULES OF THE GAME \n \nThe game is played by 2 individuals, on a grid that is 3x3. ')
          print('\nPlayer1 is X and Player2 is O.')
          print('The players take turns in placing their marks in empty squares of the grid.')
          print('\nEach square in the grid is numbered.The player can make their move using the numbers which represent the square.')
          print('\nThe first player to get 3 of their marks in a row, whether it be \nup \ndown \nacross \ndiagonal')
          print('\nIf none manage to get their marks 3 in a row.')
          print('It is a tie!')
          print('\n======================================')
          print('\n')

          board = {7:'_',8:'_',9:'_',
                   4:'_',5:'_',6:'_',
                   1:'_',2:'_',3:'_'}

          print(' ',' 7 ','|','  8',' ','|',' 9','')
          print('     ','|','     ','|')
          print('______+_______+______')
          print(' ',' 4 ','|','  5',' ','|',' 6','')
          print('     ','|','     ','|')
          print('______+_______+______')
          print(' ',' 1 ','|','  2',' ','|',' 3','',)
          print('     ','|','     ','|')
              
          def gameboard():
              print('')
              print('    '+board[7]+'  '+'|'+'    '+board[8]+'   '+'|'+' '+board[9]+' ')
              print('       '+'|'+'        '+'|')
              print('_______+________+______')
              print('    '+board[4]+'  '+'|'+'    '+board[5]+'   '+'|'+' '+board[6]+' ')
              print('       '+'|'+'        '+'|')
              print('_______+________+______')
              print('    '+board[1]+'  '+'|'+'    '+board[2]+'   '+'|'+' '+board[3]+' ')
              print('       '+'|'+'        '+'|')

          def xo_win_check():
              #cases for 'x'
              if(board[1]==board[2]==board[3]=='X'):
                  return 1
              elif(board[4]==board[5]==board[6]=='X'):
                  return 1
              elif(board[7]==board[8]==board[9]=='X'):
                  return 1 
              elif(board[1]==board[5]==board[9]=='X'):
                  return 1 
              elif(board[7]==board[5]==board[3]=='X'):
                  return 1 
              elif(board[7]==board[4]==board[1]=='X'):
                  return 1 
              elif(board[9]==board[6]==board[3]=='X'):
                  return 1
              elif(board[8]==board[5]==board[2]=='X'):
                  return 1 
              
              #cases for 'o'
              
              elif(board[1]==board[2]==board[3]=='O'):
                  return 2 
              elif(board[4]==board[5]==board[6]=='O'):
                  return 2
              elif(board[7]==board[8]==board[9]=='O'):
                  return 2 
              elif(board[1]==board[5]==board[9]=='O'):
                  return 2
              elif(board[7]==board[5]==board[3]=='O'):
                  return 2 
              elif(board[7]==board[4]==board[1]=='O'):
                  return 2 
              elif(board[9]==board[6]==board[3]=='O'):
                  return 2
              elif(board[8]==board[5]==board[2]=='O'):
                  return 2
              else:
                  return 0
                  print('Game Over \nIt is a tie')
                  
          def tictactoe():
              xwin=0
              owin=0
              player=1
              total_moves = 0
              end_check = 0
              while True:
                  end_check=xo_win_check()
                  if(total_moves==9):
                      gameboard()
                      print('It is a tie!')
                      print('Game Over')
                      break
                  
                  elif(end_check==1):
                      print('======================================')
                      print('\nX is the winner','\nGame Over')
                      xwin+=1
                      break
                  
                  elif(end_check==2):
                      print('======================================')
                      print('\nO is the winner','\nGame Over')
                      owin+=1
                      break
                      
                  while True:
                      print('\n')
                      gameboard()
                      if(player==1):
                          x_input=int(input('Player1,enter your move: '))
                          if((x_input in board)and(board[x_input]=='_')):
                              board[x_input]='X'
                              player=2
                              break
                          elif(x_input not in board):
                              print('======================================')
                              print('\nYour input is invalid')
                              continue
                          elif(board[x_input]!='_'):
                              print('======================================')
                              print('\nThe place has been taken already')
                              continue
                          else:
                              print('gah')
                              
                              
                      else:
                          o_input=int(input('Player2,enter your move: '))
                          if((o_input in board)and(board[o_input]=='_')):
                              board[o_input]='O'
                              player=1
                              break
                          elif(o_input not in board):
                              print('======================================')
                              print('\nYour input is invalid','\nEnter a number from 1-9.')
                              continue
                          elif(board[o_input]!='_'):
                              print('======================================')
                              print('\nThe place has been taken already')
                              continue
                          else:
                              print('gah')
                  
                  total_moves+=1
                  
              import mysql.connector as sql
              conn=sql.connect(host='localhost',
                               user='root',
                               password='squareroot',
                               db='mysql')
              if conn.is_connected():
                  print ('\nPython and MySQL successfully connected')
                  cur=conn.cursor()
                  
              sql = ('INSERT INTO ttt(xwin,owin,tmoves) VALUES (%s, %s, %s)')
              val = [xwin,owin,total_moves]
              cur.execute(sql, val)
              conn.commit()
              s=input('\nDo you want statistics-Y/N? ')
              if((s=='Y')or(s=='y')or(s=='yes')):
                  cur.execute('SELECT * FROM ttt')
                  myresult = cur.fetchall()
                  print('\nxwin|','owin|','tmoves')
                  for x in myresult:
                      print(x)
                      
                  cur.execute('select sum(xwin) from ttt')
                  myresult = cur.fetchall()
                  for x in myresult:
                      print('\ntotal wins by X',x)
                      
                  cur.execute('select sum(owin) from ttt')
                  myresult = cur.fetchall()
                  for x in myresult:
                      print('total wins by O',x)
              else:
                  print('Okay!')
              
              replay()
                      
          def replay():    
              replay=input('\nDo you want to play Tic-Tac-Toe again? \ny/n')
              if(replay=='y' or replay=='Y' or replay=='yes'):
                  for key in board:
                      board[key]='_'
                  tictactoe()
              else:
                  print('\nTic-Tac-Toe Game exited')
                  pass
              
          tictactoe()

        print('=====================================================')          
        hello=input('\nDo you want to continue playing games? y/n ')
        if((hello=='n')or(hello=='N')or(hello=='no')or(hello=='n ')):
            print('=====================================================')    
            print('Arcade Exited')
            break
        
        else:
            pass
    elif(archade=='e'):
        print('=====================================================')    
        print('Arcade Exited')
        break
    else:
        print('\n | WRONG GAME CODE |')
        

        

