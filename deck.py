from flashcard import FlashCard
import random

class FlashCardDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, english: str, chinese: str):
        self.cards.append(FlashCard(english, chinese))

    def load_default_cards(self):
        
        words = [
            ("apple", "苹果"),
            ("book", "书"),
            ("cat", "猫"),
            ("hello", "你好"),
            ("water", "水"),
            ("computer", "计算机"),
            ("language", "语言")
        ]
        for en, zh in words:
            self.add_card(en, zh)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self):
        return self.cards.copy()
