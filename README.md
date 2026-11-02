# ⚔️ General's Gauntlet

**Test your knowledge of history's greatest military commanders.**

General's Gauntlet is an AI-powered history quiz game built with Python and Streamlit. Choose a historical general, receive an AI-generated question, and submit your answer to see whether you know your history.

## Features

- Choose from historical generals such as Hannibal Barca, Napoleon Bonaparte, Julius Caesar and Alexander the Great.
- Enter your own historical general.
- Select a difficulty level: Easy, Medium or Hard.
- Generate history questions using AI.
- Submit answers and receive AI-powered feedback.
- Get an explanation of the correct answer.

## Technologies Used

- Python
- Streamlit
- Ollama
- Large Language Models (LLMs)

## How to Run

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project folder:

   ```bash
   cd generals-gauntlet
   ```

3. Install the required packages:

   ```bash
   pip install streamlit
   ```

4. Make sure Ollama is installed and running, with your chosen model available.

5. Start the application:

   ```bash
   streamlit run general-app.py
   ```

6. Open the local URL provided in your terminal.

## How It Works

The application sends prompts to an AI model through Ollama. The model generates a question about the selected general and later evaluates the user's answer, providing feedback and an explanation.

## Future Improvements

- Add more historical generals and historical periods.
- Improve question accuracy using reliable historical sources.
- Add a scoring and leaderboard system.
- Add different question types.
- Improve the user interface.

## Important Note

Questions and answer evaluations are AI-generated, so historical information and marking may occasionally be inaccurate. Answers should be checked against reliable historical sources.

---

**Created as an independent Python and AI development project.**
