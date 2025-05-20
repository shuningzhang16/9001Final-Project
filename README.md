# 9001Final-Project
FlashLang is a command-line flashcard learning tool developed in Python using only the standard library. No external libraries are required. The program helps users practice English-to-Chinese vocabulary translation and is designed for both language learners and programming beginners.
Main features include:
1. Prompts an English word and accepts a Chinese translation as input
2. Provides immediate feedback on whether the answer is correct, ignoring case and spacing differences
3. Automatically tracks the time taken to complete the quiz
4. Displays a final summary of total questions, correct answers, accuracy rate, and time used
The program follows a modular design with the following components:
flashcard.py defines the structure of a single flashcard and its answer-checking logic
deck.py manages the collection of flashcards, including loading and shuffling
game.py handles the game flow and user interaction
timer.py tracks the start and end time of the quiz
result.py calculates and displays performance statistics
formatter.py ensures consistent and clear output formatting
main.py serves as the entry point and initializes the game
To run the program, open a terminal in the project folder and execute python main.py to begin the quiz.
The program is cleanly structured and suitable for educational use. Its modular architecture also supports future extensions such as error tracking, file-based word imports, and reverse-mode quizzes.
