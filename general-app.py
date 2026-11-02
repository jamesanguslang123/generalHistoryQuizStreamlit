
import streamlit as st
import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Page settings
st.set_page_config(
    page_title="⚔️ Do you know your history!",
    page_icon="⚔️",
    layout="wide"
)

# Ollama settings
OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "gpt-oss:20b-cloud")


# Function to communicate with AI
def ask_ai(prompt):

    data = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    request = Request(
        f"{OLLAMA_URL}/api/generate",
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urlopen(request, timeout=120) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"]


# Website heading
st.title("⚔️ Do You Know Your History?")
st.write("Test your knowledge of history's greatest generals.")

st.divider()


# General selection
generalOptions = [
    "Napoleon Bonaparte",
    "Hannibal Barca",
    "Julius Caesar",
    "Alexander the Great",
    "Scipio Africanus",
    "Genghis Khan",
    "Sun Tzu",
    "Saladin",
    "Frederick the Great",
    "Other (enter your own)"
]

selectedGeneral = st.selectbox(
    "Who is your favourite historical general?",
    generalOptions
)

# Allow the user to enter their own general
if selectedGeneral == "Other (enter your own)":
    userGeneral = st.text_input("Enter your favourite general:")
else:
    userGeneral = selectedGeneral


# Difficulty selection
difficulty = st.selectbox(
    "Choose your difficulty:",
    ["Easy", "Medium", "Hard"]
)


# Store the question and feedback between Streamlit reruns
if "question" not in st.session_state:
    st.session_state.question = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""


st.divider()


# Generate question
if st.button("Generate History Question", type="primary"):

    if not userGeneral.strip():
        st.warning("Please enter a historical general first.")

    else:
        prompt = f"""
        You are a historical quizmaster.

        Generate ONE historically accurate {difficulty.lower()} difficulty
        question about the general {userGeneral}.

        Ask a clear question with one objectively checkable answer.
        Do not give away the answer.
        Do not include multiple questions.
        """

        try:
            with st.spinner("The history books are being consulted..."):
                st.session_state.question = ask_ai(prompt)

            st.session_state.feedback = ""

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as error:
            st.error(f"AI connection error: {error}")


# Display the question and answer box
if st.session_state.question:

    st.subheader("📜 Your Question")

    st.write(st.session_state.question)

    userAnswer = st.text_area(
        "Enter your answer:",
        placeholder="What is your answer?"
    )

    if st.button("Submit Answer"):

        if not userAnswer.strip():
            st.warning("You need to enter an answer!")

        else:
            checkingPrompt = f"""
            You are a fair historical quizmaster.

            Historical general: {userGeneral}

            Question: {st.session_state.question}

            User's answer: {userAnswer}

            Check whether the answer is historically correct.

            Accept different wording, spelling variations and equivalent
            historical names where appropriate.

            Do not mark a correct answer wrong just because it is worded
            differently.

            Give your response in this format:

            VERDICT: NOT A LARP / LARP DETECTED / CLOSE

            EXPLANATION: Explain why the answer is correct, incorrect
            or partially correct.

            CORRECT ANSWER: Give the historically accurate answer.
            """

            try:
                with st.spinner("Checking your historical knowledge..."):
                    st.session_state.feedback = ask_ai(checkingPrompt)

            except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as error:
                st.error(f"AI connection error: {error}")


# Display AI verdict
if st.session_state.feedback:

    st.divider()
    st.subheader("🏛️ Your Verdict")

    st.write(st.session_state.feedback)


# Generate another question
if st.button("Try Another Question"):
    st.session_state.question = ""
    st.session_state.feedback = ""
    st.rerun()
