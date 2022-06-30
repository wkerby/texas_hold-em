#create a simulation of a no-limit texas hold'em game
import random
import collections

#create a list that contains all player 'hole cards' or personal hands
player_hands = {'p1':[],'p2':[],'p3':[],'p4':[],'p5':[],'p6':[],
'p7':[],'p8':[],'p9':[]}

#establish a list for player roles for each round of the texas hold'em game
player_roles = {'p1':'Dealer','p2':'Small Blind','p3':'Big Blind','p4':'Under the Gun',
'p5':'Under the Gun + 1','p6': 'Under the Gun + 2','p7':'Middle Position','p8':'Hi Jack','p9':'Cutoff'}

#store all player chip budgets in separate variables
chip_bank = {'Black':[10,150],'Red':[20,100],'Blue':[30,50],'Green':[40,25]}
player_chips = {'p1':{},'p2':{},'p3':{},'p4':{},'p5':{},'p6':{},
'p7':{},'p8':{},'p9':{}}

#initiate player budget before beginning of game
#start by getting dot product of chip type counts and chip type values
for chip_color in list(chip_bank.keys()):
	player_bank += chip_bank[chip_color][0]*chip_bank[chip_color][1]

for player in list(player_chips.keys()):
	player_chips[player] = chip_bank
	player_chips[player]['Budget'] = player_bank

#create a list that represents every possible budget value a player could have during the game
#this will be used when deciding the bet amount for a player
#this is simply a list in increments of 25 from (i.e. 1 green chip) to 5400 (i.e. winner of all players' chips)
possible_amounts_list = list(range(25,(len(list(player_hands.keys()))*player_bank)+1,25))

#create a dict of dicts - key representing the possible amount in question, and value representing
#a dict of combination of chip types and numbers that sum to the possible amount
chip_combinations = {}
for possible_amount in possible_amounts_list:
	chip_combinations[possible_amount] = []

#create a player profile that assigns a randommized personality to each player in the game
player_profiles = ["conservative", "moderate", "risk taker"]
player_profiles = player_hands
for player in list(player_hands.keys()):
	player_profiles[player] = choice(player_profiles)

