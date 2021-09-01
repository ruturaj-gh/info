import random
print("\t  $$_Welcome to the snake ,water ,gun game_$$\n")
print("1.snake is denoted by==>s\n2.water is denoted by==>w\n3.gun is denoted by ==>g\n")
print("!Rules--> this is trio game simple and straight forward \n1. if your choice is snake it  will drink water and also it gets shot by gun depends on computer's choice \n2. if your choice is gun it will sink in water and also it will shot the snake \n3.if your choice is water gun will sink in it & snake will drink all that \n")
chances_left=0
l=("s","w","g")
my_point=0
comp_point=0
while chances_left<11:
		c=input("choose s,w,g-->")
		j=random.choice(l)
		if c==j:
			print(" \t \t Tie")
		elif c=="s" and j=="w":
			print("\t you won coz snake drank all that \n")
			my_point+=1			
		elif c=="s" and j=="g":
			print("\t you lose coz your snake shot by a gun \n")
			comp_point+=1
		elif c=="w" and j=="s":
			print("\t you lose coz your water drank by the snake \n")
			comp_point+=1
		elif c=="w" and j=="g":
			print("\t you won coz computers gun drowned in your water \n")
			my_point+=1
		elif c=="g" and j=="s":
			print("\t you won coz you shot that snake \n")
			my_point+=1
		elif c=="g" and j=="w":
			print("\t you lose coz your gun sink in to the water \n")
			comp_point+=1
		else:
			print("\t\t invalid inputs \n")	
		print("chances left",11-chances_left)
		chances_left+=1
		print("your score=",my_point)
		print("comp score=",comp_point)
		
if my_point>comp_point:
		print("\t \t Heyaa! You won")
elif my_point==comp_point:
		print("\t \t Tie!! ooof that was rough")
else:
		print("\t \tOHH!! poor thing you lose try again")					