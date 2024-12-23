'''
Card Game - Battle
52 card deck 
Shuffle Deck 
Split deck in 2 - half to player 1, half to player 2
Each player grabs a card, lay it on the table 
Jack < King 
Player with higher card game wins
Player who wins takes the 2 cards
Player who loses the overall game has no remaining cards
If card ranking is same 
Jack = Jack   - "Battle" is declared
In a  Battle, take an additional set of cards
Play with higher card has won the "Battle"
Player that wins the Battle takes all the cards (4 in this card - 2 initial and 2 recently drawn)
Game continues untill a player has all the cards
'''

#Functions
#Deck of 13 cards
cardDeck1 = ['King'* 4, 'Queen'* 4, 'Jack'* 4, 
            '10'* 4, '9'* 4, '8'* 4, '7'* 4,
            '6'* 4, '5'* 4, '4'* 4, '3'* 4, '2'* 4, '1'* 4]
#print(len(cardDeck)) # Question: why is this 13 and not 52?
#*********************************************************************************************************************************
#Test variables
testDeck = ['King', 'Queen', 'Jack', 
            '10', '9', '8', '7',
            '6', '5', '4', '3', '2', '1',
            'King', 'Queen', 'Jack', 
            '10', '9', '8', '7',
            '6', '5', '4', '3', '2', '1',
            'King', 'Queen', 'Jack', 
            '10', '9', '8', '7',
            '6', '5', '4', '3', '2', '1',
            'King', 'Queen', 'Jack', 
            '10', '9', '8', '7',
            '6', '5', '4', '3', '2', '1']

test_player1_splitDeck = ['King', 'Queen', 'Jack', 
                            '10', '9', '8', '7',
                            '6', '5', '4', '3', '2', '1',
                            'King', 'Queen', 'Jack', 
                            '10', '9', '8', '7',
                            '6', '5', '4', '3', '2', '1']
test_player2_splitDeck = ['10', '9', '8', '7',
                            'King', 'Queen', 'Jack', 
                            '6', '5', '4', '3', '2', '1',
                            'King', 'Queen', 'Jack', 
                            '10', '9', '8', '7',
                            '6', '5', '4', '3', '2', '1']

#*********************************************************************************************************************************
#Function to create 52 cards
def cardDeck():
    completeDeck = []
    incompleteDeck = ['King', 'Queen', 'Jack', 
                      '10', '9', '8', '7',
                      '6', '5', '4', '3', '2', '1']
    for i in range(4):
        for suite in incompleteDeck:
            completeDeck.append(suite)
   # print(f'Length:{len(completeDeck)}') #52
    return completeDeck
#print(cardDeck())

#*********************************************************************************************************************************
#Function to define Card Ranking
def cardRanking(card):
    cardDeckRanking = {'King':1000, 'Queen':900, 'Jack':800, 
                       '10':700, '9':600, '8':500,'7':400, 
                       '6':300, '5':200, '4':100, '3':90, '2':80, '1':70}
    
    return cardDeckRanking[card]
#print(cardRanking('2')) #returns 80

#*********************************************************************************************************************************
#Shuffle Deck
import random
def shuffleDeck(completeDeck):
    random.shuffle(completeDeck)  
    return completeDeck   #returns shuffled deck
#print(shuffleDeck(testDeck))

#*********************************************************************************************************************************
#Function to split deck into 2 for players 1 and 2
def splitDeck(shuffledDeck):
    player1_splitDeck = []
    player2_splitDeck = []
    i = 0

    for card in shuffledDeck:
        if i < 26:
             player1_splitDeck.append(card)
#             i += 1
        if i > 25:
            player2_splitDeck.append(card)
        i += 1
    
    return player1_splitDeck,player2_splitDeck

    # for j in shuffledDeck:
    #     player2_splitDeck.append(j)
    # return player2_splitDeck
#print(splitDeck(testDeck))
#*********************************************************************************************************************************
#Function for player to grab a card from the deck
def grabCard(player,player1_splitDeck,player2_splitDeck):
    if player == 'player1':
        position_player1 = 'test'
        selectedPosition_player1 = []
        availablePosition_player1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

        while position_player1 not in availablePosition_player1: #ask player for input if position is not in the list of selected positions
            print(f'Player 1 Available positions: {availablePosition_player1}')
            position_player1 = int(input("Select a position: "))
        selectedPosition_player1.append(position_player1)
        availablePosition_player1.pop(position_player1) #remove selected position from the list of available position 
        playedCard_player1 = player1_splitDeck[position_player1]
        print(f'Updated Available position: {availablePosition_player1}')
        return playedCard_player1
        
    elif player == 'player2':
        position_player2 = 'test'
        selectedPosition_player2 = []
        availablePosition_player2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

        while position_player2 not in availablePosition_player2: #ask player for input if position is not in the list of selected positions
            print(f'Player 2 Available positions: {availablePosition_player2}')
            position_player2 = int(input("Select a position: "))
        selectedPosition_player2.append(position_player2)
        availablePosition_player2.pop(position_player2) #remove selected position from the list of available position 
        playedCard_player2 = player2_splitDeck[position_player2]
        print(f'Updated Available position: {availablePosition_player2}')
        return playedCard_player2   
