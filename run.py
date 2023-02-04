import gspread
from google.oauth2.service_account import Credentials
import string


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
answers = SPREADSHEET.worksheet('answers')


topic1 = questions.get_all_values()
# get_answers = answers.get_all_values()

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
    and the values sorted
    """
    score = 0
    for num, (q, a) in enumerate(questions.items(), start=1):
        print(f"\n{num}: {q}")
        correct_answer = a[0]
        sort_label = dict(zip(string.ascii_uppercase, sorted(a)))
        for label, a in sort_label.items():
            print(f" {label}. {a}")
# create stand-alone function for checking score
        a_label = input('\n Your answer: ').upper()
        answer = sort_label[a_label]
        if answer == correct_answer:
            score += 1
            print("You got the answer right")
        else:
            print(f"Sorry, the correct answer is {correct_answer}")

    return score


def start_game():
    """
    The function will start a new quiz displaying the rules, asking
    for a username (and displaying topics)
    """

    print("\n Welcome to The History Quiz")

    # get_username()

    print("\n Do you want to start a new quiz?")

    # get_questions()


def get_username():
    """
    Gets username for user
    """
    while True:
        username = input("Please choose a username: ").strip()

        if username == '':
            print("Username must not be empty")
        elif not len(username) > 2:
            print("Your username must contain at least 3 characters")
        else:
            print(f"Hi {username}!")
            break
    return username


def update_worksheet(data, worksheet):
    """
    Push username and score to the leaderboard worksheet
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SPREADSHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def replay():
    while True:
        yes_no = input("\n Would you like to play again?\n Y / N: ").upper()

        if yes_no not in ("Y", "N"):
            print("Please try again")
        elif yes_no == "Y":
            return True
        else:
            return False


def main():
    """
    Runs the main program
    """
    username = get_username()
    start_game()
    score = get_questions()
    data = username, score
    user_score = [i for i in data]
    update_worksheet(user_score, 'leaderboard')

    while replay():
        start_game()

    print('goodnight')


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
