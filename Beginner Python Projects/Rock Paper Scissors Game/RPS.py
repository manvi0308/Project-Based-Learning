import random
import pyttsx3

# A utility function that will speak or will do live commentory on the game
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
 
# Introduction part of the game
speak('Hello, Welcome to your game, ROCK-PAPER-SCISSORS')    
print(" ---------------------")
print("| Rock Paper Scissors |")
print(" ---------------------")
speak('SO Manvi you will have three choices, rock-paper-scissors, you have to enter R for rock, P for paper, S for scissors')
listCh = ["R", "P", "S"]

# Initially scores of both the players is 0
userScore = 0
computerScore = 0
i = 1

speak('So one player will be you and other one will be a super-smart computer,Play smartly')
speak('How many times you want to play?')
chance = int(input("How many time you want to play (no. of chances): "))

# Running the loop  till the desired chances
while i <= chance:
    
    # choosing a random choice for computer's response
    computerCh = str(random.choice(listCh))

    # taking user's input
    speak('Enter your move, R for Rock, P for Paper, S for Scissors ')
    
    # we are giving liberty to user that he/she can either 
    # use lowercase or uppercase alphabets, coz i have used
    # .upper() function to make it fine
    
    userCh = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
    
    # case where there is tie
    if userCh == computerCh:
        speak('Oops its a tie, your move and computer move is same')
        print("Tie You Both Entered Same")

    # if player enters Rock, there are two possibilities now,
    # either the computer had chosen P or S, now will compare both the cases to find out who is the winner
    
    elif userCh == "R":
        
        print("Computer Enter: ", computerCh)
        if computerCh == "P":
            speak('You lose, Paper covers rock')
            print("👉 You lose! Paper covers Rock")
            
            computerScore += 1
            
        # the case where computer's choice is scissors
        else:
            speak('You win Rock smashes scissors')
            print("👉 You win! Rock smashes Scissors")
            userScore += 1
            
    # if player enters P, in this case too computer might have entered either 
    # R or S
    
    elif userCh == "P":
        print("Computer Enter: ", computerCh)
        
        # where computer chosen scissors
        if computerCh == "S":
            print("👉 You lose! Scissor cut Paper")
            computerScore += 1
        else:
            print("👉 You win! Paper covers Rock")
            userScore += 1

    elif userCh == "S":
        
        print("Computer Enter: ", computerCh)
        
        if computerCh == "R":
            print("👉 You lose! Rock smashes Scissors")
            computerScore += 1
            
        else:
            print("👉 You win! Scissor cut Paper")
            userScore += 1
    else:
        print(":(")

    
    # Displaying scoreboard
    
    speak('')
    speak('Displaying scoreboard for you !!')
    print("\n\t******ScoreBoard******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")

    i += 1


# after the completion of while loop
speak('GAME OVER, hope you enjoyed it')
print("\n\n################################################# Game Over #######################################")
print("*******************************************************************************************************")
if userScore < computerScore:
    speak('Sorry you lose the game, computer win the game')
    print("😭 Sorry You lose the game 😭\n computer win the game with score:", computerScore)
elif userScore == computerScore:
    
    speak('Hey the game is tie, you need to play again')
    print("😅 Game is Tie Play Again 😅")
else:
    speak('Yipee you won the game')
    print("😄 You Win the Game with score:", userScore, "😄")
    
    
# code ends here
# made by github.com/manvi0308

