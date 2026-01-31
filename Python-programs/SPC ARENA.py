import random
youdict={"s":1, "p":0, "sc":2 }
reversedict={1:"stone",0:"paper",2:"secissor"}
# This is scorecard
your_score=0
computer_score=0
draws=0
while True:#This is intructions and information
	print("\n Stone Paper Secissor Game")
	print("Type: Stone/Paper/Secissor")
	print("Type q for EXIT")
	computer= random.choice([0,1,2])
	youstr=input("Enter your choice: ").lower()
	if youstr=="q":
		print("Final score ")
		print(f"Your score:{your_score} ")
		print(f"Computer: {computer_score}")
		print(f"Draw:{draws}")
		print("GAME OVER")
		break
		       
	if youstr not in youdict:
		print("INVALID CHOICE , TRY AGAIN")
		continue
		
	you=youdict[youstr]
	print(f"You choose: {reversedict[you]}")
	print(f"Computer choose: {reversedict[computer]}")
	if computer==you:
		print("Its draw ")
		draws+=1
	else:
		if computer==1 and you==0:
			print("You win ")
			your_score+=1
		elif computer==0 and you==1:
			print("You lose")
			computer_score+=1
		elif computer==0 and you==2:
			print("You win ")
			your_score+=1
		elif computer==2 and you==0:
			print("You lose ")
			computer_score+=1
		elif computer==1 and you==2:
			print("You lose")
			computer_score+=1
		elif computer==2 and you==1:
			print("You win")
			your_score+=1
			
		print(f" Score-- You: {your_score}| Computer: {computer_score}| Draws: {draws}")
		# At the end this show your score and progress 
			
			
		
      
	