#print(grabCard('player2',testDeck,testDeck))
#*********************************************************************************************************************************
#Function to compare card rsnking 
def compareCard(playedCard_player1, playedCard_player2):
    cardValue_player1 = cardRanking(playedCard_player1)
    cardValue_player2 = cardRanking(playedCard_player2)
    if cardValue_player1 == cardValue_player2:
        return 'battle'
    elif cardValue_player1 > cardValue_player2:
        return 'play1'
    else:
        return 'play2'
#print(compareCard('King','King'))
battlecards = []
#*********************************************************************************************************************************
#Function to take 4 cards when  a 'battle' is declared
def battle(player1_splitDeck,player2_splitDeck,battlecards):
    #battlecards = []
    battleCard_player1 = grabCard('player1',player1_splitDeck,player2_splitDeck)
    battleCard_player2 = grabCard('player2',player1_splitDeck,player2_splitDeck)
    print(f'Player 1 Battle Card: {battleCard_player1}')
    print(f'Player 2 Battle Card: {battleCard_player2}')
 #   battleWinner = compareCard(battleCard_player1, battleCard_player2)
    battlecards.append(battleCard_player1)
    battlecards.append(battleCard_player2)
    battleWinner = compareCard(battleCard_player1, battleCard_player2)
    print(f'Battlecards: {battlecards}')
    return battlecards,battleWinner
#*********************************************************************************************************************************
#Function to determine the winner of the current round being played
def roundWinner(play,playedcard_player1,playedcard_player2,player1_splitDeck,player2_splitDeck,battlecards):
    wonDeck_player1 = []
    wonDeck_player2 = []
    inBattle = True

    if play == 'play1': #if player 1 won, player 1 takes both players cards
        wonDeck_player1.append(playedcard_player1)
        wonDeck_player1.append(playedcard_player2)
        print(f'Player 1 won deck: {wonDeck_player1}')
    if play == 'play2': #if player 2 won, player 2 takes both players cards
        wonDeck_player2.append(playedcard_player1)
        wonDeck_player2.append(playedcard_player2)
        print(f'Player 2 won deck: {wonDeck_player2}')
    if play == 'battle': #ask players to each grab a card
        # grabCard('player1',player1_splitDeck,player2_splitDeck)
        # grabCard('player2',player1_splitDeck,player2_splitDeck)
        while inBattle:
            battlecards,battleWinner = battle(player1_splitDeck,player2_splitDeck,battlecards)
          #  battleWinner = compareCard(battleCard_player1, battleCard_player2)
            if battleWinner == 'play1':
                wonDeck_player1.append(playedcard_player1)
                wonDeck_player1.append(playedcard_player2)
                for battlecard in battlecards:
                    wonDeck_player1.append(battlecard)
                print('Player 1 won the battle')
                inBattle = False
            if battleWinner == 'play2':
                wonDeck_player2.append(playedcard_player1)
                wonDeck_player2.append(playedcard_player2)
                for battlecard in battlecards:
                    wonDeck_player2.append(battlecard)
                print('Player 2 won the battle')
                inBattle = False
            if battleWinner == 'battle':
                inBattle = True
  
    return wonDeck_player1, wonDeck_player2 #remember this returns a tuple

#print(roundWinner('play1','King','King',test_player1_splitDeck,test_player2_splitDeck))
print(roundWinner('battle','King','King',test_player1_splitDeck,test_player2_splitDeck,battlecards))
#if there are multiple battle all the battle cards are not stored
# 0 4 1 5
#*********************************************************************************************************************************
#Function to determine the overall winner
def overallWinner(wonDeck_player1, wonDeck_player2):
    if len(wonDeck_player1) == 52:
        print("Player 1 wins")
        return True
    elif len(wonDeck_player2) == 52:
        print("Player 2 wins")
        return True
    else:
        pass #do nothing

#print(overallWinner(testDeck,test_player2_splitDeck))
#*********************************************************************************************************************************   
#Game Logic
# completeDeck = cardDeck()   #create a deck of 52 cards
# print(f'52 Card Deck: {completeDeck}')
# shuffledDeck = shuffleDeck(completeDeck)   #Shuffle the deck of 52 cards, returns shuffled deck
# print(f'Shuffled Deck: {shuffledDeck}')
# player1_splitDeck,player2_splitDeck = splitDeck(shuffledDeck)
# print(f'Player 1 Split Deck: {player1_splitDeck}')
# print(f'Player 2 Split Deck: {player2_splitDeck}')
# print(f'Player 1 Split Deck Length: {len(player1_splitDeck)}')
# print(f'Player 2 Split Deck Length: {len(player2_splitDeck)}')

#*********************************************************************************************************************************
'''
Notes
#########################################################
def cardRanking(cardDeck,card):
    x = 0
    value = 1000
    for suite in cardDeck:
         ranking = {suite:value}
         value -= 50
         print(f'suite: {suite} Value: {ranking[suite]}')
    
    return ranking[card]

print(cardRanking(cardDeck, 'King'))

#########################################################
#prices_lookup ={'apple':3,'oranges':1.00,'milk':5.80}
#print(prices_lookup['apple'])
'''