#Wade Willms
#BlackJack Project
from numpy import random
import time
def doubleAceCount():
	global userAces
	global botAces
	global bot2Aces
	global bot3Aces
	global bot4Aces
	global bot5Aces
	global bot6Aces
	global userPlaying
	global botPlaying
	global bot2Playing
	global bot3Playing
	global bot4Playing
	global bot5Playing
	global bot6Playing
	global userSum
	global botSum
	global bot2Sum
	global bot3Sum
	global bot4Sum
	global bot5Sum
	global bot6Sum

	if userPlaying == True:
		if userAces == 2:
			userSum -= 10
			userAces -= 1
	if botPlaying == True:
		if botAces == 2:
			botSum -=10
			botAces -= 1
	if bot2Playing == True:
		if bot2Aces == 2:
			bot2Sum -=10
			bot2Aces -= 1
	if bot3Playing == True:
		if bot3Aces == 2:
			bot3Sum -=10
			bot3Aces -= 1
	if bot4Playing == True:
		if bot4Aces == 2:
			bot4Sum -=10
			bot4Aces -= 1
	if bot5Playing == True:
		if bot5Aces == 2:
			bot5Sum -=10
			bot5Aces -= 1
	if bot6Playing == True:
		if bot6Aces == 2:
			bot6Sum -=10
			bot6Aces -= 1


#---------------------------------- Shuffle ----------------------------------
def Shuffle():
	global DeckNames
	global DeckValues
	global DeckNamesMaster
	global DeckValuesMaster
	if len(DeckNamesMaster) < 28:
		del DeckNamesMaster[:]
		del DeckValuesMaster[:]
		DeckBuilder = 1
		while DeckBuilder < 9:
			DeckNamesMaster = DeckNamesMaster + DeckNames
			DeckValuesMaster = DeckValuesMaster + DeckValues
			DeckBuilder += 1

#-----------------------------------------------------------------------------
#---------------------------------- Stat Reset -------------------------------
def reset():
	global botHand
	global botMoney
	global botSum
	global botBid
	global botTurnsSat
	global botPlaying
	global botKicked
	global botBust
	global botBlackJack
	global bot2Hand
	global bot2Money
	global bot2Sum
	global bot2Bid
	global bot2TurnsSat
	global bot2Playing
	global bot2Kicked
	global bot2Bust
	global bot2BlackJack
	global bot3Hand
	global bot3Money
	global bot3Sum
	global bot3Bid
	global bot3TurnsSat
	global bot3Playing
	global bot3Kicked
	global bot3Bust
	global bot3BlackJack
	global bot4Hand
	global bot4Money
	global bot4Sum
	global bot4Bid
	global bot4TurnsSat
	global bot4Playing
	global bot4Kicked
	global bot4Bust
	global bot4BlackJack
	global bot5Hand
	global bot5Money
	global bot5Sum
	global bot5Bid
	global bot5TurnsSat
	global bot5Playing
	global bot5Kicked
	global bot5Bust
	global bot5BlackJack
	global bot6Hand
	global bot6Money
	global bot6Sum
	global bot6Bid
	global bot6TurnsSat
	global bot6Playing
	global bot6Kicked
	global bot6Bust
	global bot6BlackJack
	global botAces
	global bot2Aces
	global bot3Aces
	global bot4Aces
	global bot5Aces
	global bot6Aces

	global dealerHand
	global dealerFaceUpCard
	global dealerSum
	global dealerBust
	global dealerBlackJack
	global dealerAces

	global userHand
	global userSum
	global userMoney
	global userBid
	global userTurnsSat
	global userPlaying
	global userBust
	global userBlackJack
	global userKicked
	global userAces

#User
	userSum = 0
	userBid = 0
	userBust = False
	userBlackJack = False
	userHand.clear()
	userAces = 0

	if userTurnsSat >= 3:
		userKicked = True
		print("You were kicked for sitting to many turns in a row")
		time.sleep(1)
	if userMoney < 50:
		userKicked = True
		print("You were kicked for not having enough money")
		time.sleep(1)

