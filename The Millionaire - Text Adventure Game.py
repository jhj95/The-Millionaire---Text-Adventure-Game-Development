#!/usr/bin/env python
# coding: utf-8

# ***
# ***
# 
# 
# <br><h2>Text Adventure Game Development |       Who Wants To Be A Millionaire</h2>
# <h4>MSc in Business Analytics           |       Data Science : Python</h4>
# <br>Jorge Hernández Jiménez - Marketing Analyst<br>
# Hult International Business School<br>
# 
# <a href="https://github.com/jhj95">GitHub</a> <br>
# <a href="https://www.linkedin.com/in/jorge-hernandez-jimenez/">LinkedIn</a><br><br><br>
# 
# ***
# ***

# <img src = "img/millionaire.png" style ="width:1110px;height:583px"/>

# <br>

# In[6]:


####################################################################################################
############################### WHO WANT TO BE A MILLIONAIRE? ######################################
####################################################################################################

"""
My name is Jorge Hernández Jiménez and this is my first project working with Python (10/12/2019). 
I have never coded before. After two weeks since I started to study Python at Hult International 
Business School in San Francisco, I have created a text adventure game based on the TV Show: 
Who Want to be a Millionaire? During the game, the player have to answer three different questions 
that are selected randomly from a list of five questions. Every time the player get an asnwer write
he/she can decide if continue with the game and put in risk all its money or finish the game and 
get the money he/she just won.

I would have like to put some audios like the sound of the roulette spinning. I got a code to can 
do it in a different cell but I could not define it and insert in this code. The code I used was:

from IPython.display import Audio, Image, YouTubeVideo
roulette_spin = 'sounds/roulette.mp3'
Audio(data = roulette_spin, autoplay = True)


"""


# Importing packages
import sys
import time
import random
import numpy as np


# Import sys and time in order to use a function that when printing do it as tyerwirtter. 
# I call this function slow_print and it sustitutes the function print() in this code:

def slow_print(text):
    #Making slow_print global
    global slow_print
    for word in text:
        sys.stdout.write(word)
        sys.stdout.flush( )
        time.sleep(0.05) #this control the speed to print the text

        

#############################################################################################
# Here start the first stage of my game map: INTRODUCTION (welcome, step_1, step_2 and step_3)
#############################################################################################

# Defining welcome which starts the game:
def welcome():
    
    # Host's welcoming:
    welcome_title()
    slow_print('\n\n The biggest Game Show ever seen in TV. Where your dreams come true.\n' +
               """Today the prize is $45M, YES, I'm saying it right:\n\n""" +
               '\t    FOURTY FIVE F***ING MILLION DOLLARS.\n\n' +
               'Today we have a new candidate\n' +
               """What's your name my dear?""")

    # Input the name of the player (player_name), and doing it global varaible:
    global player_name
    player_name = input(prompt = 'Write here your name: \n')
    #Capitalizing the input so first letter is always capital letter and looks more formal 
    player_name = player_name.capitalize()

    # The host welcome the player and ask for confirmation to play
    slow_print('\n WELCOME ' + player_name + '!\n'+
               'Do you want to win $50M ' + player_name + "?\n")
    step_1() #Calling step_1()



# Defining step_1. The player input yes/no to start playing (yes) or finish the game (no)
def step_1():
    
    # Input a boolean confirming want to participate the game:
    answer_1 = input(prompt = 'Write: Yes or No\n')
    answer_1 = answer_1.lower() #Making the input lower-case to simplify the code
    
    if answer_1 == 'yes' or answer_1 == 'y' or answer_1 == 'sure':
        slow_print("""\n\t\t THEN LET'S PLAY THE GAME !!!""")
        step_2() #Calling step_2
    
    elif answer_1 == 'no' or answer_1 == 'n':
        slow_print("\n\t Then what are you doing here my friend?\n" +
                   "\t\t NEXT CANDIDATE! \n")
        
    # This else is in case the player write something different than yes or no, the game give them 
    # other opportunity to re-enter the right input
    else:
        slow_print('Are you sure you answered the question?')
        step_1()
        



