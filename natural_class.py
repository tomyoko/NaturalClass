from random import shuffle

def is_set(cards):    
    features = ["shading", "color", "number", "shape"]
    for feature in features:
        unique_values = set()
        for card in cards:
            unique_values.add(card.get_value(feature))
        #TODO: return error if len(u_v) == 0 or if len(u_v) > len(cards)
        if 1 < len(unique_values) < len(cards):
            return False                            
    return True

class Game:    
    def __init__(self, deck, players):
        #TODO: allow 'deck' to be omitted, in which case default deck is created
        self.deck = deck
        self.players = players
        self.NUM_STARTING_CARDS = 9
        self.SET_LENGTH = 3

    def claim_set(self, selected_cards):
        if is_set(selected_cards):# - if correct:
            # - remove those cards
            for card in selected_cards:
                self.deck.cards_in_play.remove(card)
            # - track player score            
            # TODO: What if there's more than one player?
                self.players[0].change_score(self.SET_LENGTH)
            # - deal cards
            # TODO?     - if >=3 cards in deck, deal 3
            # - if <3 cards in deck, deal number in deck
            # - if <3 cards in play area, end game
                self.deck.deal(self.SET_LENGTH)                 
        else:    # - if incorrect:
            # - penalise player (track player score)
            self.players[0].change_score(-self.SET_LENGTH)

    def play(self):
        self.deck.deal(self.NUM_STARTING_CARDS)     # - deal 9 cards
        while True:    # - loop:
            #TODO: make cards look nicer!
            print(self.deck.cards_in_play)
            #TODO: handle errors
            does_set_exist = input("Is there a set? I need food. (Answer 'Y' for yes, 'N' for no.)")    # - user says whether there's a set                
            if does_set_exist == "Y":
                selected_indices = []
                for _ in range(self.SET_LENGTH):
                    selected_indices.append(int(input("Feed me a card. I'm so hungry!")))    # - if yes: evaluate chosen cards    
                selected_cards = []    
                for integer in selected_indices:
                    selected_cards.append(self.deck.cards_in_play[integer])
                self.claim_set(selected_cards)
            #finish this
            else:    # - if no:
                self.deck.deal(self.SET_LENGTH)     # - add 3 cards
                    # - if no cards to add, end game and declare winner

class Deck:
    def __init__(self):
        self.undealt_cards = []
        shadings = ["solid", "striped", "empty"]
        colors    = ["red", "green", "purple"]
        shapes    = ["oval", "diamond", "squiggle"]
        numbers    = ["one", "two", "three"]
        for shading in shadings:
            for color in colors:
                for shape in shapes:
                    for number in numbers:
                        self.undealt_cards.append(Card(shading, color, shape, number))
        shuffle(self.undealt_cards)
        self.cards_in_play = []

    def deal(self, number_of_cards):
        for _ in range(number_of_cards):
            self.cards_in_play.append(self.undealt_cards.pop())

class Player:
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def change_score(self, num_points):
        self.score = max(0, self.score + num_points)

class Card:
    def __init__(self, shading, color, shape, number):
        self.shading = shading
        self.color = color
        self.shape = shape
        self.number = number        
    def __repr__(self):
        return f"({self.shading}, {self.color}, {self.shape}, {self.number})"
    def get_value(self, feature):
        if feature == "shading":
            return self.shading
        elif feature == "color":
            return self.color
        elif feature == "shape":
            return self.shape
        elif feature == "number":
            return self.number
        else:
            print('Go fuck yourself. Give a real feature, asshole.') #TODO: Raise error


if __name__ == "__main__":
    d = Deck()
    d.deal(12)
    print(len(d.undealt_cards))
    print(len(d.cards_in_play))

