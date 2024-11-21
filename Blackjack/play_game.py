from DeckOfCards import *

def calculate_score(hand):
    # Calculate the total score of a hand of cards. Adjusts for Aces if the score exceeds 21.
    score = sum(card.val for card in hand)  # Sum up the values of the cards in hand
    num_aces = sum(1 for card in hand if card.face == 'Ace')  # Count the number of Aces
    
    # Adjust the score for Aces if the score exceeds 21
    while score > 21 and num_aces:
        score -= 10  # Reduce the score by 10 for each Ace adjusted
        num_aces -= 1  # Decrease the number of Aces to adjust
    
    return score

def display_hand(hand, name="Player"):
    # Display the hand and score for a player or dealer.
    hand_str = ', '.join(f"{card.face} of {card.suit}" for card in hand)  # Create a string representation of the hand
    print(f"{name}'s hand: {hand_str}")
    print(f"{name}'s score: {calculate_score(hand)}")

def play_game(deck):
    # Main function to play the Blackjack game.
    if deck.play_idx > len(deck.deck) - 10:
        # If there are fewer than 10 cards remaining, reshuffle the deck
        print("Reshuffling deck...")
        deck.shuffle_deck()

    print("\nStarting a new round of Black Jack!")
    
    # Deal two cards to the player and two cards to the dealer
    user_hand = [deck.get_card(), deck.get_card()]
    dealer_hand = [deck.get_card(), deck.get_card()]
    
    # Display the player's initial hand
    display_hand(user_hand, "Player")
    
    while True:
        choice = input("Would you like a hit? (y/n): ").strip().lower()  
        # Ask player if they want a hit
        
        if choice == 'y':
            # Add a new card to the player's hand and display the updated hand and score
            user_hand.append(deck.get_card())
            display_hand(user_hand, "Player")
            
            if calculate_score(user_hand) > 21:
                # If the player's score exceeds 21, they bust and lose
                print("You busted! Dealer wins.")
                return  # End the game
        else:
            break  # Player chooses to stop hitting
    
    # Display the dealer's intital two cards 
    print(f"\nDealer's hand: {', '.join(f'{card.face} of {card.suit}' for card in dealer_hand[:2])}")
    
    dealer_score = calculate_score(dealer_hand)  
    # Calculate the dealer's score
    
    # Dealer's turn: draw cards until the score is at least 17
    while dealer_score < 17:
        dealer_hand.append(deck.get_card())
        dealer_score = calculate_score(dealer_hand)
    
    # Display the dealer's final hand and score
    display_hand(dealer_hand, "Dealer")
    
    # Determine the outcome of the game
    user_score = calculate_score(user_hand)
    
    if dealer_score > 21:
        print("Dealer busted, you win!")  # Dealer busts
    elif user_score > dealer_score:
        print("You win!")  # Player has a higher score
    elif user_score < dealer_score:
        print("Dealer wins!")  # Dealer has a higher score
    else:
        print("It's a tie!")  # Scores are equal

def main():
    # Main loop to run multiple games.
    deck = DeckOfCards()  # Create a deck outside the game loop
    deck.shuffle_deck()   # Shuffle the deck at the start

    while True:
        play_game(deck)  # Play a round with the current deck
        if input("\nAnother game? (y/n): ").strip().lower() != 'y':
            print("Thanks for playing!")
            break  # Exit the loop and end the game

if __name__ == "__main__":
    main()  # Start the game