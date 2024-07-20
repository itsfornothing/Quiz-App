Quizzler is a quiz application that fetches trivia questions from the Open Trivia Database (OpenTDB) and displays them to the user through a graphical user interface (GUI) created with Tkinter. Users can answer the questions by pressing True or False buttons, and their score is updated based on their answers.

Features
- Fetches trivia questions from the OpenTDB API.
- Displays questions in a Tkinter GUI.
- Allows users to answer True/False questions.
- Updates and displays the user's score.
- Changes the background color of the question canvas based on the correctness of the answer.

- ## Installation
1. Clone the repository to your local machine.
2. Ensure you have Python installed (preferably Python 3.8+).
3. Install the required packages using pip:
    ```bash
    pip install requests
    ```

## Usage
1. Run the `main.py` file to start the application:
    ```bash
    python main.py
    ```
2. The application will fetch 10 True/False questions from the OpenTDB API and display them one by one.
3. Answer each question by clicking the True or False button.
4. Your score will be updated and displayed after each question.
5. After all quest

## Files
- `main.py`: The main entry point of the application.
- `data.py`: Fetches quiz data from the OpenTDB API.
- `question_model.py`: Defines the `Question` class used to model each quiz question.
- `ui.py`: Creates the user interface using Tkinter.
- `quiz_brain.py`: Contains the logic for handling the quiz.

## Example
```python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