# Defining step_2 where the host ask the player if he knows about the wheel of fortune:
def step_2():
    
    # The host explain the game
    slow_print('\n\n So ' + player_name + ', what we have prepared here for you today, is:\n\n' +
               '\t\t  THE WHEEL OF FORTUNE\n\n Do you know what it is?\n') 

    # Input a boolean about knowing what the wheel of fortune is:
    answer_2 = input(prompt = 'Write: Yes or No\n')
    answer_2 = answer_2.lower() #Making the input lower-case to simplify the code
    
    # In this input don´t really matter what the player write, the host explain it anyways:
    if answer_2 == 'yes' or answer_2 == 'y' or answer_2 == 'sure':
        slow_print("""\n That's good buddy. Anyways I'm going to explain it for if\n""" +
                   """someone in the audience doesn't.\n""")
        step_3()
        
    elif answer_2 == 'no' or answer_2 == 'n':
        slow_print("\n\t    NO PROBLEM! I'll explain it for you.\n")
        step_3()
        
    # This else is in case the player write something different than yes or no, the game give them 
    # other opportunity to re-enter the right input
    else:
        slow_print('Are you sure you answered the question?')
        step_2()



# Defining step_3 where the host explain the game and give the player the opportunity to hear the 
# explanation all the times he want:
def step_3():
    
    # The wheel of fortune explanation:
    slow_print("\n So the wheel of fortune consists on a set of 5 different questions\n" +
        "from which we will choose 3 of them. Each question has a prize of $15M \n" +
        "and once you get right a question, you win $15M. Then you have to decide \n" +
        "if continue playing and try to get the next question or you can go home \n" +
        "with the money you just won.\n\n" +
        "\t\t BUT LISTEN CAREFULLY " + player_name.upper() + '!\n\n' +
        "If you decide to continue playing and you fail the next question, \n" +
        "you will have to go home with nothing in your wallet, did you understand?\n")

    
    # Input a boolean about understanding the game:
    answer_3 = input(prompt = 'Write Yes or No \n')
    answer_3 = answer_3.lower() #Making the input lower-case to simplify the code
    
    
    # Creating a while that re-explain the wheel of fortune in case the player don´t understand it:
    while answer_3 != 'yes' and answer_3 != 'y' and answer_3 != 'sure':
        slow_print('\n No problem I will explain it once more for you.\n')
        step_3()
        
    if answer_3 == 'yes' or answer_3 == 'y' or answer_3 == 'sure':
        slow_print("""\n\t\t THEN LET'S SPIN THE ROULETTE \n""")
        step_4()





#######################################################################################
# Here start the second stage of my game map: 1st Question (step_4 and step_5)
#######################################################################################

