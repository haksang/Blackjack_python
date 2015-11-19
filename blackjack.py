import random

deck = []
suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['None', 'Ace', '2', '3', '4', '5', '6', \
              '7', '8', '9', '10', 'Jack', 'Queeen', 'King']
value = [0, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def create_deck():
    for i in range(len(suit_names)):
        for j in range(len(face_names)-1):
            card = [suit_names[i], face_names[j+1], value[j+1]]
            deck.append(card)
    random.shuffle(deck)
    return deck

    """
    Create a list("deck") of all 52 cards, shuffle them, and return the list
    A card is represented by a tuple with three elements: the face, the suit, and the value
    For instance: ('8', 'Hearts', 8), ('Ace', 'Diamonds', 11)
    """
    
def hand_value(hand):
    sum = 0
    for value in hand:
        sum += value[-1]
    return sum
    """
    Compute the value of the cards in the list "hand"
    """    
    

def card_string(card):
    return card[1] + " of " + card[0]

    """
    Return a nice string to represent a card 
    (such as "a King of Spades" or "an Ace of Diamonds")
    """    

def ask_yesno(prompt):
    print prompt
    answer = raw_input()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print "I beg your pardon!"
        ask_yesno(prompt)
    """
    Display the text prompt and let's the user enter a string.
    If the user enters "y", the function returns "True", 
    and if the user enters "n", the function returns "False"
    If the user enters anything else, the function prints "I beg your pardon!",
    and asks again, repeating this until the user has entered a correct string.
    """    
    

### Now the game start!
while True:    
    # prompt for starting a new game and create a deck
    print "Welcome to Black Jack!\n"
    deck = create_deck()
    # create two hands of dealer and player
    dealer = []
    player = []

    # initial two dealings
    card = deck.pop()
    print "You are dealt " + card_string(card)
    player.append(card)
    card = deck.pop()
    print "Dealer is dealt a hidden card"
    dealer.append(card)
    card = deck.pop()
    print "You are dealt " + card_string(card)
    player.append(card)
    card = deck.pop()
    print "Dealer is dealt " + card_string(card)
    dealer.append(card)
    print "Your total is", hand_value(player)

    # player's turn to draw cards
    while hand_value(player) < 21 \
          and ask_yesno("Would you like another card? (y/n) "):
        # draw a card for the player
        card = deck.pop()
        print "You are dealt " + card_string(card)
        player.append(card)
        print "Your total is", hand_value(player)
        
    # if the player's score is over 21, the player loses immediately.     
    if hand_value(player) > 21:
        print "You went over 21! You lost."
    else:
        # draw cards for the dealer while the dealer's score is less than 17
        print "\nThe dealer's hidden card was " + card_string(dealer[0])
        while hand_value(dealer) < 17:
            card = deck.pop()
            print "Dealer is dealt " + card_string(card)
            dealer.append(card)
        print "The dealer's total is", hand_value(dealer)
        
        # summary        
        player_total = hand_value(player)
        dealer_total = hand_value(dealer)
        print "\nYour total is", player_total
        print "The dealer's total is", dealer_total
        
        if dealer_total > 21:
            print "The dealer went over 21! You win!"
        else:
            if player_total > dealer_total:
                print "You win!"
            elif player_total < dealer_total:
                print "You lost!"
            else:
                print "You have a tie!"
            
    if not ask_yesno("\nPlay another round? (y/n) "):
        break
