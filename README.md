# Python Quiz Game

A simple Python-based quiz game that tests your general knowledge with true/false questions.

## Features
- Uses a question bank from predefined data.
- Tracks your score and provides feedback on each answer.
- Supports multiple question sets from `question_data` and `trivia_data`.

## Setup and Run
1. **Clone the Repository**:
   - Open a terminal and run: `git clone https://github.com/ob-cheng/python-oop-quiz-game.git`.
2. **Navigate to the Project**:
   - Run: `cd python-oop-quiz-game`.
3. **Ensure Python is Installed**:
   - Verify Python 3 is installed by running `python --version` or `python3 --version`.
4. **Run the Game**:
   - Execute: `python main.py` or `python3 main.py` to start the quiz.

## Files
- `main.py`: Entry point to run the quiz.
- `question_model.py`: Defines the `Question` class to structure questions and answers.
- `data.py`: Contains the question datasets (`question_data` and `trivia_data`).
- `quiz_brain.py`: Manages the quiz logic, score, and user interaction.

## Usage
Answer each question with "True" or "False". The game continues until all questions are answered, then displays your final score.