# Defining the step_4 where the game do a roulette to select three question from a list of five 
# questions, using a random selection with the package numpy and the function random.sample
def step_4():
    
    # Starting the game:
    slow_print('\n So now Lisa is going to spin the roulette three times and the numbers \n' +
               """she gets, will be your questions. LET'S GO LISA!\n\n""")

    slow_print('\n\t\t SPIN THE ROULETTE\n')
    
    slow_print('\n\n AND THE QUESTIONS ARE ...\n\n')

    
    # Selecting the questions randomly:

    #Creating a list for the randomly selected questions, and doing it global:
    global questions_numbers
    questions_numbers = []

    
    #Random the questions (x3) using np.random.sample
    question = random.sample(range(1,5),3)

    
    # For loop to append the random selected questions
    for x in range(3):
        if question[x] == 1:
            questions_numbers.append('Question 1 \t') # .append we add the random selected  
                                                      # question to questions_numbers
        elif question[x] == 2:                        
            questions_numbers.append('Question 2 \t')
            
        elif question[x] == 3:
            questions_numbers.append('Question 3 \t')
            
        elif question[x] == 4:
            questions_numbers.append('Question 4 \t')
            
        elif question[x] == 5:
            questions_numbers.append('Question 5 \t')

            
    #Printing the questions selected
    slow_print('Questions order: ')
    slow_print(questions_numbers)    
    
    
    # Defining the variables question_x:
    question_1 = ("""\n The topic is programming. And it says:\n""" + 
                "Who was the creator of the python language in 1989?\n\n" +
                "A) Steve Jobs                B) Guido van Rossum \n" + 
                "C) John Python               D) Robert Downey Jr \n")

    question_2 = ("\n The topic is cinematography. And it says: \n" + 
                 "How did Spider-Man get his power? \n\n" + 
                 "A) Military experiment      B) Born with them \n" + 
                 "   gone away \n" +
                 "C) Woke with them after     D) Bitten by a \n" +
                 "   a strange dream             radioactive spider \n")

    question_3 = ("\n The topic is sports. And it says: \n" +
                 "How many holes are on a standard bowling ball? \n" + 
                 "A) 2                        B) 3 \n" +
                 "C) 5                        D) 10 \n")

    question_4 = ("\n The topic is sports. And it says: \n" + 
                 "How many rings are on the Olympic flag? \n" +
                 "A) None                     B) 4 \n" +
                 "C) 5                        D) 7 \n")

    question_5 = ("\n The topic is history. And it says: \n" +
                 "Which mammal first reached Earth's orbit alive? \n" +
                 "A) Human                    B) Monkey \n" +
                 "C) Cat                      D) Dog \n")

    
    
    # Create a list with all the questions, all_questions, and doing it global:
    global all_questions
    all_questions = [question_1, question_2, question_3, question_4, question_5]

    
    # Defining the variable answer_question_x, these are the answers to the questions:
    answer_question_1a = 'b' 
    answer_question_1b = 'guido van rossum'

    answer_question_2a = 'd'
    answer_question_2b = 'bitten by a radioactive spider'

    answer_question_3a = 'b'
    answer_question_3b = '3' # making the variable a string; it's not necessary, but I did it

    answer_question_4a = 'c'
    answer_question_4b = '5'

    answer_question_5a = 'b'
    answer_question_5b = 'monkey'

    
    # Create a list with all the answers, all_answers, and doing it global:
    global all_answers
    all_answers = [answer_question_1a, answer_question_1b, answer_question_2a, answer_question_2b,
                   answer_question_3a, answer_question_3b, answer_question_4a, answer_question_4b,
                   answer_question_5a, answer_question_5b]
    
    
    # The host start with the first questions:
    slow_print("""\n\n LET'S START WITH THE FIRST QUESTION!!! \n\n""")

    
    # Ask the first question based on the random selection:
    if questions_numbers[0] == 'Question 1 \t':
        slow_print(all_questions[0])
        
    elif questions_numbers[0] == 'Question 2 \t':
        slow_print(all_questions[1])
        
    elif questions_numbers[0] == 'Question 3 \t':
        slow_print(all_questions[2])
        
    elif questions_numbers[0] == 'Question 4 \t':
        slow_print(all_questions[3])
        
    else:
        slow_print(all_questions[4])

        
    # Input the answer of the first question:
    answer_4 = input(prompt= '\n Write your answer here. Just write the letter of' +
                             'the answer (A,B,C,D):')
    answer_4 = answer_4.lower() #Making the input lower-case to simplify the code
    
    
    # Variable for right answer:
    win_1 = ("\n AND THE ANSWER IS RIGHT!! YOU WIN $15M " + player_name.upper() + "\n\n" +
             "\t\t CONGRATULATIONS MY FRIEND!\n\n")
    
    
    # Variable for wrong answer, global variable:
    global lose
    lose = ("\n OHHHHH, that is not the answer " + player_name + ". I'm so sorry my friend. \n" +
            """Today you won't become a Millionaire. \n""")


    # We create a conditional to see if the answer has been correct using the list all_answers:
    if questions_numbers[0] == 'Question 1 \t' and answer_4 == all_answers[0] or answer_4 == all_answers[1]:
        slow_print(win_1)
        step_5()
        
    elif questions_numbers[0] == 'Question 2 \t' and answer_4 == all_answers[2] or answer_4 == all_answers[3]:
        slow_print(win_1)
        step_5()
        
    elif questions_numbers[0] == 'Question 3 \t' and answer_4 == all_answers[4] or answer_4 == all_answers[5]:
        slow_print(win_1)
        step_5()
        
    elif questions_numbers[0] == 'Question 4 \t' and answer_4 == all_answers[6]  or answer_4 == all_answers[7]:
        slow_print(win_1)
        step_5()
        
    elif questions_numbers[0] == 'Question 5 \t' and answer_4 == all_answers[8] or answer_4 == all_answers[9]:
        slow_print(win_1)
        step_5()
        
    # Here the game finish for the player who put the wrong answer
    else:
        slow_print(lose)
        game_over()



