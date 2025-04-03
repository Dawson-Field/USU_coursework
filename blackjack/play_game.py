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

def get_valid_input(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(valid_choices)}")

def play_game(deck):
    print("\nWelcome to Black Jack!")
    print("\ndeck before shuffled:")
    deck.print_deck()
    
    deck.shuffle_deck()
    print("\ndeck after shuffled:")
    deck.print_deck()
    
    user_hand = []
    dealer_hand = []
    
    # Deal initial cards
    for i in range(2):
        user_hand.append(deck.get_card())
        dealer_hand.append(deck.get_card())
    
    # Display user's cards
    for i, card in enumerate(user_hand, 1):
        print(f"\nCard number {i} is: {card.face} of {card.suit}")
    
    user_score = calculate_score(user_hand)
    print(f"Your total score is: {user_score}")
    
    # Check for automatic win with 21
    if user_score == 21:
        print("Blackjack! You win!")
        return
    
    # User's turn
    while True:
        choice = get_valid_input("Would you like a hit?(y/n) ", ['y', 'n'])
        if choice == 'y':
            new_card = deck.get_card()
            user_hand.append(new_card)
            print(f"\nCard number {len(user_hand)} is: {new_card.face} of {new_card.suit}")
            user_score = calculate_score(user_hand)
            print(f"Your total score is: {user_score}")
            
            if user_score > 21:
                print("You busted! Dealer wins!")
                return
        else:
            break
    
    # Dealer's turn
    print(f"\nDealer card number 1 is: {dealer_hand[0].face} of {dealer_hand[0].suit}")
    print(f"Dealer card number 2 is: {dealer_hand[1].face} of {dealer_hand[1].suit}")
    
    dealer_score = calculate_score(dealer_hand)
    card_count = 2
    
    while dealer_score < 17:
        new_card = deck.get_card()
        dealer_hand.append(new_card)
        card_count += 1
        print(f"Dealer hits, card number {card_count} is: {new_card.face} of {new_card.suit}")
        dealer_score = calculate_score(dealer_hand)
    
    print(f"Dealer score is: {dealer_score}")
    
    # Determine winner
    if dealer_score > 21:
        print("Dealer Busted, you win!!!")
    elif user_score > dealer_score:
        print("You win!")
    elif user_score < dealer_score:
        print("Dealer score is higher, you lose!")
    else:
        print("It's a tie!")

def main():
    deck = DeckOfCards()
    
    while True:
        play_game(deck)
        if get_valid_input("\nanother game?(y/n): ", ['y', 'n']) != 'y':
            break

if __name__ == "__main__":
    main()