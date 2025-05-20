from formatter import print_boxed_title
from timer import Timer
from result import GameResult

class FlashLangGame:
    def __init__(self, deck):
        self.deck = deck
        self.score = 0
        self.timer = Timer()

    def start(self):
        print_boxed_title("Welcome to FlashLang")
        self.deck.shuffle()
        cards = self.deck.get_cards()
        self.timer.start()

        for i, card in enumerate(cards):
            print(f"\n[Card {i+1}] Translate to Chinese: {card.english}")
            answer = input("Your answer: ")
            if card.check_answer(answer):
                print("Correct.")
                self.score += 1
            else:
                print(f"Wrong. Correct answer: {card.chinese}")

        self.timer.stop()
        result = GameResult(len(cards), self.score, self.timer.duration())
        result.display()