# Defining step_5 where once the player got right the first question, he can decide to continue 
# or finish the game:
def step_5():
    
    # Ask the player if he want to continue playing or go home:
    slow_print('Now, ' + player_name + ' you are already a Millionaire. Do you want to'
               'continue, \n  and try to get the $30M?')
    
    answer_5 = input(prompt = 'Write: Yes or No\n')
    answer_5 = answer_5.lower() #Making the input lower-case to simplify the code

    if answer_5 == 'yes' or answer_5 == 'y' or answer_5 == 'sure':
        slow_print("""\n\t\t THEN LET'S CONTINUE PLAYING\n""")
        step_6()

    elif answer_5 == 'no' or answer_5 == 'n':
        slow_print("\n\t Okay, then this has been all for today my friends,\n"
              "\t\t I'll see you all next week!\n")
        win_15()
        
    # This else is in case the player write something different than yes or no, the game give them 
    # other opportunity to re-enter the right input
    else:
        slow_print('Are you sure you answered the question?')
        step_5()





#######################################################################################
#Here start the third stage of my game map: 2nd Question (step_6 and step_7)
#######################################################################################


# Defining step_6 where the host asks the second randomly selected question: 
def step_6():

    # The host ask the second question:
    print("""\n LET'S GO WITH THE SECOND QUESTION!!!""")

    
    # Ask the second question based on the random selection:
    if questions_numbers[1] == 'Question 1 \t':
        slow_print(all_questions[0])
        
    elif questions_numbers[1] == 'Question 2 \t':
        slow_print(all_questions[1])
        
    elif questions_numbers[1] == 'Question 3 \t':
        slow_print(all_questions[2])
        
    elif questions_numbers[1] == 'Question 4 \t':
        slow_print(all_questions[3])
        
    else:
        slow_print(all_questions[4])

        
    # Input the answer of the first question
    answer_6 = input(prompt= 'Write your answer here. Just write the letter of' +
                             'the answer (A,B,C,D):')
    answer_6 = answer_6.lower() #Making the input lower-case to simplify the code
    
    
    # Variable for right answer:
    win_2 = ("\n AND THE ANSWER IS RIGHT!! YOU WIN $30M " + player_name.upper() + "\n" +
             "\n\t\t CONGRATULATIONS MY FRIEND!\n")

    
    # We create a conditional to see if the answer has been correct using the list all_answers:
    if questions_numbers[1] == 'Question 1 \t' and answer_6 == all_answers[0] or answer_6 == all_answers[1]:
        slow_print(win_2)
        step_7()
        
    elif questions_numbers[1] == 'Question 2 \t' and answer_6 == all_answers[2] or answer_6 == all_answers[3]:
        slow_print(win_2)
        step_7()
        
    elif questions_numbers[1] == 'Question 3 \t' and answer_6 == all_answers[4] or answer_6 == all_answers[5]:
        slow_print(win_2)
        step_7()
        
    elif questions_numbers[1] == 'Question 4 \t' and answer_6 == all_answers[6] or answer_6 == all_answers[7]:
        slow_print(win_2)
        step_7()
        
    elif questions_numbers[1] == 'Question 5 \t' and answer_6 == all_answers[8] or answer_6 == all_answers[9]:
        slow_print(win_2)
        step_7()
        
    # Here the game finish for the player who put the wrong answer
    else:
        slow_print(lose)
        game_over()