#create a variable for round number
round_num = 0
while len(player_hands) >= 2:
	#rotate player roles one spot in a clock-wise fashion after the first round
	role_rotate = list(player_roles.values())
	role_rotate = collections.deque(role_rotate)
	role_rotate = role_rotate.rotate(round_num)
	for player in list(player_roles.keys()):
		player_roles[player] = role_rotate[(list(player_roles.keys())).index(player)]

	#wipe the player from the game if he doesn't have any money in his 'bank'
	if player_bank < 0:
		del player_roles[player]
		del player_hands[player]
		del player_chips[player]
		print('Player ' + player[1] + ' is eliminated!')

	#create the card deck
	#create dict of all cards with eack key representing each suit
	cards = ['ace','king','queen','jack','10','9','8','7','6','5','4','3','2']
	card_suits = ['spades','hearts','diamonds','clubs']
	card_deck = {}
	for card_suit in card_suits:
		card_deck[card_suit] = cards

	#deal the 'hole cards' to all players and store hands in a list of dictionaries
	#establish a list that represents the 'hole cards' through which to loop
	hand = ['card1','card2']

	for player_hand in list(player_hands.keys()):
		hand_num = 0
		while hand_num < 2:
			suit = choice(card_suits)
			card = choice(cards)
			player_hands[player_hand].append({suit:card})
			#ensure that card is no longer picked from deck
			card_deck[suit].remove(card)
			hand_num += 1
	#pass a variable that represents the preflop (0), flop (1), turn (2), and river (3) rounds
	sub_round_num = 0

	#create a dictionary for betting pot for each round
	bet_pot = {'Black':[0,150],'Red':[0,100],'Blue':[0,50],'Green':[0,25]}

	#begin with obligatory bets for big blind and small blind players
	#determine the big blind and small blind players and communicate to player 1
	for player,player_role in list(player_roles.items()):
		if player_role == "Big Blind":
			#check to see if the player can afford to play the role of big blind
			if player_chips[player]['Budget'] >= 50:
				if player_chips[player]['Blue'][0] >= 1:
					player_chips[player]['Blue'][0] -= 1 #remove one blue chip from player bank
					bet_pot['Blue'] += 1 #put this one blue chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Big Blind! He puts $50 worth of chips into the pot this round preflop!')
				elif player_chips[player]['Green'][0] >= 2:
					player_chips[player]['Green'][0] -= 2 #remove two green chips from player bank
					bet_pot['Green'] += 2 #put these two green chips into the betting pot for the round
					print('Player ' + player[1] + ' is the Big Blind! He puts $50 worth of chips into the pot this round preflop!')
				elif player_chips[player]['Red'][0] >= 1:
					player_chips[player]['Red'][0] -= 1 #remove one red chip from player bank
					bet_pot['Red'] += 1 #put this one red chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Big Blind! He has to put a little more than $50 worth of chips into the pot this round preflop due to his chip count!')
				elif player_chips[player]['Black'][0] >= 1:
					player_chips[player]['Black'][0] -= 1 #remove one black chip from player bank
					bet_pot['Black'] += 1 #put this one black chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Big Blind! He has to put a little more than $50 worth of chips into the pot this round preflop due to his chip count!')
				#re-display the player's current budget after the preflop Big Blind dues are paid
				for chip_color in list(chip_bank.keys()):
						player_bank += player_chips[player][chip_color][0]*player_chips[player][chip_color][1]
					player_chips['Budget'] = player_bank
			else:
				print('Player ' + player[1] + ' cannot aford to be the Big Blind is therefore eliminated!')
				del player_roles[player]
				del player_hands[player]
				del player_chips[player]
		elif player_role == "Small Blind":
			#check to see if the player can afford to play the role of small blind
			if player_chips[player]['Budget'] >= 25:
				if player_chips[player]['Green'][0] >= 1:
					player_chips[player]['Green'][0] -= 1 #remove one green chip from player bank
					bet_pot['Green'] += 1 #put this one green chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Small Blind! He puts $25 worth of chips into the pot this round preflop!')
				elif player_chips[player]['Blue'][0] >= 1:
					player_chips[player]['Blue'][0] -= 1 #remove one blue chip from player bank
					bet_pot['Blue'] += 1 #put this one blue chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Small Blind! He has to put a little more than $25 worth of chips into the pot this round preflop due to his chip count!')
				elif player_chips[player]['Red'][0] >= 1:
					player_chips[player]['Red'][0] -= 1 #remove one red chip from player bank
					bet_pot['Red'] += 1 #put this one red chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Small Blind! He has to put a little more than $25 worth of chips into the pot this round preflop due to his chip count!')
				elif player_chips[player]['Black'][0] >= 1:
					player_chips[player]['Black'][0] -= 1 #remove one black chip from player bank
					bet_pot['Black'] += 1 #put this one black chip into the betting pot for the round
					print('Player ' + player[1] + ' is the Small Blind! He has to put a little more than $25 worth of chips into the pot this round preflop due to his chip count!')
				for chip_color in list(chip_bank.keys()):
						player_bank += player_chips[player][chip_color][0]*player_chips[player][chip_color][1]
					player_chips['Budget'] = player_bank
			else:
				print('Player ' + player[1] + ' cannot aford to be the Small Blind is therefore eliminated!')
				del player_roles[player]
				del player_hands[player]
				del player_chips[player]

	#now simulate the bets for the round
	#identify the under the gun player, as he is first to make a move
	under_gun_index = list(player_roles.keys()).index(player for player, player_role in list(player_roles.items()) if player_role == "Under the Gun")
	under_gun_append = list(player_roles.keys())[:under_gun_index-1]
	under_gun_start = list(player_roles.keys())[under_gun_index:]
	bet_rotation = under_gun_start.append(under_gun_append)
	for player in bet_rotation:
		#consider 'hole card' hands for each player that are more conducive to a higher preflop bet
		#pairs - check for a pair in the player hand
		#create a list that represents the odds that a computer-simulated player will bet, call, raise, check, or fold, respectively
		#now establish rules that make sense for bet, call, raise, check, or fold based on preceding player moves
		#create a dictionary that records each player's preflop action
		player_bets = player_hands
		player_bet_amounts = player_hands
		bet_amount = ["small","medium","large","all in"]
		bet_amount_prob = [0 for option in bet_options]
		for player in list(player_hands.keys()):
			#assign higher probabilities of a risky bet to the "risk taker" player profile
			if player_profiles[player] == "conservative":
				player_bet_amounts[player] = choose(bet_amount,[0.60,0.30,0.09,0.01])
			elif player_profiles[player] == "moderate":
				player_bet_amounts[player] = choose(bet_amount,[0.20,0.45,0.30,0.05])
			elif player_profiles[player] == "risk taker":
				player_bet_amounts[player] = choose(bet_amount,[0.10,0.40,0.40,0.10])
		bet_options = ['bet','call','raise','check','fold']
		bet_options_prob = [0 for option in bet_options]
		for player in bet_rotation:
			if bet_rotation.index(player) == 0: #i.e. if the player is in the "Under the Gun" spot or first to take action on bets
				if list(player_hands[player][0].values())[0] == list(player_hands[player][1].values())[0]:
					#this means that the player in question was dealt a pair
					#now check specific card value
					if list(player_hands[player][0].values())[0] in cards[:4]: #i.e. is the pair a face card or ace pair
						if player_profiles[player] == "conservative":
							bet_options_prob[bet_options.index('bet')] = 0.60
							bet_options_prob[bet_options.index('check')] = 0.30
							bet_options_prob[bet_options.index('fold')] = 0.10
						elif player_profiles[player] == "moderate":
							bet_options_prob[bet_options.index('bet')] = 0.80
							bet_options_prob[bet_options.index('check')] = 0.15
							bet_options_prob[bet_options.index('fold')] = 0.05
						elif player_profiles[player] == "risk taker":
							bet_options_prob[bet_options.index('bet')] = 1
					else:
						if player_profiles[player] == "conservative":
							bet_options_prob[bet_options.index('bet')] = 0.50
							bet_options_prob[bet_options.index('check')] = 0.30
							bet_options_prob[bet_options.index('fold')] = 0.20
						elif player_profiles[player] == "moderate":
							bet_options_prob[bet_options.index('bet')] = 0.70
							bet_options_prob[bet_options.index('check')] = 0.25
							bet_options_prob[bet_options.index('fold')] = 0.05
						elif player_profiles[player] == "risk taker":
							bet_options_prob[bet_options.index('bet')] = 0.90
							bet_options_prob[bet_options.index('check')] = 0.08
							bet_options_prob[bet_options.index('fold')] = 0.02
				else: #bookmark
					if player_profiles[player] == "conservative":
						bet_options_prob[bet_options.index('call')] = 0.20
						bet_options_prob[bet_options.index('raise')] = 0.60
						bet_options_prob[bet_options.index('fold')] = 0.20
					elif player_profiles[player] == "moderate":
						bet_options_prob[bet_options.index('call')] = 0.40
						bet_options_prob[bet_options.index('raise')] = 0.50
						bet_options_prob[bet_options.index('fold')] = 0.10
					elif player_profiles[player] == "risk taker":
						bet_options_prob[bet_options.index('call')] = 0.70
						bet_options_prob[bet_options.index('raise')] = 0.29
						bet_options_prob[bet_options.index('fold')] = 0.01

				#"Under the Gun" player now makes his decision		
				player_bets[player] = random.choices(bet_options,bet_options_prob,k=1)
			#now assign action probability weights for turns past the under the gun player
			else:
				if player_bets[bet_rotation[bet_rotation.index(player) - 1]] == 'bet' or 'raise':
					#if a bet or raise was placed by the previous player, all players that preceded the bet or raise have to choose whether or not to call or raise
					player_precedents = bet_rotation[:bet_rotation.index(player) - 1]
					for player in player_precedents:
						if player_profiles[player] == "conservative":
							bet_options_prob[bet_options.index('call')] = 0.25
							bet_options_prob[bet_options.index('raise')] = 0.10
							bet_options_prob[bet_options.index('fold')] = 0.65
						elif player_profiles[player] == "moderate":
							bet_options_prob[bet_options.index('call')] = 0.50
							bet_options_prob[bet_options.index('raise')] = 0.20
							bet_options_prob[bet_options.index('fold')] = 0.30
						elif player_profiles[player] == "risk taker":
							bet_options_prob[bet_options.index('call')] = 0.45
							bet_options_prob[bet_options.index('raise')] = 0.52
							bet_options_prob[bet_options.index('fold')] = 0.03
					



	#now simulate the flop
	#create community hand as a list of dictionaries 
	community_hand = []
	for card in list(range(1,6)):
		#important that dealer picks these cards from the remaining card deck dictionary and not the cards and suits lists
		suit = choice(list(card_deck.keys()))
		card = choice(card_deck[suit])
		community_hand.append({suit:card})
		card_deck[suit].remove(card)
	#display player 1's budget in a readable fashion preflop
	print('Player 1 chip bank: ' + '\n' + str(player_chips['p1']['Green'][0]) + ' Green for ' + str(player_chips['p1']['Green'][0]*player_chips['p1']['Green'][1]) + '\n'
	+ str(player_chips['p1']['Blue'][0]) + ' Blue for ' + str(player_chips['p1']['Blue'][0]*player_chips['p1']['Blue'][1]) + '\n'
	+ str(player_chips['p1']['Red'][0]) + ' Red for ' + str(player_chips['p1']['Red'][0]*player_chips['p1']['Red'][1]) + '\n'
	+ str(player_chips['p1']['Black'][0]) + ' Black for ' + str(player_chips['p1']['Black'][0]*player_chips['p1']['Black'][1]) + '\n'
	+ 'Total ' + str(player_chips['p1']['Budget']))
	#display player 1's 'hole cards' in a readable fashion preflop
	print('Player 1 hand: ' + '\n' + list(player_hands['p1'].values())[0] ' of ' + list(player_hands['p1'].keys())[0]
		+ '\n' + list(player_hands['p1'].values())[1] ' of ' + list(player_hands['p1'].keys())[1])
	#ask player 1 if he is ready for the flop
	flop_check = input("Are you ready for the flop (yes/no)?")
	#display the flop
	if flop_check.lower() == "yes":
		print("On the table:")
		#display what is on the table in a readable fashion
		for card in list(range(len(community_hand))):
			print()











