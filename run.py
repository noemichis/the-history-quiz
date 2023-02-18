import os
from time import sleep
import random
import string
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
import game_art


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Variables to easier access Google Sheets
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open("the_history_quiz")

# Worksheets saved as variables
TOPIC_1 = SPREADSHEET.worksheet("topic1")
TOPIC_2 = SPREADSHEET.worksheet("topic2")
TOPIC_3 = SPREADSHEET.worksheet("topic3")
TOPIC_4 = SPREADSHEET.worksheet("topic4")
l_board = SPREADSHEET.worksheet("Leaderboard")


def typewriter(word, speed=0.03):
    """
    Typewriter function to be reused for certain prints
    Code from:
    https://stackoverflow.com/questions/20302331/typing-effect-in-python
    """
    for i in word:
        print(i, end='', flush=True)
        sleep(speed)


def choose_topic():
    """
    Allows user to select the topic they wish to play
    """
    while True:
        print(game_art.TOPIC_LIST)
        typewriter("\n Choose your topic: ")
        selection = input().upper()
        if validate_answer(selection):
            break
    os.system("clear")
    return selection


def validate_answer(values):
    """
    Validates users answer input and returns
    error message if not in A, B, C, D
    """
    try:
        if values not in ("A", "B", "C", "D"):
            raise ValueError("The valid options are A,B,C,D, try again.")
    except ValueError as exc:
        print(f"\n {exc}")
        return False
    return True


def get_topic_wks(selection):
    """
    Checks which letter was selected and opens the
    corresponding worksheet to get the topic questions
    """
    if selection == "A":
        print(game_art.VIKINGS)
        questions = question_dict(TOPIC_1)
    elif selection == "B":
        print(game_art.ROMANS)
        questions = question_dict(TOPIC_2)
    elif selection == "C":
        questions = question_dict(TOPIC_3)
        print(game_art.EGYPT)
    else:
        questions = question_dict(TOPIC_4)
        print(game_art.GREECE)
    return questions


def question_dict(selection):
    """
    Loops through values returned and create dictionary
    """
    topic = selection.get_all_values()
    questions = {col[0]: col[1:] for col in topic}
    return questions


def display_questions(questions):
    """
    Loops through questions dictionary and displays the keys enumerated
    and the answers sorted randomly
    """
    quest = random.sample(list(questions.items()), k=10)

    score = 0
    for num, (prompt, option) in enumerate(quest, start=1):
        typewriter(f"\n{num}: {prompt}\n")
        correct_answer = option[0]
        random_option = random.sample(option, k=len(option))
        random_label = dict(zip(string.ascii_uppercase, random_option))
        for label, option in random_label.items():
            typewriter(f" {label}. {option}\n")
        while True:
            choice = input("\nYour answer: ").upper()
            if validate_answer(choice):
                break
        answer = random_label[choice]
        score += check_answer(correct_answer, answer)
    show_score(score, len(questions))
    return score


def check_answer(correct_answer, answer):
    """
    Checks if users answer is the correct one,
    if it is returns 1.
    """
    if answer == correct_answer:
        typewriter(" That's right!\n")
        return 1
    typewriter(f" Ooops, the correct answer is '{correct_answer}'\n")
    return 0


def show_score(score, num):
    """
    Shows final score to the user
    """
    print("\n __________________________________________________")
    text = f"{score} out of {num}"
    if score <= 3:
        typewriter(f"\n   Hmmm, {text}, better luck next time!")
    elif score <= 7:
        typewriter(f"\n   Oh nice, {text}, that's a good start!")
    else:
        typewriter(f"\n   Look at that, {text}, you're rocking it!")
    print("\n __________________________________________________")


def check_wks(worksheet):
    """
    Opens worksheet and filters out exceptions
    """
    try:
        SPREADSHEET.worksheet(worksheet)
        return True
    except (
        gspread.exceptions.WorksheetNotFound,
        gspread.exceptions.APIError
    ):
        print(" An error occurred, we can not access the Leaderboard")
        return False


def update_worksheet(data, worksheet):
    """
    Push username and score to the Leaderboard worksheet
    """
    if check_wks(worksheet):
        typewriter(f"\n Updating {worksheet}...\n")
        l_board.append_row(data)
        typewriter(f"\n {worksheet} updated successfully.\n")


def display_leaderboard(worksheet):
    """
    Displays the top 10 from the Leaderboard on choice of the user
    """
    if check_wks(worksheet):
        data = l_board.get_all_values()
        top_10 = sorted(data, key=lambda x: int(x[1]), reverse=True)
        headers = ["Player", "HighScore"]
        board = tabulate(top_10[:10], headers, tablefmt="outline")
        print(game_art.LEADER_BOARD)
        print(f"{board}")


def replay(score):
    """
    Function to prompt user about their next action.
    """
    while True:
        print(game_art.CHOICES)
        user_choice = input().upper()
        if user_choice == "A":
            data = username, score
            update_worksheet(data, "Leaderboard")
            display_leaderboard("Leaderboard")
        elif user_choice == "B":
            os.system("clear")
            main()
        elif user_choice == "C":
            typewriter("\n Thank you for playing, see you next time!\n")
            quit()
        else:
            print(" The valid options are A,B,C, try again.")


def main():
    """
    Runs the main program
    """
    score = 0
    topic = choose_topic()
    questions = get_topic_wks(topic)
    score += display_questions(questions)
    replay(score)


if __name__ == '__main__':
    os.system("clear")
    print(game_art.GAME_LOGO)
    typewriter("\n Please enter your name: ")
    while True:
        username = input().strip()
        username = username.capitalize()
        if username == '':
            print("Username must not be empty")
        elif not len(username) > 2:
            print("Your username must contain at least 3 characters")
        else:
            break
    os.system("clear")
    typewriter(f"\n Welcome, {username}!\n")
    print(game_art.RULES)
    typewriter(" Press any key to continue ")
    input()
    os.system("clear")

    main()
