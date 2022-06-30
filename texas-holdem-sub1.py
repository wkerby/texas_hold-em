import random

#establish a list that contains all player 'hole cards' or personal hands
player_hands = {'p1':[],'p2':[],'p3':[],'p4':[],'p5':[],'p6':[],
'p7':[],'p8':[],'p9':[]}

#store all player chip budgets in separate variables
chip_bank = {'Black':[10,150],'Red':[20,100],'Blue':[30,50],'Green':[40,25]}
player_chips = {'p1':{},'p2':{},'p3':{},'p4':{},'p5':{},'p6':{},
'p7':{},'p8':{},'p9':{}}

#initiate player budget before beginning of game
	#start by getting dot product of chip type counts and chip type values
player_bank = 0
for chip_color in list(chip_bank.keys()):
	player_bank += chip_bank[chip_color][0]*chip_bank[chip_color][1]

for player in list(player_chips.keys()):
	player_chips[player] = chip_bank
	player_chips[player]['Budget'] = player_bank

#create a list that represents every possible budget value a player could have during the game
#this will be used when deciding the bet amount for a player
possible_amounts_list = list(range(25,(len(list(player_hands.keys()))*player_bank)+1,25))

#create a dict of lists represnting every possible number of chip of each type a player could possess 
#and the value of one chip of each type
chip_permutations = {}
for chip_color in list(chip_bank.keys()):
	chip_permutations[chip_color] = [] 

print(chip_permutations)

	# chip_permutations[chip_color].append(list(range(0,(9*chip_bank[chip_color][0])+1)))
	# chip_permutations[chip_color].append(chip_bank[chip_color][1])


# #create a dict of dicts - key representing the possible amount in question, and value representing
# #a dict of combination of chip types and numbers that sum to the possible amount
# chip_amount_combos = {}
# for possible_amount in possible_amounts_list:
# 	chip_amount_combos[possible_amount] = []

# #fill each possible amount key with all chip combo dicts that sum to that amount		
# chip_combo = {}
# count = 0
# while count < 5000:
# 	for chip_color in list(chip_bank.keys()):
# 		chip_number = choice(chip_permutations[chip_color])[0]
# 		add_value = chip_number*chip_permutations[chip_color][1]
# 		chip_combo[chip_color] = chip_number
# 		possible_amount += add_value
# 	if possible_amount in list(chip_amount_combos.keys()):
# 		chip_amount_combos[possible_amount].append(chip_combo)
# 	else:
# 		pass
# 	count += 1

# print(chip_amount_combos)
	