#bot
	botSum = 0
	botBid = 0
	botBust = False
	botBlackJack = False
	botHand.clear()
	botAces = 0
	if botKicked == False:
		if botTurnsSat >= 3:
			botKicked = True
			print("Roman was kicked for sitting to many turns in a row")
			time.sleep(1)
		if botMoney < 50:
			botKicked = True
			print("Roman was kicked for not having enough money")
			time.sleep(1)
	bot2Sum = 0
	bot2Bid = 0
	bot2Bust = False
	bot2BlackJack = False
	bot2Hand.clear()
	bot2Aces = 0
	if bot2Kicked == False:
		if bot2TurnsSat >= 3:
			bot2Kicked = True
			print("Tina was kicked for sitting to many turns in a row")
			time.sleep(1)
		if bot2Money < 50:
			bot2Kicked = True
			print("Tina was kicked for not having enough money")
			time.sleep(1)
	bot3Sum = 0
	bot3Bid = 0
	bot3Bust = False
	bot3BlackJack = False
	bot3Hand.clear()
	bot3Aces = 0
	if bot3Kicked == False:
		if bot3TurnsSat >= 3:
			bot3Kicked = True
			print("Keith was kicked for sitting to many turns in a row")
			time.sleep(1)
		if bot3Money < 50:
			bot3Kicked = True
			print("Keith was kicked for not having enough money")
			time.sleep(1)
	bot4Sum = 0
	bot4Bid = 0
	bot4Bust = False
	bot4BlackJack = False
	bot4Hand.clear()
	bot4Aces = 0
	if bot4Kicked == False:
		if bot4TurnsSat >= 3:
			bot4Kicked = True
			print("Ryan was kicked for sitting to many turns in a row")
			time.sleep(1)
		if bot4Money < 50:
			bot4Kicked = True
			print("Ryan was kicked for not having enough money")
			time.sleep(1)
	bot5Sum = 0
	bot5Bid = 0
	bot5Bust = False
	bot5BlackJack = False
	bot5Hand.clear()
	bot5Aces = 0
	if bot5Kicked == False:
		if bot5TurnsSat >= 3:
			bot5Kicked = True
			print("John was kicked for sitting to many turns in a row")
			time.sleep(1)
		if bot5Money < 50:
			bo5tKicked = True
			print("John was kicked for not having enough money")
			time.sleep(1)
	bot6Sum = 0
	bot6Bid = 0
	bot6Bust = False
	bot6BlackJack = False
	bot6Hand.clear()
	bot6Aces = 0
	if bot6Kicked == False:
		if bot6TurnsSat >= 3:
			bot6Kicked = True
			print("Karen was kicked for sitting to many turns in a row")
			time.sleep(1)
		if bot6Money < 50:
			bot6Kicked = True
			print("Karen was kicked for not having enough money")
			time.sleep(1)
#Dealer
	dealerSum = 0
	dealerFaceUpCard = 0
	dealerBust = False
	dealerBlackJack = False
	dealerHand.clear()
	dealerAces = 0
