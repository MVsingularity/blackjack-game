# Blackjack
import random
# Planning
    # Dealer cards
dealer_cards = []
    # Player cards
player_cards = []
    # Deal the cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has x &:", dealer_cards[1])

# player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

    # Display the cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")
if sum(dealer_cards) < 16:
    dealer_cards.append(random.randint(1,11))
    print("The dealer has x &:", dealer_cards[1], dealer_cards[2])
    # Sum of the dealer cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?"))
    if action_taken == "hit":
        player_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
            break
        else:
            print("You win!")
            break

    if sum(player_cards) > 21:
        print("You BUSTED! Dealer wins.")
    elif sum(player_cards) == 21:
        print("You have BLACKJACK! You win!! 21")

    # Sum of the Player cards
    # Compare the sums
    # If P card sum is greater than 21 =Bust
    # If P card sum is less than 21 = Hit or stay
    # If P option stay compare sum of D and P
    # If P sum < 21 && > D sum then P wins
    # If P sum < D sum then P loses
