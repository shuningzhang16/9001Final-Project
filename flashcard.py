class FlashCard:
    def __init__(self, english: str, chinese: str):
        self.english = english.strip()
        self.chinese = chinese.strip()

    def check_answer(self, user_input: str) -> bool:
        return self.chinese.lower().replace(" ", "") == user_input.strip().lower().replace(" ", "")
