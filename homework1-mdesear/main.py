import card, deck, hand
            
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjust()

def hit_or_stand(deck, hand, dealer):
    global playing

    while True:
        answer = input("\nWould you like to (h)it or (s)tand?") 
        if answer[0].lower() == "h":
            hit(deck, hand)
            if hand.value < 21:
                show_hand(hand)
                continue    # Player can continue hitting as long as value doesn't exceed 21
        elif answer[0].lower() == "s":
            print("Player stands. Dealer's turn to play.")
            while dealer.value < 17:
                hit(deck, dealer)
            playing = False
        else:
            print("Invalid input. Please type 'h' to hit or 's' to stand.")
            continue
        break

def show_hand(player):
    print("\nPLAYER'S HAND:\n---------------", *player.cards, sep="\n")
    print("---------------")
    print("Player's hand value = " + str(player.value))

def show_hand_hidden(dealer):
    print("\nDEALER'S HAND:\n---------------")
    print("[CARD HIDDEN]")
    print(dealer.cards[1])  # Only the second card is shown "face up"
    print("---------------")

def show_hand_all(dealer):
    print("\n===============\nSHOWING HAND...\n===============")
    print("\nDEALER'S HAND:\n---------------", *dealer.cards, sep="\n")
    print("---------------")
    print("Dealer's hand value = " + str(dealer.value))

def outcome(player, dealer):
    # All possible game outcomes are below
    if player.value > 21:
        print("Player busts!")

    elif dealer.value > 21:
        print("\nDealer busts!")

    elif player.value == dealer.value:
        print("\nDealer and player's hands have the same value. Push!")

    elif dealer.value == 21:
        print("\nDealer got a blackjack!")

    elif player.value == 21:
        print("\nPlayer got a blackjack!")
            
    elif dealer.value > player.value:
        print("\nDealer's hand is closer to 21. Dealer wins!")

    elif player.value > dealer.value:
        print("\nPlayer's hand is closer to 21. Player wins!")    

print("=====================\nWelcome to Blackjack!\n=====================")

def main():
    while True:
        playing = True
        newDeck = deck.Deck()
        newDeck.shuffle()

        while playing:
            # Player and dealer are dealt two cards
            player_hand = hand.Hand()
            player_hand.add_card(newDeck.deal())
            player_hand.add_card(newDeck.deal())

            dealer_hand = hand.Hand()
            dealer_hand.add_card(newDeck.deal())
            dealer_hand.add_card(newDeck.deal())

            show_hand_hidden(dealer_hand)
            show_hand(player_hand)

            hit_or_stand(newDeck, player_hand, dealer_hand)       

            show_hand(player_hand)
            show_hand_all(dealer_hand)

            outcome(player_hand, dealer_hand)

            while True:
                restart = input("\nWould you like to play again (y/n)?")
                if restart[0].lower() == 'y':
                    playing = True
                    break
                elif restart[0].lower() == 'n':
                    print("Thank you for playing! Quitting application...")
                    exit()
                if not restart == ("y" or "n"):
                    print("Invalid input. Please type 'y' to keep playing and 'n' to quit.")
            continue

if __name__ == "__main__":
    main()