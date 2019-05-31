# Problem Statement
#
# You are dealing cards to a group of players. In this game, the cards are numbered 0-9 and have no distinguishing characteristics other than their numbers. A given deck may have many cards that share the same number. You are given an integer numPlayers that represents the number of people playing. You are also given a string deck which contains the cards to be used (0th character is the top of the deck, and the last character is the bottom). You will deal the cards starting with player 0, then player 1, until you reach player numPlayers-1, dealing one card at a time. Then you repeat this process until the cards are exhausted. Cards are always dealt from the top of the deck.  You will return a tuple (string) that shows each of the players' cards in the order they were dealt (cards dealt earlier show up earlier in the particular string). Player k's hand corresponds to element k of the returned tuple (string). One added constraint is that each player must be dealt the same number of cards. To enforce this constraint you will not deal extra cards that will unbalance the players' hands (cards held). In other words, if you have dealt to the last player, and don't have enough cards to deal another to every player, stop dealing. The returned tuple (string) must contain exactly numPlayers elements, each element containing exactly the same number of characters.
# Definition
#
# Class:
# CardCount
# Method:
# dealHands
# Parameters:
# integer, string
# Returns:
# tuple (string)
# Method signature:
# def dealHands(self, numPlayers, deck):

# Gendo90 has submitted the 250-point problem for 192.91 points
# Successful on first try!
class CardCount(object):
    def dealHands(self, numPlayers, deck):
        num_cards_used = len(deck)-(len(deck)%numPlayers)
        cards_used = [card for card in deck[:num_cards_used]]
        print(cards_used)
        hands = ["" for player in range(numPlayers)]
        while(cards_used):
            for i in range(len(hands)):
                hands[i] += cards_used.pop(0)

        return tuple(hands)


test = CardCount()

print(test.dealHands(6, "012345012345012345"))
