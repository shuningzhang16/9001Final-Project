from formatter import print_boxed_title, print_divider, print_summary_line

class GameResult:
    def __init__(self, total_questions: int, correct_answers: int, duration: float):
        self.total_questions = total_questions
        self.correct_answers = correct_answers
        self.duration = duration

    def accuracy(self) -> float:
        if self.total_questions == 0:
            return 0.0
        return round((self.correct_answers / self.total_questions) * 100, 1)

    def display(self):
        print_boxed_title("Quiz Summary")
        print_summary_line("Total Questions:", self.total_questions)
        print_summary_line("Correct Answers:", self.correct_answers)
        print_summary_line("Accuracy:", f"{self.accuracy()}%")
        print_summary_line("Time Taken:", f"{self.duration} seconds")
        print_divider()
