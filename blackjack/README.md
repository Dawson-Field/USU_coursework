# Blackjack Game 

## Overview

This program simulates a simple version of the card game Blackjack (also known as 21). The goal of the game is to draw cards that add up to, but not over, 21. The program allows the user to play against a dealer, with the dealer drawing cards until their score is 17 or higher. The game includes card dealing, shuffling, handling of Aces (which can be worth either 1 or 11), and determining the winner based on the user's and dealer's scores.

## Program Requirements

1. **Game Rules**:
   - The **user wins** if:
     - The user's score is higher than the dealer's score without exceeding 21.
     - The dealer "busts" (goes over 21).
     - The user gets 21 with their first two cards (a "Blackjack").
   
   - The **user loses** if:
     - The user "busts" (their score exceeds 21).
     - The dealer's score is equal to or higher than the user's and does not exceed 21.

2. **Deck Setup**:
   - The game uses a `DeckOfCards` object, which contains 52 `Card` objects. 
   - The deck is shuffled before the game starts and printed to show the shuffle.
   - The cards are drawn from the deck, and their values are scored accordingly:
     - Cards 2–10 are worth their face value.
     - Jack, Queen, and King are worth 10 points.
     - Ace is worth either 1 or 11, depending on the user's total score.

3. **Gameplay**:
   - The user is dealt two cards, and the dealer is also dealt two cards.
   - The user's cards and score are displayed.
   - The user is then asked if they would like a "hit" (draw another card) or "stand" (keep their current hand).
   - If the user's score exceeds 21, they lose.
   - If the user decides to stand, the dealer reveals their cards and continues to draw cards until their score reaches 17 or higher.
   - The game ends when either the user or the dealer busts, or when both have stood, and their scores are compared.

4. **Ace Handling**:
   - An Ace can be worth either 1 or 11 points. The program automatically adjusts the value of Aces to prevent the user or dealer from busting if they have one or more Aces.

5. **Input Validation**:
   - The program validates all user inputs, requiring 'y' or 'n' responses for hit/stand and play again decisions.
   - Invalid inputs prompt the user to enter a valid response.

6. **Game Loop**:
   - After each round, the user is asked if they want to play again.
   - If they choose "yes", the deck is reshuffled and the game starts over.
   - The program prints the deck before and after each shuffle to verify proper shuffling.

## Files

- **DeckOfCards.py**: Contains the `Card` and `DeckOfCards` classes, which handle the card deck, card dealing, and shuffling.
- **play_game.py**: This file contains the main game logic and interacts with the `DeckOfCards` class to play the game.

## Example Output
```
Welcome to Black Jack!

deck before shuffled:
2 of Hearts, 3 of Hearts, 4 of Hearts, ...

deck after shuffled:
8 of Hearts, 10 of Clubs, King of Clubs, ...

Card number 1 is: 8 of Hearts
Card number 2 is: 10 of Clubs
Your total score is: 18
Would you like a hit?(y/n) n

Dealer card number 1 is: 9 of Spades
Dealer card number 2 is: King of Diamonds
Dealer score is: 19
Dealer score is higher, you lose!

another game?(y/n): y
```

## Contact
For any questions or feedback, feel free to contact me at [dawsontfield@gmail.com](mailto:dawsontfield@gmail.com).