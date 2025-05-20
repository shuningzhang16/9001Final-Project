from deck import FlashCardDeck
from game import FlashLangGame

def main():
    deck = FlashCardDeck()
    deck.load_default_cards()
    game = FlashLangGame(deck)
    game.start()

if __name__ == "__main__":
    main()