#-----------------------------------------------------------------------------
#------------------------------------ Payout ---------------------------------
def payout():
	global userSum
	global userMoney
	global userBid
	global userPlaying
	global userBust
	global userBlackJack
	global botSum
	global botMoney
	global botBid
	global botPlaying
	global botBust
	global botBlackJack
	global bot2Sum
	global bot2Money
	global bot2Bid
	global bot2Playing
	global bot2Bust
	global bot2BlackJack
	global bot3Sum
	global bot3Money
	global bot3Bid
	global bot3Playing
	global bot3Bust
	global bot3BlackJack
	global bot4Sum
	global bot4Money
	global bot4Bid
	global bot4Playing
	global bot4Bust
	global bot4BlackJack
	global bot5Sum
	global bot5Money
	global bot5Bid
	global bot5Playing
	global bot5Bust
	global bot5BlackJack
	global bot6Sum
	global bot6Money
	global bot6Bid
	global bot6Playing
	global bot6Bust
	global bot6BlackJack
	global dealerSum
	global dealerBust
	global dealerBlackJack
	if userPlaying == True:
		if userBlackJack == True:
			userMoney = userMoney + (userBid * 2)
			print("Your new money total is: " + str(userMoney))
			time.sleep(1)
		elif userBust == False and userSum == dealerSum:
			print("You tied Dealer, money returned: " + str(userMoney))
			time.sleep(1)
		elif userBust == True:
			userMoney = userMoney - userBid
			print("Your new money total is: " + str(userMoney))
			time.sleep(1)
		elif userSum > dealerSum and dealerBust == False:
			userMoney = userMoney + userBid
			print("Your new money total is: " + str(userMoney))
			time.sleep(1)
		elif userSum < dealerSum and dealerBust == False:
			userMoney = userMoney - userBid
			print("Your new money total is: " + str(userMoney))
			time.sleep(1)
		elif userBust == False and dealerBust == True:
			userMoney = userMoney + userBid
			print("Your new money total is: " + str(userMoney))
			time.sleep(1)
	if botPlaying == True:
		if botBlackJack == True:
			botMoney = botMoney + (botBid * 2)
			print("Roman's new money total is: " + str(botMoney))
			time.sleep(1)
		elif botBust == False and botSum == dealerSum:
			print("Roman tied Dealer, money returned: " + str(botMoney))
			time.sleep(1)
		elif botBust == True:
			botMoney = botMoney - botBid
			print("Roman's new money total is: " + str(botMoney))
			time.sleep(1)
		elif botSum > dealerSum and dealerBust == False:
			botMoney = botMoney + botBid
			print("Roman's new money total is: " + str(botMoney))
			time.sleep(1)
		elif botSum < dealerSum and dealerBust == False:
			botMoney = botMoney - botBid
			print("Roman's new money total is: " + str(botMoney))
			time.sleep(1)
		elif botBust == False and dealerBust == True:
			botMoney = botMoney + botBid
			print("Roman's new money total is: " + str(botMoney))
			time.sleep(1)
	if bot2Playing == True:
		if bot2BlackJack == True:
			bot2Money = bot2Money + (bot2Bid * 2)
			print("Tina's new money total is: " + str(bot2Money))
			time.sleep(1)
		elif bot2Bust == False and bot2Sum == dealerSum:
			print("Tina tied Dealer, money returned: " + str(bot2Money))
			time.sleep(1)
		elif bot2Bust == True:
			bot2Money = bot2Money - bot2Bid
			print("Tina's new money total is: " + str(bot2Money))
			time.sleep(1)
		elif bot2Sum > dealerSum and dealerBust == False:
			bot2Money = bot2Money + bot2Bid
			print("Tina's new money total is: " + str(bot2Money))
			time.sleep(1)
		elif bot2Sum < dealerSum and dealerBust == False:
			bot2Money = bot2Money - bot2Bid
			print("Tina's new money total is: " + str(bot2Money))
			time.sleep(1)
		elif bot2Bust == False and dealerBust == True:
			bot2Money = bot2Money + bot2Bid
			print("Tina's new money total is: " + str(bot2Money))
			time.sleep(1)
	if bot3Playing == True:
		if bot3BlackJack == True:
			bot3Money = bot3Money + (bot3Bid * 2)
			print("Keith's new money total is: " + str(bot3Money))
			time.sleep(1)
		elif bot3Bust == False and bot3Sum == dealerSum:
			print("Keith tied Dealer, money returned: " + str(bot3Money))
			time.sleep(1)
		elif bot3Bust == True:
			bot3Money = bot3Money - bot3Bid
			print("Keith's new money total is: " + str(bot3Money))
			time.sleep(1)
		elif bot3Sum > dealerSum and dealerBust == False:
			bot3Money = bot3Money + bot3Bid
			print("Keith's new money total is: " + str(bot3Money))
			time.sleep(1)
		elif bot3Sum < dealerSum and dealerBust == False:
			bot3Money = bot3Money - bot3Bid
			print("Keith's new money total is: " + str(bot3Money))
			time.sleep(1)
		elif bot3Bust == False and dealerBust == True:
			bot3Money = bot3Money + bot3Bid
			print("Keith's new money total is: " + str(bot3Money))
			time.sleep(1)
	if bot4Playing == True:
		if bot4BlackJack == True:
			bot4Money = bot4Money + (bot4Bid * 2)
			print("Ryan's new money total is: " + str(bot4Money))
			time.sleep(1)
		elif bot4Bust == False and bot4Sum == dealerSum:
			print("Ryan tied Dealer, money returned: " + str(bot4Money))
			time.sleep(1)
		elif botBust == True:
			bot4Money = bot4Money - bot4Bid
			print("Ryan's new money total is: " + str(bot4Money))
			time.sleep(1)
		elif bot4Sum > dealerSum and dealerBust == False:
			bot4Money = bot4Money + bot4Bid
			print("Ryan's new money total is: " + str(bot4Money))
			time.sleep(1)
		elif bot4Sum < dealerSum and dealerBust == False:
			bot4Money = bot4Money - bot4Bid
			print("Ryan's new money total is: " + str(bot4Money))
			time.sleep(1)
		elif bot4Bust == False and dealerBust == True:
			bot4Money = bot4Money + bot4Bid
			print("Ryan's new money total is: " + str(bot4Money))
			time.sleep(1)
	if bot5Playing == True:
		if bot5BlackJack == True:
			bot5Money = bot5Money + (bot5Bid * 2)
			print("John's new money total is: " + str(bot5Money))
			time.sleep(1)
		elif bot5Bust == False and bot5Sum == dealerSum:
			print("John tied Dealer, money returned: " + str(bot5Money))
			time.sleep(1)
		elif bot5Bust == True:
			bot5Money = bot5Money - bot5Bid
			print("John's new money total is: " + str(bot5Money))
			time.sleep(1)
		elif bot5Sum > dealerSum and dealerBust == False:
			bot5Money = bot5Money + bot5Bid
			print("John's new money total is: " + str(bot5Money))
			time.sleep(1)
		elif bot5Sum < dealerSum and dealerBust == False:
			bot5Money = bot5Money - bot5Bid
			print("John's new money total is: " + str(bot5Money))
			time.sleep(1)
		elif bot5Bust == False and dealerBust == True:
			bot5Money = bot5Money + bot5Bid
			print("John's new money total is: " + str(bot5Money))
			time.sleep(1)
	if bot6Playing == True:
		if bot6BlackJack == True:
			bot6Money = bot6Money + (bot6Bid * 2)
			print("Karen's new money total is: " + str(bot6Money))
			time.sleep(1)
		elif bot6Bust == False and bot6Sum == dealerSum:
			print("Karen tied Dealer, money returned: " + str(bot6Money))
			time.sleep(1)
		elif bot6Bust == True:
			bot6Money = bot6Money - bot6Bid
			print("Karen's new money total is: " + str(bot6Money))
			time.sleep(1)
		elif bot6Sum > dealerSum and dealerBust == False:
			bot6Money = bot6Money + bot6Bid
			print("Karen's new money total is: " + str(bot6Money))
			time.sleep(1)
		elif botSum < dealerSum and dealerBust == False:
			bot6Money = bot6Money - bot6Bid
			print("Karen's new money total is: " + str(bot6Money))
			time.sleep(1)
		elif bot6Bust == False and dealerBust == True:
			bot6Money = bot6Money + bot6Bid
			print("Karen's new money total is: " + str(bot6Money))
			time.sleep(1)
