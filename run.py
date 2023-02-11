import gspread
from google.oauth2.service_account import Credentials
import string
import random
from tabulate import tabulate
import game_art


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SPREADSHEET = GSPREAD_CLIENT.open('the_history_quiz')

questions = SPREADSHEET.worksheet('questions')
l_board = SPREADSHEET.worksheet('leaderboard')


topic1 = questions.get_all_values()

# loop through values returned and create dictionary
questions = {}
for select in topic1:
    question = select[0]
    answers = select[1:]
    questions[question] = answers


# creates quiz
def get_questions():
    """
    Loops through questions dictionary and displays the keys enumerated
    and the answers sorted randomly
    """
    score = 0
    for num, (prompt, option) in enumerate(questions.items(), start=1):
        print(f"\n{num}: {prompt}")
        correct_answer = option[0]
        random_label = dict(zip(string.ascii_uppercase, random.sample(option, k=len(option))))
        for label, option in random_label.items():
            print(f" {label}. {option}")
        choice = input('\n Your answer: ').upper()
        answer = random_label[choice]
        score += validate_answer(correct_answer, answer)
    show_score(score, len(questions))


def validate_answer(correct_answer, answer):
    """
    Checks if users answer is the correct one,
    if it is returns 1.
    """
    if answer == correct_answer:
        print("That's right!")
        return 1
    else:
        print(f"Sorry, the correct answer is {correct_answer}")
        return 0


def show_score(score, num):
    """
    Shows final score to the user
    """
    print(f"\nYou got {score} out of {num} questions")
    data = username, score
    update_worksheet(data, 'leaderboard')


def update_worksheet(data, worksheet):
    """
    Push username and score to the leaderboard worksheet
    """
    print(f"Updating {worksheet}...\n")
    worksheet_to_update = SPREADSHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully.\n")


def display_leaderboard():
    """
    Displays the top 10 from the leaderboard on choice of the user
    """
    data = l_board.get_all_values()
    top_10 = sorted(data, key=lambda x: x[1], reverse=True)
    board = tabulate(top_10[:10], headers=['Player', 'HighScore'], tablefmt="outline")
    print(board)


def replay():
    """
    Function to prompt user about their next action.
    """
    while True:
        user_choice = input("\n Please choose an option:\nA. Check Leaderboard\nB. Play Again\nC. Quit\n").lower()
        if user_choice == 'a':
            display_leaderboard()
        elif user_choice == "b":
            get_questions()
        else:
            return False


def main():
    """
    Runs the main program
    """
    get_questions()
    replay()
    print('GoodBye')


if __name__ == '__main__':
    print(game_art.GAME_LOGO)
    print("\n Welcome to The History Quiz\n")
    print("Please enter your name to start the game:")
    while True:
        username = input("\n").strip()
        if username == '':
            print("Username must not be empty")
        elif not len(username) > 2:
            print("Your username must contain at least 3 characters")
        else:
            break
    print(f"\n Hi {username}!\n")
    input("\n Press a key to start a new quiz\n")

    main()


# question_num = 1
# for question in question_list:
#     print(question)
#     for answer in get_answers[question_num-1]:
#         print(answer)

#     question_num += 1

# try:
#     if len(username) > 2:
#         print(f"Hi {username}!")
#         break
# except TypeError:
# print("Your username must contain at least 3 characters")