# Defining step_7 where once the player got right the first question, he can decide to continue or 
# finish the game:        
def step_7():

    # Ask the player if he want to continue playing or go home:
    slow_print('\n Now, ' + player_name + ' you are already a Millionaire. Do you want ' +
               'to continue, \n and try to get the $45M?')
    answer_7 = input(prompt = 'Write: Yes or No\n')
    answer_7 = answer_7.lower() #Making the input lower-case to simplify the code
    
    if answer_7 == 'yes' or answer_7 == 'y' or answer_7 == 'sure':
        slow_print("""\n\t\t THEN LET'S CONTINUE PLAYING\n""")
        step_8()

    elif answer_7 == 'no' or answer_7 == 'n':
        slow_print("\n\t Okay, then this has been all for today my friends,\n" +
                   "\t\t I'll see you all next week!\n")
        win_30()
        
    # This else is in case the player write something different than yes or no, the game give them 
    # other opportunity to re-enter the right input
    else:
        slow_print('Are you sure you answered the question?')
        step_7()





#############################################################################
# Here start the fourth stage of my game map: 3rd Question (step_8)
#############################################################################

# Defining step_8 where the host asks the third randomly selected question: 
def step_8():
    
     # The host ask the third question:
    slow_print("""\n LET'S GO WITH THE THIRD QUESTION!!!""")

    # Ask the third  question based on the random selection:
    if questions_numbers[2] == 'Question 1 \t':
        slow_print(all_questions[0])
        
    elif questions_numbers[2] == 'Question 2 \t':
        slow_print(all_questions[1])
        
    elif questions_numbers[2] == 'Question 3 \t':
        slow_print(all_questions[2])
        
    elif questions_numbers[2] == 'Question 4 \t':
        slow_print(all_questions[3])
        
    else:
        slow_print(all_questions[4])
 

    # Input the answer of the first question
    answer_8 = input(prompt = 'Write your answer here. Just write the letter of' + 
                              'the answer (A,B,C,D):')
    answer_8 = answer_8.lower() #Making the input lower-case to simplify the code
    
    
    # Variable for right answer:
    win_3 = ("\n AND THE ANSWER IS RIGHT!! YOU WIN $45M " + player_name.upper() + "\n" +
             "\n\t\t CONGRATULATIONS MY FRIEND!")

    
    # We create a conditional to see if the answer has been correct using the list all_answers:
    # After this, the game finishes!
    if questions_numbers[2] == 'Question 1 \t' and answer_8 == all_answers[0] or answer_8 == all_answers[1]:
        slow_print(win_3)
        win_45()
        
    elif questions_numbers[2] == 'Question 2 \t' and answer_8 == all_answers[2] or answer_8 == all_answers[3]:
        slow_print(win_3)
        win_45()
        
    elif questions_numbers[2] == 'Question 3 \t' and answer_8 == all_answers[4] or answer_8 == all_answers[5]:
        slow_print(win_3)
        win_45()
        
    elif questions_numbers[2] == 'Question 4 \t' and answer_8 == all_answers[6] or answer_8 == all_answers[7]:
        slow_print(win_3)
        win_45()
        
    elif questions_numbers[2] == 'Question 5 \t' and answer_8 == all_answers[8] or answer_8 == all_answers[9]:
        slow_print(win_3)
        win_45()
        
    # Here the game finish for the player who put the wrong answer
    else:
        slow_print(lose)
        game_over()