#-------------------------------------------------------------------------------
#---------------------------- Dealer Play --------------------------------------
def dealerPlay():
	global dealerHand
	global dealerSum
	global dealerBust
	global dealerBlackJack
	global dealerAces
	print("Dealer revealed his Facedown Card")
	time.sleep(1)
	print("Dealer Hand: " + str(dealerHand))
	print(" Dealer Total: " + str(dealerSum))
	time.sleep(1)

	while dealerSum < 17:
		x = random.randint(len(DeckNamesMaster))
		dealerHand.append(DeckNamesMaster[x])
		dealerSum = dealerSum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			dealerAces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
		print("The dealer delt himself a card.")
		time.sleep(1)
		print("Dealer Hand: " + str(dealerHand))
		print(" Dealer Total: " + str(dealerSum))
		time.sleep(1)
	if dealerSum > 21:
		if dealerAces > 0:
			dealerAces -= 1
			dealerSum = dealerSum - 10
		else:
			dealerBust = True
			print("The Dealer Bust")
			time.sleep(1)
	if dealerSum == 21:
		dealerBlackJack = True
		print("The Dealer got BlackJack")
		time.sleep(1)
#-------------------------------------------------------------------------------
#---------------------------- Play/Hit/Stand/Double/Bust -----------------------
def playGame():
	global userHand
	global userSum
	global userPlaying
	global userBid
	global userMoney
	global botHand
	global botSum
	global bot2Hand
	global bot2Sum
	global bot3Hand
	global bot3Sum
	global bot4Hand
	global bot4Sum
	global bot5Hand
	global bot5Sum
	global bot6Hand
	global bot6Sum
	global botPlaying
	global bot2Playing
	global bot3Playing
	global bot4Playing
	global bot5Playing
	global bot6Playing
	global botBid
	global botMoney
	global bot2Bid
	global bot2Money
	global bot3Bid
	global bot3Money
	global bot4Bid
	global bot4Money
	global bot5Bid
	global bot5Money
	global bot6Bid
	global bot6Money
	global DeckNamesMaster
	global DeckValuesMaster
	global botBust
	global botBlackJack
	global bot2Bust
	global bot2BlackJack
	global bot3Bust
	global bot3BlackJack
	global bot4Bust
	global bot4BlackJack
	global bot5Bust
	global bot5BlackJack
	global bot6Bust
	global bot6BlackJack
	global userBust
	global userBlackjack
	global botAces
	global bot2Aces
	global bot3Aces
	global bot4Aces
	global bot5Aces
	global bot6Aces
	global userAces
	choice = 0
	if userPlaying == True:
		userContinue = True
	else:
		userContinue = False
	if botPlaying == True:
		botContinue = True
	else:
		botContinue = False
	if bot2Playing == True:
		bot2Continue = True
	else:
		bot2Continue = False
	if bot3Playing == True:
		bot3Continue = True
	else:
		bot3Continue = False
	if bot4Playing == True:
		bot4Continue = True
	else:
		bot4Continue = False
	if bot5Playing == True:
		bot5Continue = True
	else:
		bot5Continue = False
	if bot6Playing == True:
		bot6Continue = True
	else:
		bot6Continue = False





	while userContinue == True or botContinue == True or bot2Continue == True or bot3Continue == True or bot4Continue == True or bot5Continue == True or bot6Continue == True:
		if userContinue == True and userSum != 21:
			print("What would you like to do?")
			print("1.) Hit")
			print("2.) Double")
			print("3.) Stand")
			while choice < 1 or choice > 3:
				choice = int(input("Your choice: "))
			if choice == 1:
				x = random.randint(len(DeckNamesMaster))
				userHand.append(DeckNamesMaster[x])
				userSum = userSum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					userAces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
				choice = 0
			if choice == 2:
				if userBid * 2 < userMoney:
					userBid *= 2
					x = random.randint(len(DeckNamesMaster))
					userHand.append(DeckNamesMaster[x])
					userSum = userSum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						userAces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
					choice = 0
					userContinue = False
				else:
					choice = 0
					print("You don't have enough money")
					print("What would you like to do?")
					print("1.) Hit")
					print("2.) Stand")
					while choice < 1 or choice > 2:
						choice = int(input("Your choice: "))
					if choice == 1:
						x = random.randint(len(DeckNamesMaster))
						userHand.append(DeckNamesMaster[x])
						userSum = userSum + DeckValuesMaster[x]
						if DeckValuesMaster[x] == 11:
							userAces += 1
						DeckNamesMaster.pop(x)
						DeckValuesMaster.pop(x)
						choice = 0
					if choice == 2:
						userContinue = False
			if choice == 3:
				userContinue = False
		if botContinue == True:
			y = random.randint(1, 100)
			if botSum < 12:
				print("Roman Hit")
				time.sleep(1)
				x = random.randint(len(DeckNamesMaster))
				botHand.append(DeckNamesMaster[x])
				botSum = botSum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					botAces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
			elif botSum == 21:
				botBlackJack = True
			elif botSum > 17:
				if y % 2 == 0 and y > 84:
					print("Roman Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					botHand.append(DeckNamesMaster[x])
					botSum = botSum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						botAces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					botContinue = False
			else:
				if y % 2 == 0 and y > 20:
					print("Roman Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					botHand.append(DeckNamesMaster[x])
					botSum = botSum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						botAces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					botContinue = False
		if bot2Continue == True:
			y = random.randint(1, 100)
			if bot2Sum < 12:
				print("Tina Hit")
				time.sleep(1)
				x = random.randint(len(DeckNamesMaster))
				bot2Hand.append(DeckNamesMaster[x])
				bot2Sum = bot2Sum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					bot2Aces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
			elif bot2Sum == 21:
				bot2BlackJack = True
			elif bot2Sum > 17:
				if y % 2 == 0 and y > 84:
					print("Tina Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot2Hand.append(DeckNamesMaster[x])
					bot2Sum = bot2Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot2Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot2Continue = False
			else:
				if y % 2 == 0 and y > 20:
					print("Tina Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot2Hand.append(DeckNamesMaster[x])
					bot2Sum = bot2Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot2Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot2Continue = False
		if bot3Continue == True:
			y = random.randint(1, 100)
			if bot3Sum < 12:
				print("Keith Hit")
				time.sleep(1)
				x = random.randint(len(DeckNamesMaster))
				bot3Hand.append(DeckNamesMaster[x])
				bot3Sum = bot3Sum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					bot3Aces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
			elif bot3Sum == 21:
				bot3BlackJack = True
			elif bot3Sum > 17:
				if y % 2 == 0 and y > 84:
					print("Keith Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot3Hand.append(DeckNamesMaster[x])
					bot3Sum = bot3Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot3Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot3Continue = False
			else:
				if y % 2 == 0 and y > 20:
					print("Keith Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot3Hand.append(DeckNamesMaster[x])
					bot3Sum = bot3Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot3Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot3Continue = False
		if bot4Continue == True:
			y = random.randint(1, 100)
			if bot4Sum < 12:
				print("Ryan Hit")
				time.sleep(1)
				x = random.randint(len(DeckNamesMaster))
				bot4Hand.append(DeckNamesMaster[x])
				bot4Sum = bot4Sum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					bot4Aces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
			elif bot4Sum == 21:
				bot4BlackJack = True
			elif bot4Sum > 17:
				if y % 2 == 0 and y > 84:
					print("Ryan Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot4Hand.append(DeckNamesMaster[x])
					bot4Sum = bot4Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot4Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot4Continue = False
			else:
				if y % 2 == 0 and y > 20:
					print("Ryan Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot4Hand.append(DeckNamesMaster[x])
					bot4Sum = bot4Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot4Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot4Continue = False
		if bot5Continue == True:
			y = random.randint(1, 100)
			if bot5Sum < 12:
				print("John Hit")
				time.sleep(1)
				x = random.randint(len(DeckNamesMaster))
				bot5Hand.append(DeckNamesMaster[x])
				bot5Sum = bot5Sum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					bot5Aces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
			elif bot5Sum == 21:
				bot5BlackJack = True
			elif bot5Sum > 17:
				if y % 2 == 0 and y > 84:
					print("John Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot5Hand.append(DeckNamesMaster[x])
					bot5Sum = bot5Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot5Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot5Continue = False
			else:
				if y % 2 == 0 and y > 20:
					print("John Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot5Hand.append(DeckNamesMaster[x])
					bot5Sum = bot5Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot5Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot5Continue = False
		if bot6Continue == True:
			y = random.randint(1, 100)
			if bot6Sum < 12:
				print("Karen Hit")
				time.sleep(1)
				x = random.randint(len(DeckNamesMaster))
				bot6Hand.append(DeckNamesMaster[x])
				bot6Sum = bot6Sum + DeckValuesMaster[x]
				if DeckValuesMaster[x] == 11:
					bot6Aces += 1
				DeckNamesMaster.pop(x)
				DeckValuesMaster.pop(x)
			elif bot6Sum == 21:
				bot6BlackJack = True
			elif bot6Sum > 17:
				if y % 2 == 0 and y > 84:
					print("Karen Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot6Hand.append(DeckNamesMaster[x])
					bot6Sum = bot6Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot6Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot6Continue = False
			else:
				if y % 2 == 0 and y > 20:
					print("Karen Hit")
					time.sleep(1)
					x = random.randint(len(DeckNamesMaster))
					bot6Hand.append(DeckNamesMaster[x])
					bot6Sum = bot6Sum + DeckValuesMaster[x]
					if DeckValuesMaster[x] == 11:
						bot6Aces += 1
					DeckNamesMaster.pop(x)
					DeckValuesMaster.pop(x)
				else:
					bot6Continue = False
		if userContinue == True:
			if userSum > 21:
				if userAces > 0:
					userSum = userSum - 10
					userAces -= 1
				if userSum > 21:
					userBust = True
					userContinue = False
					print("You Bust")
					time.sleep(1)
			elif userSum == 21:
				print("You got a BlackJack")
				time.sleep(1)
				userBlackJack = True
				userContinue = False
		if botContinue == True:
			if botSum > 21:
				if botAces > 0:
					botAces -= 1
					botSum = botSum - 10
				if botSum > 21:
					botBust = True
					botContinue = False
					print("Roman Bust")
					time.sleep(1)
			elif botSum == 21:
				print("Roman got a BlackJack")
				time.sleep(1)
				botBlackJack = True
				botContinue = False
		if bot2Continue == True:
			if bot2Sum > 21:
				if bot2Aces > 0:
					bot2Aces -= 1
					bot2Sum = bot2Sum - 10
				if bot2Sum > 21:
					bot2Bust = True
					bot2Continue = False
					print("Tina Bust")
					time.sleep(1)
			elif bot2Sum == 21:
				print("Tina got a BlackJack")
				time.sleep(1)
				bot2BlackJack = True
				bot2Continue = False
		if bot3Continue == True:
			if bot3Sum > 21:
				if bot3Aces > 0:
					bot3Aces -= 1
					bot3Sum = bot3Sum - 10
				if bot3Sum > 21:
					bot3Bust = True
					bot3Continue = False
					print("Keith Bust")
					time.sleep(1)
			elif bot3Sum == 21:
				print("Keith got a BlackJack")
				time.sleep(1)
				bot3BlackJack = True
				bot3Continue = False
		if bot4Continue == True:
			if bot4Sum > 21:
				if bot4Aces > 0:
					bot4Aces -= 1
					bot4Sum = bot4Sum - 10
				if bot4Sum > 21:
					bot4Bust = True
					bot4Continue = False
					print("Ryan Bust")
					time.sleep(1)
			elif bot4Sum == 21:
				print("Ryan got a BlackJack")
				time.sleep(1)
				bot4BlackJack = True
				bot4Continue = False
		if bot5Continue == True:
			if bot5Sum > 21:
				if bot5Aces > 0:
					bot5Aces -= 1
					bot5Sum = bot5Sum - 10
				if bot5Sum > 21:
					bot5Bust = True
					bot5Continue = False
					print("John Bust")
					time.sleep(1)
			elif bot5Sum == 21:
				print("John got a BlackJack")
				time.sleep(1)
				bot5BlackJack = True
				bot5Continue = False
		if bot6Continue == True:
			if bot6Sum > 21:
				if bot6Aces > 0:
					bot6Aces -= 1
					bot6Sum = bot6Sum - 10
				if bot6Sum > 21:
					bot6Bust = True
					bot6Continue = False
					print("Karen Bust")
					time.sleep(1)
			elif bot6Sum == 21:
				print("Karen got a BlackJack")
				time.sleep(1)
				bot6BlackJack = True
				bot6Continue = False
		choice = 0
		showHands()
		dealerFaceDown()
#-------------------------------------------------------------------------------
#---------------------------- Dealer Facedown Show -----------------------------
def dealerFaceDown():
	global dealerHand
	global dealerSum
	global dealerFaceUpCard
	print("Dealer Hand: " + str(dealerHand[1]))
	print("Dealer Total: " + str(dealerFaceUpCard))
	time.sleep(1)
#-------------------------------------------------------------------------------
#---------------------------- Show Hands ---------------------------------------
def showHands():
	global userHand
	global userSum
	global userPlaying
	global botHand
	global botSum
	global botPlaying
	global bot2Hand
	global bot2Sum
	global bot2Playing
	global bot3Hand
	global bot3Sum
	global bot3Playing
	global bot4Hand
	global bot4Sum
	global bot4Playing
	global bot5Hand
	global bot5Sum
	global bot5Playing
	global bot6Hand
	global bot6Sum
	global bot6Playing
	if botPlaying == True:
		print("Roman's Hand: " + str(botHand))
		print("Roman's Total: " + str(botSum))
		time.sleep(1)
	if bot2Playing == True:
		print("Tina's Hand: " + str(bot2Hand))
		print("Tina's Total: " + str(bot2Sum))
		time.sleep(1)
	if bot3Playing == True:
		print("Keith's Hand: " + str(bot3Hand))
		print("Keith's Total: " + str(bot3Sum))
		time.sleep(1)
	if bot4Playing == True:
		print("Ryan's Hand: " + str(bot4Hand))
		print("Ryan's Total: " + str(bot4Sum))
		time.sleep(1)
	if bot5Playing == True:
		print("John's Hand: " + str(bot5Hand))
		print("John's Total: " + str(bot5Sum))
		time.sleep(1)
	if bot6Playing == True:
		print("Karen's Hand: " + str(bot6Hand))
		print("Karen's Total: " + str(bot6Sum))
		time.sleep(1)
	if userPlaying == True:
		print("Your Hand: " + str(userHand))
		print("Your Total: " + str(userSum))
		time.sleep(1)
#-----------------------------------------------------------------------------

#---------------------------- User Bid ---------------------------------------
def userBet():
	global userMoney
	global userBid
	userBid=0
	print("Your Money: " + str(userMoney))
	while userBid < 25 or userBid > userMoney:
		userBid = (int(input("Your bet: ")))
		if userBid < 25:
			print("Bet must be greater than 25")
		if userBid > userMoney:
			print("You don't have enough money")
	print("You bet: " + str(userBid))
#-----------------------------------------------------------------------------
#---------------------------- User Initial Deal ------------------------------
def userDeal():
	global userHand
	global userSum
	global DeckNamesMaster
	global DeckValuesMaster
	global userAces
	x = random.randint(len(DeckNamesMaster))
	userHand.append(DeckNamesMaster[x])
	userSum = userSum + DeckValuesMaster[x]
	if DeckValuesMaster[x] == 11:
		userAces += 1
	DeckNamesMaster.pop(x)
	DeckValuesMaster.pop(x)
#-------------------------------------------------------------------------------
#---------------------------- Dealer Initial Deal ------------------------------
def dealerDeal():
	global dealerHand
	global dealerSum
	global DeckNamesMaster
	global DeckValuesMaster
	global dealerFaceUpCard
	global dealerAces
	x = random.randint(len(DeckNamesMaster))
	dealerHand.append(DeckNamesMaster[x])
	dealerSum = dealerSum + DeckValuesMaster[x]
	if DeckValuesMaster[x] == 11:
		dealerAces += 1
	if dealerSum != 0:
		dealerFaceUpCard = DeckValuesMaster[x]
	DeckNamesMaster.pop(x)
	DeckValuesMaster.pop(x)
#-------------------------------------------------------------------------------
#---------------------------- Bot Initial Deal ---------------------------------
def botsDeal():

	global botHand
	global botSum
	global botPlaying
	global bot2Hand
	global bot2Sum
	global bot2Playing
	global bot3Hand
	global bot3Sum
	global bot3Playing
	global bot4Hand
	global bot4Sum
	global bot4Playing
	global bot5Hand
	global bot5Sum
	global bot5Playing
	global bot6Hand
	global bot6Sum
	global bot6Playing
	global DeckNamesMaster
	global DeckValuesMaster
	global botAces
	global bot2Aces
	global bot3Aces
	global bot4Aces
	global bot5Aces
	global bot6Aces


	if botPlaying == True:
		x = random.randint(len(DeckNamesMaster))
		botHand.append(DeckNamesMaster[x])
		botSum = botSum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			botAces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
	if bot2Playing == True:
		x = random.randint(len(DeckNamesMaster))
		bot2Hand.append(DeckNamesMaster[x])
		bot2Sum = bot2Sum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			bot2Aces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
	if bot3Playing == True:
		x = random.randint(len(DeckNamesMaster))
		bot3Hand.append(DeckNamesMaster[x])
		bot3Sum = bot3Sum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			bot3Aces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
	if bot4Playing == True:
		x = random.randint(len(DeckNamesMaster))
		bot4Hand.append(DeckNamesMaster[x])
		bot4Sum = bot4Sum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			bot4Aces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
	if bot5Playing == True:
		x = random.randint(len(DeckNamesMaster))
		bot5Hand.append(DeckNamesMaster[x])
		bot5Sum = bot5Sum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			bot5Aces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
	if bot6Playing == True:
		x = random.randint(len(DeckNamesMaster))
		bot6Hand.append(DeckNamesMaster[x])
		bot6Sum = bot6Sum + DeckValuesMaster[x]
		if DeckValuesMaster[x] == 11:
			bot6Aces += 1
		DeckNamesMaster.pop(x)
		DeckValuesMaster.pop(x)
#-------------------------------------------------------------------------------
#------------------------------ Bot Bid ----------------------------------------
def botsBid():
	global botKicked
	global bot2Kicked
	global bot3Kicked
	global bot4Kicked
	global bot5Kicked
	global bot6Kicked
	if botKicked == False:
		x = random.randint(100)
		global botMoney
		global botBid
		global botTurnsSat
		global botPlaying
		if x%2 == 0 or x < 50:
			botPlaying = True
			botBid = random.randint(25, botMoney)
			botTurnsSat = 0
			print("Roman bet: " + str(botBid))
			time.sleep(1)
		else:
			print("Roman Passed")
			time.sleep(1)
			botPlaying = False
			botTurnsSat +=1

	if bot2Kicked == False:
		x = random.randint(100)
		global bot2Money
		global bot2Bid
		global bot2TurnsSat
		global bot2Playing
		if x%2 == 0 or x > 50:
			bot2Playing = True
			bot2Bid = random.randint(25, bot2Money)
			bot2TurnsSat = 0
			print("Tina bet: " + str(bot2Bid))
			time.sleep(1)
		else:
			print("Tina Passed")
			time.sleep(1)
			bot2Playing = False
			bot2TurnsSat +=1

	if bot3Kicked == False:
		x = random.randint(100)
		global bot3Money
		global bot3Bid
		global bot3TurnsSat
		global bot3Playing
		if x%2 == 0 or x < 30:
			bot3Playing = True
			bot3Bid = random.randint(25, bot3Money)
			bot3TurnsSat = 0
			print("Keith bet: " + str(bot3Bid))
			time.sleep(1)
		else:
			print("Keith Passed")
			time.sleep(1)
			bot3Playing = False
			bot3TurnsSat +=1

	if bot4Kicked == False:
		x = random.randint(100)
		global bot4Money
		global bot4Bid
		global bot4TurnsSat
		global bot4Playing
		if x%2 == 0 or x > 70:
			bot4Playing = True
			bot4Bid = random.randint(25, bot4Money)
			bot4TurnsSat = 0
			print("Ryan bet: " + str(bot4Bid))
			time.sleep(1)
		else:
			print("Ryan Passed")
			time.sleep(1)
			bot4Playing = False
			bot4TurnsSat +=1

	if bot5Kicked == False:
		x = random.randint(100)
		global bot5Money
		global bot5Bid
		global bot5TurnsSat
		global bot5Playing
		if x % 2 == 0 or x < 20:
			bot5Playing = True
			bot5Bid = random.randint(25, bot5Money)
			bot5TurnsSat = 0
			print("John bet: " + str(bot5Bid))
			time.sleep(1)
		else:
			print("John Passed")
			time.sleep(1)
			bot5Playing = False
			bot5TurnsSat +=1

	if bot6Kicked == False:
		x = random.randint(100)
		global bot6Money
		global bot6Bid
		global bot6TurnsSat
		global bot6Playing
		if x % 2 == 0 or x > 80:
			bot6Playing = True
			bot6Bid = random.randint(25, bot6Money)
			bot6TurnsSat = 0
			print("Karen bet: " + str(bot6Bid))
			time.sleep(1)
		else:
			print("Karen Passed")
			time.sleep(1)
			bot6Playing = False
			bot6TurnsSat +=1
#-------------------------------------------------------------------------------



#------------------------- Deck Build ------------------------------------------
DeckNames = ["2H", "2D", "2S", "2C", "3H", "3D", "3S", "3C", "4H", "4D", "4S", "4C", "5H", "5D", "5S", "5C", "6H", "6D", "6S", "6C", "7H", "7D", "7S", "7C", "8H", "8D", "8S", "8C", "9H", "9D", "9S", "9C", "10H", "10D", "10S", "10C", "JH", "JD", "JS", "JC", "QH", "QD", "QS", "QC", "KH", "KD", "KS", "KC", "AH", "AD", "AS", "AC"]
DeckValues = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
DeckNamesMaster = []
DeckNamesMasterCopy = []
DeckValuesMaster = []
DeckValuesMasterCopy = []
DeckBuilder = 1
while DeckBuilder < 9:
	DeckNamesMaster = DeckNamesMaster + DeckNames
	DeckValuesMaster = DeckValuesMaster + DeckValues
	DeckBuilder += 1
DeckValuesMasterCopy = DeckValuesMaster
DeckNamesMasterCopy = DeckNamesMaster
#-------------------------------------------------------------------------------
#----------------------- User and Bot Variables --------------------------------
dealerHand = []
dealerFaceUpCard = 0
dealerSum = 0
dealerBust = False
dealerBlackJack = False
dealerAces = 0

userHand = []
userSum = 0
userMoney = 2500
userBid = 0
userTurnsSat = 0
userPlaying = True
userBust = False
userBlackJack = False
userKicked = False
userAces = 0

botName = "Roman"
botHand = []
botSum = 0
botMoney = random.randint(500, 5000)
botBid = 0
botTurnsSat = 0
botPlaying = True
botKicked = False
botBust = False
botBlackJack = False
botAces = 0

bot2Name = "Tina"
bot2Hand = []
bot2Sum = 0
bot2Money = random.randint(500, 5000)
bot2Bid = 0
bot2TurnsSat = 0
bot2Playing = True
bot2Kicked = False
bot2Bust = False
bot2BlackJack = False
bot2Aces = 0

bot3Name = "Keith"
bot3Hand = []
bot3Sum = 0
bot3Money = random.randint(500, 5000)
bot3Bid = 0
bot3TurnsSat = 0
bot3Playing = True
bot3Kicked = False
bot3Bust = False
bot3BlackJack = False
bot3Aces = 0

bot4Name = "Ryan"
bot4Hand = []
bot4Sum = 0
bot4Money = random.randint(500, 5000)
bot4Bid = 0
bot4TurnsSat = 0
bot4Playing = True
bot4Kicked = False
bot4Bust = False
bot4BlackJack = False
bot4Aces = 0

bot5Name = "John"
bot5Hand = []
bot5Sum = 0
bot5Money = random.randint(500, 5000)
bot5Bid = 0
bot5TurnsSat = 0
bot5Playing = True
bot5Kicked = False
bot5Bust = False
bot5BlackJack = False
bot5Aces = 0

bot6Name = "Karen"
bot6Hand = []
bot6Sum = 0
bot6Money = random.randint(500, 5000)
bot6Bid = 0
bot6TurnsSat = 0
bot6Playing = True
bot6Kicked = False
bot6Bust = False
bot6BlackJack = False
bot6Aces = 0
#-------------------------------------------------------------------------------
#---------------------------- Game Loop ----------------------------------------
gameChoice = 0
userChoice = 0

print("Black Jack")
while gameChoice < 1 or gameChoice > 2:
	print("1. Play Game")
	print("2. Quit Game")
	gameChoice = (int(input("Your Choice: ")))
	if gameChoice != 1 and gameChoice !=2:
		print("Invalid Choice. Try again")

#test=0
#while test < 1:
if gameChoice == 1:
#	while userMoney > 49:
	while gameChoice != 2 and userKicked == False:
		while userChoice > 2 or userChoice < 1:
			print("Make a choice")
			print("1.) Play this hand")
			print("2.) Pass this hand")
			userChoice = (int(input("Your Choice: ")))
			if userChoice > 2 or userChoice < 1:
				print("Invalid Choice. Try Again")
		if userChoice == 1:
			userChoice = 0
			userPlaying = True
			userTurnsSat = 0
			userBet()
			botsBid()
			userDeal()
			botsDeal()
			dealerDeal()
			userDeal()
			botsDeal()
			dealerDeal()
			doubleAceCount()
			showHands()
			dealerFaceDown()
			playGame()
			dealerPlay()
			payout()
			reset()
			Shuffle()
		elif userChoice == 2:
			userChoice = 0
			userPlaying = False
			userTurnsSat += 1
			botsBid()
			botsDeal()
			dealerDeal()
			botsDeal()
			dealerDeal()
			doubleAceCount()
			dealerFaceDown()
			playGame()
			dealerPlay()
			payout()
			reset()
			Shuffle()
		gameChoice = 0
		if userKicked == False:
			while gameChoice > 2 or gameChoice < 1:
				print("Make a choice")
				print("1.) Continue Playing")
				print("2.) Quit Game")
				gameChoice = (int(input("Your Choice: ")))
				if gameChoice > 2 or gameChoice < 1:
					print("Invalid Choice. Try Again")
			if gameChoice == 2:
				print("Application Closed")
else:
	print("Application Closed")
