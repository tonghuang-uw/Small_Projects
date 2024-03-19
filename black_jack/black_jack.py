import random

"""
Creating a blackjack game, for now, we use only one deck of cards
"""



# a list of all the suits 
# clubs, heart, diamond, spades


def main():
    print("--------Black Jack--------")
    account = 10000

    while True:
        # initial stage
        cards = Deck()
        bet = PlayerBet(account)
        if bet == 'y':
            account = 10000
            continue
        elif bet == 'n':
            break
        else:
            bet = int(bet)
        dealer = []
        player = []

        # two cards for dealer and two cards for player

        for i in range(2):
            drawn_card_dealer = cards.pop()
            dealer.append(drawn_card_dealer)
            drawn_card_player = cards.pop()
            player.append(drawn_card_player)
        
        print("Dealer: ???")
        DisplayCards(dealer, True)
        print()
        print("Player: {}".format(CheckValue(player)))
        DisplayCards(player)
        
        # If blackjack
        if CheckValue(player) == 21:
            print("Yeah! You got a blackjack!")
            account += 1.5*bet
            continue
        while True:
            action = PlayerAction()
            print(action)
            if action == 'H':
                print(1)
                drawn_card_player = cards.pop()
                player.append(drawn_card_player)
                if CheckValue(player) <= 21:
                    print("Dealer: ???")
                    DisplayCards(dealer, True)
                    print()
                    print("Player: {}".format(CheckValue(player)))
                    DisplayCards(player)
                    
                else:
                    print("Dealer: {}".format(CheckValue(dealer)))
                    DisplayCards(dealer)
                    print()
                    print("Player: {}".format(CheckValue(player)))
                    DisplayCards(player)
                    print("You busted!")
                    account -= bet
                    break
            else:
                print("Dealer: {}".format(CheckValue(dealer)))
                DisplayCards(dealer)
                print()
                print("Player: {}".format(CheckValue(player)))
                DisplayCards(player)

                while CheckValue(dealer) < 17:
                    drawn_card_dealer = cards.pop()
                    dealer.append(drawn_card_dealer)

                    print("Dealer: {}".format(CheckValue(dealer)))
                    DisplayCards(dealer)
                    print()
                    print("Player: {}".format(CheckValue(player)))
                    DisplayCards(player)

                    if CheckValue(dealer) > 21:
                        print("You win!")
                        account += bet
                        break
                    else:
                        continue
                if CheckValue(dealer) == CheckValue(player):
                    print("You tie!")
                elif CheckValue(dealer) > CheckValue(player) and CheckValue(dealer) <= 21:
                    print(CheckValue(dealer))
                    print("You lose!")
                    account -= bet
                elif CheckValue(dealer) <= 21 and CheckValue(player) > CheckValue(dealer):
                    print("You win!")
                    account += bet
                break

    #while ...:
        # Playing one game
        # house has to play until 17 hits or busted
        # player can hit or stand
        
        # initial stage
        


        ## function for initial stage
        ## function to display both cards
        ## function to ask players for their actions
        ## function to check the value of the hands
        

        # following stage

        ### display both dealer and player cards
        ### ask if player for their action
        ### stop if player stand or busted(check the value)
        ### if busted(end the game) if in, dealer start
        ### display

        # if player stop
        ### dealer's turn
        ### until 17 hits or busted
        ## function for dealer 

        # check if busted or they want to stand
        


def Deck():
    # To produce one deck of 52 cards
    Suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
    Ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    Cards = [(suit, rank) for suit in Suits for rank in Ranks]

    random.shuffle(Cards)
    return Cards


def PlayerAction():
    
    while True:
        print("(H)it, (S)tand")
        action = input(">").upper().strip()
        print(action)
        if action in ['H', 'S']:
            return action
        else:
            print("Invalid input. Please enter H or S")
    


def PlayerBet(account):
    
    if account <= 0:
        print("You have loss all the money, do you want to reset?(y/n)")
        while True:
            ifcontinue = input(">").lower()
            if ifcontinue == 'y' or ifcontinue == 'n':
                return ifcontinue
            else:
                print("Please enter y or n")

    while True:
        print("Now, Your account is {}".format(account))
        print("How much do you want to bet? (1-10000, QUIT)")
        bet = input('> ').upper().strip()
        if int(bet) > account:
            print("Please enter a valid amound, your entered amount exceed you maximum account!")
            continue
        if bet == "QUIT":
            break

        if not bet.isdecimal():
            print("Please enter a valid amount. (1-10000, QUIT)")
            continue

        bet = int(bet)
        if bet <= 10000 and bet >= 1:
            return bet
        else:
            print("Please enter a valid amount. (1-10000)")
            continue



def CheckValue(Cards):
    # Check the value of cards
    total = 0
    n_a = 0
    for card in Cards:
        rank = card[1]

        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
            n_a += 1
        else:
            total += int(rank)
        
        if total > 21 and n_a >=1:
            total -= 10
            n_a -=1

    return total


def DisplayCards(Cards, initial_stage = False):
    
    row = [' ', ' ', ' ', ' ', ' ']
    if initial_stage == True:
        suit, rank = Cards[1]
        row[0] += " ___ "
        row[1] += "|#  |"
        row[2] += "|###|"
        row[3] += "|__#|"

        row[0] += " ___ "
        row[1] += "|{} | ".format(rank.ljust(2))
        row[2] += "| {} | ".format(suit)
        row[3] += "|_{}| ".format(rank.rjust(2, "_"))

    else:
        for i in range(len(Cards)):
            # Print the card's front:
            suit, rank = Cards[i]  # The card is a tuple data structure.
            row[0] += ' ___  '
            row[1] += '|{} | '.format(rank.ljust(2))
            row[2] += '| {} | '.format(suit)
            row[3] += '|_{}| '.format(rank.rjust(2, '_'))
    
    for r in row:
        print(r)


if __name__ == "__main__":
    main()
