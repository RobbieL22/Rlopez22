import itertools #imports the tools used in the programming so that the program understands certain functions used
import random 
suits = ['s', 'c', 'd', 'h'] #possible suits
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'] #possible faces
'''deck = set(itertools.product(faces , suits))''' #creates a 52 element list with every combination of possible suits and faces
deck = ['A Spades','2 Spades','3 Spades','4 Spades','5 Spades','6 Spades','7 Spades','8 Spades','9 Spades','10 Spades','J Spades','Q Spades','K Spades','A Hearts','2 Hearts','3 Hearts','4 Hearts','5 Hearts','6 Hearts','7 Hearts','8 Hearts','9 Hearts','10 Hearts','J Hearts','Q Hearts','K Hearts','A Clubs','2 Clubs','3 Clubs','4 Clubs','5 Clubs','6 Clubs','7 Clubs','8 Clubs','9 Clubs','10 Clubs','J Clubs','Q Clubs','K Clubs','A Diamonds','2 Diamonds','3 Diamonds','4 Diamonds','5 Diamonds','6 Diamonds','7 Diamonds','8 Diamonds','9 Diamonds','10 Diamonds','J Diamonds','Q Diamonds','K Diamonds',]
deck2 = deck #for security, I have created a second deck that will keep track of cards that have not been drawn
drawn_cards = random.sample(deck,5) #creates a 5 element list of randomly selected elements in the 'deck' list
deck2.remove(drawn_cards[0]) #removes the first drawn card from the deck so that it will not be drawn again
deck2.remove(drawn_cards[1]) #removes the second drawn card
deck2.remove(drawn_cards[2]) #removes the third drawn card
deck2.remove(drawn_cards[3]) #removes the fourth drawn card
deck2.remove(drawn_cards[4]) #removes the fifth drawn card
print 'You drew:'
print drawn_cards #Shows the list of cards you drew
choices = ['0','0','0','0','0'] #The default list of cards you would like to swap, all five of your choices
def swap(): #function checks if you would like to swap any cards, swaps the first.
    print "Would you like to swap any cards? (Type y for yes, Type n if you are happy with your cards)" # asks question and tells player what to do.
    swap1 = raw_input() #receives the input of the player
    if swap1 == "y": #if the player input a y for yes
        while 0==0: #will loop continuing to check for a swap
            print "Which card would you like to switch first? (Type a number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch, 1 for far left, 5 for far right)" #tells player how to select a card to swap
            change1 = raw_input() #will take the players input
            if change1 == '1': #checks if the input was a 1
                drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                choices[0] = '1' #keeps track of the first card you chose in the list 'choices'
                deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
            elif change1 == '2': #checks if the input was a 2
                drawn_cards[1] = random.choice(deck2)#replaces the second element in the list of drawn cards with a random card from the deck
                choices[0] = '2' #keeps track of the second card you chose in the list 'choices'
                deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
            elif change1 == '3': #checks if the input was a 3
                drawn_cards[2] = random.choice(deck2)#replaces the third element in the list of drawn cards with a random card from the deck
                choices[0] = '3' #keeps track of the third card you chose in the list 'choices'
                deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
            elif change1 == '4': #checks if the input was a 4
                drawn_cards[3] = random.choice(deck2)#replaces the fourth element in the list of drawn cards with a random card from the deck
                choices[0] = '4' #keeps track of the fourth card you chose in the list 'choices'
                deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
            elif change1 == '5': #checks if the input was a 5
                drawn_cards[4] = random.choice(deck2)#replaces the fifth element in the list of drawn cards with a random card from the deck
                choices[0] = '5' #keeps track of the fifth card you chose in the list 'choices'
                deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
            else: #if the player did not input a 1,2,3,4 or 5
                print "I didn't catch that." #the program says it didn't understand.
                continue #goes back to the while loop, asks to pick a card to swap again
            swap_2() #once the player selects a card to change it will move on to ask for a second swap
            return #stops the while loop so that it will stop checking for a number
    elif swap1 == "n": #If the player's input was a n for no, it will swap anycards and directly go to show the hand
        show_hand()
    else: #If the player entered something other than y or n, it will ask them to re enter that
        print "I didn't catch that."
        swap()
def swap_2():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch another.
    print "Would you like to swap a second card? (Type y for yes, Type n if you like the other 4 cards)"
    swap2 = raw_input()#player's input
    if swap2 == 'y':#if player pressed y
        while 0==0:#loops indefinitely
            print "What other card would you like to swap? (Type a different number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch NOT THE SAME NUMBER)"
            change2 = raw_input()#another player's input
            if change2 == choices[0]:#if the player entered the same number for the first swap, tell them they can't do that. Ask them if they want to swap again
                print "You already changed that card."
                swap_2()
                return
            else:#if it is a new card, check which one
                if change2 == "1":#If they choose to swap 1
                    drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                    choices[1] = '1' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
                elif change2 == "2":#If they choose to swap 2
                    drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
                    choices[1] = '2' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
                elif change2 == "3":#If they choose to swap 3
                    drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
                    choices[1] = '3' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
                elif change2 == "4":#If they choose to swap 4
                    drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
                    choices[1] = '4' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
                elif change2 == "5":#If they choose to swap 5
                    drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
                    choices[1] = '5' #keeps track of the second card you chose in the list 'choices'
                    deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
                else: #if they didn't put in a 1,2,3,4 or 5 it will recheck which card they wanted to swap
                    print "I didn't catch that."
                    continue
                swap_3()  #once a card has been chosen, check if they want to swap a third.
                return
    elif swap2 == 'n': #if they choose not to swap a second time, show them their hand.
        show_hand()
    else: #If they did not enter a y or n, ask them to re enter
        print "I didn't catch that"
        swap_2()