# All the next fonts are copied from: http://www.patorjk.com/software/taag/#p=display&f
# =Graffiti&t=Type%20Something%20
# Defining welcome_title; which print a cool text to welcome the player:
def welcome_title():
    print("""
   __          ________ _      _____ ____  __  __ ______   _______ ____                               
   \ \        / /  ____| |    / ____/ __ \|  \/  |  ____| |__   __/ __ \                              
    \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__       | | | |  | |                             
     \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|      | | | |  | |                             
      \  /\  /  | |____| |___| |___| |__| | |  | | |____     | | | |__| |                             
  _____\/ _\/  _|______|______\_____\____/|_| _|_|______|_ __|_| _\____/        _____ _____  ______ _ 
 |__   __| |  | |  ____| |  \/  |_   _| |    | |    |_   _/ __ \| \ | |   /\   |_   _|  __ \|  ____| |
    | |  | |__| | |__    | \  / | | | | |    | |      | || |  | |  \| |  /  \    | | | |__) | |__  | |
    | |  |  __  |  __|   | |\/| | | | | |    | |      | || |  | | . ` | / /\ \   | | |  _  /|  __| | |
    | |  | |  | | |____  | |  | |_| |_| |____| |____ _| || |__| | |\  |/ ____ \ _| |_| | \ \| |____|_|
    |_|  |_|  |_|______| |_|  |_|_____|______|______|_____\____/|_| \_/_/    \_\_____|_|  \_\______(_)
                                                                                                      
                                                                                                      
""")
    

    
    
# Defining win_15, using a cool text for when the players decide to finish the game after 
# accerting 1st question: 
def win_15():
    slow_print("""\n\n
   _   _   _     _   _   _     _   _   _     _     _   _   _  
  / \ / \ / \   / \ / \ / \   / \ / \ / \   / \   / \ / \ / \ 
 ( Y | O | U ) ( W | I | N ) ( $ | 1 | 5 ) ( M ) ( ! | ! | ! )
  \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/   \_/   \_/ \_/ \_/ 
\n\n""")
    replay()

    
    
    
    
# Defining win_30, using a cool text for when the players decide to finish the game after 
# accerting 2nd question:   
def win_30():
    slow_print("""\n\n
   _   _   _     _   _   _     _   _   _     _     _   _   _  
  / \ / \ / \   / \ / \ / \   / \ / \ / \   / \   / \ / \ / \ 
 ( Y | O | U ) ( W | I | N ) ( $ | 3 | 0 ) ( M ) ( ! | ! | ! )
  \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/   \_/   \_/ \_/ \_/ 
\n\n""")
    replay()

    
    
    

# Defining win_45, using a cool text for the winners:
def win_45():
    slow_print("""\n\n
   _   _   _     _   _   _     _   _   _     _     _   _   _  
  / \ / \ / \   / \ / \ / \   / \ / \ / \   / \   / \ / \ / \ 
 ( Y | O | U ) ( W | I | N ) ( $ | 4 | 5 ) ( M ) ( ! | ! | ! )
  \_/ \_/ \_/   \_/ \_/ \_/   \_/ \_/ \_/   \_/   \_/ \_/ \_/ 
\n\n""")
    replay()

    
    
    
    
# Defining game_over, using a cool text for when the player lose:       
def game_over():
    slow_print("""\n\n
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          
 \n\n""")
    replay()

    

# Defining replay, creating a function so users can play again once they finish:      
def replay():
   
    slow_print('\n\nDo you want to play again ?\n')
    
    # Input a boolean about replaying the game:
    answer_9 = input(prompt = 'Write: Yes or No\n')
    answer_9 = answer_9.lower() #Making the input lower-case to simplify the code
    
    # In this input don´t really matter what the player write, the host explain it anyways:
    if answer_9 == 'yes' or answer_9 == 'y' or answer_9 == 'sure':
        slow_print("""\n That's good folk. LET'S TRY AGAIN!! \n""")
        welcome()
        
    elif answer_9 == 'no' or answer_9 == 'n':
        slow_print("\n\t NO PROBLEM! Have a good day!\n")
        
    # This else is in case the player write something different than yes or no, the game give them 
    # other opportunity to re-enter the right input
    else:
        slow_print('Are you sure you answered the question?')
        replay()


        
        
# Initiating the game:        
welcome()


# In[7]:


from IPython.display import Audio, Image, YouTubeVideo
roulette_spin = 'sounds/roulette.mp3'
Audio(data = roulette_spin, autoplay = True)

