import gspread
from google.oauth2.service_account import Credentials

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


question_list = questions.get_all_values()
get_answers = answers.get_all_values()

question_num = 1

for question in question_list:
    print(question)
    for answer in get_answers[question_num-1]:
        print(answer)

    question_num += 1


# for question, answer in question_list, answ:
#     print(question, answer)

# dict(zip(question_list, get_answers))

# print(my_dict)

# for answer_select in range(len(get_answers)):
#     for answer in get_answers[answer_select]:
#         print(answer, end=" ")
#     print()

# print(answer_list)

# for question, answer in question_list, answer_l:

#     print(f"{question}\n {answer}")

# print(f"{question}\n {answer_list}")