def swap_3():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch another.
    print "Would you like to swap a third card? (Type y for yes, Type n if you like the other 3 cards)"
    swap3 = raw_input()#player's input
    if swap3 == 'y':#if they choose y to swap a card
        while 0==0:#loops indefinitely
            print "What other card would you like to swap? (Type a different number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch NOT THE SAME NUMBER)"
            change3 = raw_input()#another input of the player
            if change3 == choices[0] or change3 == choices[1]: #Checks if the player chose a card that they already swapped the first or second time
                print "You already changed that card."
                swap_3()
                return
            else:#if they picked a new card
                if change3 == "1":#checks if they want to swap card 1
                    drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                    choices[2] = '1' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
                elif change3 == "2":#checks if they want to swap card 2
                    drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
                    choices[2] = '2' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
                elif change3 == "3":#checks if they want to swap card 3
                    drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
                    choices[2] = '3' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
                elif change3 == "4":#checks if they want to swap card 4
                    drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
                    choices[2] = '4' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
                elif change3 == "5":#checks if they want to swap card 5
                    drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
                    choices[2] = '5' #keeps track of the third card you chose in the list 'choices'
                    deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
                else:#if they enter something other than 1,2,3,4 or 5, ask them to try again.
                    print "I didn't catch that."
                    continue
                swap_4()#once they choose a number to swap, check if they swap a fourth card.
                return
    elif swap3 == 'n':#if they don't want to swap a third card, show hand
        show_hand()
    else:#if they didn't enter y or n, ask them to re enter
        print "I didn't catch that"
        swap_3()
def swap_4():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch another.
    print "Would you like to swap a fourth card? (Type y for yes, Type n if you like the other 2 cards)"
    swap4 = raw_input()#player's input
    if swap4 == 'y':#if they choose y to swap a card
        while 0==0:#loops indefinitely
            print "What other card would you like to swap? (Type a different number 1 through 5 inclusive that corresponds to the card you want to the card you want to switch NOT THE SAME NUMBER)"
            change4 = raw_input()#another input of the player
            if change4 == choices[0] or change4 == choices[1] or change4 == choices[2]: #Checks if the player chose a card that they already swapped the first, second, or third time
                print "You already changed that card."
                swap_4()
                return
            else:#if they picked a new card
                if change4 == "1":#checks if they want to swap card 1
                    drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
                    choices[3] = '1' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
                elif change4 == "2":#checks if they want to swap card 2
                    drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
                    choices[3] = '2' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
                elif change4 == "3":#checks if they want to swap card 3
                    drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
                    choices[3] = '3' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
                elif change4 == "4":#checks if they want to swap card 4
                    drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
                    choices[3] = '4' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
                elif change4 == "5":#checks if they want to swap card 5
                    drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
                    choices[3] = '5' #keeps track of the fourth card you chose in the list 'choices'
                    deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
                else:#if they enter something other than 1,2,3,4 or 5, ask them to try again.
                    print "I didn't catch that."
                    continue
                swap_5()#once they choose a number to swap, check if they swap a fifth card.
                return
    elif swap4 == 'n':#if they don't want to swap a fourth card, show hand
        show_hand()
    else:#if they didn't enter y or n, ask them to re enter
        print "I didn't catch that"
        swap_4()
def swap_5():#If the player has not already pressed n to stop swapping cards, they will be asked if they want to switch the last one.
    print "Would you like to swap the last card? (Type y for yes, Type n if you like the last card)"
    swap5 = raw_input()#player's input
    if swap5 == 'y':#if they choose y to swap a card
        if '1' not in choices:#if they swapped every card except for number 1, swap number 1
            drawn_cards[0] = random.choice(deck2) #replaces the first element in the list of drawn cards with a random card from the deck
            choices[4] = '1' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[0]) #removes the newly drawn card from the deck
        elif '2' not in choices:#if they swapped every card except for number 2, swap number 2
            drawn_cards[1] = random.choice(deck2) #replaces the second element in the list of drawn cards with a random card from the deck
            choices[4] = '2' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[1]) #removes the newly drawn card from the deck
        elif '3' not in choices:#if they swapped every card except for number 3, swap number 3
            drawn_cards[2] = random.choice(deck2) #replaces the third element in the list of drawn cards with a random card from the deck
            choices[4] = '3' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[2]) #removes the newly drawn card from the deck
        elif '4' not in choices:#if they swapped every card except for number 4, swap number 4
            drawn_cards[3] = random.choice(deck2) #replaces the fourth element in the list of drawn cards with a random card from the deck
            choices[4] = '4' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[3]) #removes the newly drawn card from the deck
        elif '5' not in choices:#if they swapped every card except for number 5, swap number 5
            drawn_cards[4] = random.choice(deck2) #replaces the fifth element in the list of drawn cards with a random card from the deck
            choices[4] = '5' #keeps track of the fifth card you chose in the list 'choices'
            deck2.remove(drawn_cards[4]) #removes the newly drawn card from the deck
        show_hand()
    elif swap5 == 'n':#if they don't want to swap a fifth card, show hand
        show_hand()
    else:#if they didn't enter y or n, ask them to re enter
        print "I didn't catch that"
        swap_5()
def show_hand():
    print drawn_cards
swap()