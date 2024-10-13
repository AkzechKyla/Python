import pydealer as pd

deck = pd.Deck()
deck.shuffle()
dealt_cards = deck.deal(2)
player_hand = pd.Stack()

print(dealt_cards)
player_hand.add(dealt_cards)
print(player_hand)
