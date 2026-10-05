from itertools import combinations
from deckClass import Deck
from cardClass import Card


class Scoring:

    

    def fifteens(self, cards: list[Card]):
        score = 0

        for size in range(2, len(cards) + 1):
            for combination in combinations(cards, size):

                total = sum(card.get_Pegvalue() for card in combination)

                if total == 15:
                    score += 2

        return score
        
    def pairs(self, cards: list[Card]):
        score = 0
        #print(combinations(cards, 2))
        for card1, card2 in combinations(cards, 2):

            if card1.rank == card2.rank:
                score += 2

        return score

    def runs(self, cards: list[Card]):
        for size in range(len(cards), 2, -1):        # longest first
            score = 0
            for combination in combinations(cards, size):
                ranks = sorted(card.get_Runvalue() for card in combination)
                if len(set(ranks)) == size and ranks[-1] - ranks[0] == size - 1:
                    score += size
            if score:
                return score      # stop at the longest run length found
        return 0


    

    def flush(self, hand: list[Card], starter: Card, isCrib=False):

        if len(set(card.suit for card in hand)) != 1:
            return 0
        if isCrib:
            if starter is not None:
                if hand[0].suit == starter.suit:
                    return 5
            else:
                return 0
        if starter is not None:
            if hand[0].suit == starter.suit:
                return 5
        return 4

    def rightJack(self, hand: list[Card], starter: Card):
        if starter is None:
            return 0
        for card in hand:
            if card.rank == "J" and card.suit == starter.suit:
                return 1

        return 0

    def score_hand(self, hand: list[Card], starter: Card, isCrib=False):
        if starter is not None:
            cards = hand + [starter]
        else:
            cards = hand

        score = 0
        score += self.fifteens(cards)
        score += self.pairs(cards)
        score += self.runs(cards)
        score += self.flush(hand, starter,isCrib)
        score += self.rightJack(hand, starter)

        return score
        