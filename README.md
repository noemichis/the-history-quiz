# The History Quiz

## Introduction

The History Quiz is a multi-topic, multi-choice quiz application built as Project Portfolio 3 for Code Institute Full-stack development course. It is a Python terminal game that utilizes a collection of libraries to expand functionality and runs in the Code Institute mock terminal deployed on Heroku. The main inspiration was my deep interest for old civilizations, their life and their beliefs. Hence it targets anyone who shares similar interests and has a curiosity to test themselves. 

![Site landing page](assets/readme/start.png)
#### [**Live Website here**](https://the-history-quiz.herokuapp.com/)

## User Experience

### User goals
- Understand the purpose of the game
- Play the game and receive feedback for each answers
- See the result after a game is played
- Store final results and compare it with other players
- Have multiple game options

### Developer goals
- Build an easy to play, interactive game
- Retrieve topics and questions from Google Spreadsheets
- Add variety so questions and answers are randomized
- Display feedback to user if input not valid
- Offer choices to user once a game is over
- Usernames and score to be stored in Google Spreadsheets

## Design
[ASCII art](https://en.wikipedia.org/wiki/ASCII_art) is used to give the application more character. The topic names were created with the help of [Patjork](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20), text to ASCII art generator.

## Logic

### Flowchart
![Initial flowchart](assets/readme/flowchart.png) 

## Features

### Logo and username prompt 
![Logo and prompt for username](assets/readme/logo_username.png)

  - When the program is launched the logo is displayed together with a prompt to input username

### Welcome and Quiz Rulez
![Rules](assets/readme/welcome_rules.png)

  - Once the username is entered a welcome message is displayed with the instructions to play
  - The user is given time to read the instructions and once ready to start they can press any key

### Topic display
![List of topics](assets/readme/choose_topic.png)

  - The user has the option to choose from the topics listed, by entering A,B,C,D. Any other input will raise a retry message.

### Topic names
![Vikings-text](assets/readme/vikings.png)

![Romans-text](assets/readme/romans.png)

![Egypt-text](assets/readme/egypt.png)

![Greece-text](assets/readme/greece.png)

  - After the selection has been made, the quiz starts by displaying the topic name with ASCII art

### Questions and answers
  - Currently there are 10 questions for each topic

![Question-answers](assets/readme/ABCD_only.png)
  - The question and answer pairs are randomized and labeled.
  - The questions and answers are being printed with typewriter effect
  - If the answer is not valid a retry message is shown

### Answer feedback
  - Displays if correct:

![Message if correct](assets/readme/correct.png)

  - Displays if incorrect:

![Message if incorrect](assets/readme/incorrect.png)

### Result feedback
  - At the end of a quiz feedback is given according to how many questions the player gets correctly
  - Displays if less than 4 correct answers:

![Message if less than 4 correct](assets/readme/low.png)

  - Displays if less than 8 correct answers:

![Message if less than 8 correct](assets/readme/middle.png)

  - Displays if more 8 or more correct answers:

![Message if 8 or more correct](assets/readme/top.png)

### Menu
![Menu options](assets/readme/feedback_menu.png)

  - Choices after a game is finished
  - If the selection is not valid a retry message will be shown

### Leaderboard
![Leaderboard](assets/readme/leaderboard.png)

  - If player decides to check the Leaderboard, their score will be pushed to Google Sheets then TOP 10 scores are displayed(or as many as exist)
  - Menu options show again

### Play Again
  - If the player decides to play again, the terminal window is cleared and the topics are displayed, allowing to select a new one

### Quit
![Quit game](assets/readme/exit.png)

  - The game will end with a thank you message


## Future Implementations

#### **Variety of topics and questions**
In the future would be nice to add a variety of topics and increase the number of questions. As the questions will be always randomized, the users will enjoy a better selection and the game will be used more often.

#### **More complex score**
I would like to add a functionality where the player can choose to play further rounds and improve their score. When they decide to finish playing the total number of correct answers will be returned from all rounds. The player must not be able to select the quiz he already completed in the one score keep period. 


## Storage
Google Sheets is used to store all the data the project uses, starting from the questions and answers to the username and score, which the Leaderboard consists of. 
The spreadsheet is connected via Google Drive and Google Sheet API. The credentials are stored in creds.json which is further added to Git ignore to protect the sensitive data and make sure they are not made public. 
The topics are organized in separate worksheets, this way I can easily manage, update and access them. The Leaderboard is another worksheet where the **username** and **score** are stored, then the TOP 10 is displayed on the users call. 

## Testing

|Test | Completed |
|:--- |   :---:   |
|Logo displayed from game_art| Yes |
|Player asked to enter username | Yes |
|Username validation: input can not be empty and must contain minimum 3 characters | Yes |
|Welcome message displayed with capitalized username | Yes |
|Game rules displayed | Yes |
|Topic choices displayed | Yes |  
|Both uppercase and lowercase is accepted | Yes |
|Topic name imported and displayed from game_art | Yes |
|Questions/answers are displayed from correct topic | Yes |
|Questions/answers labeled and randomized | Yes |
|Topic/answer validation: input can only be A,B,C,D | Yes |
|Question feedback if correct | Yes |
|Question feedback if incorrect and show correct answer | Yes |
|Display total score and message | Yes |
|Display Menu | Yes |
|Selection validation: input can only be A,B,C | Yes |
|Select A: update and display leaderboard | Yes |
|Sort Leaderboard to return Top 10 | Yes |
|Select B: restart game and show topic choices | Yes |
|Select C: exists program | Yes |
|Typewriter effect | Yes |
|Terminal cleared | Yes |


### CI Python Linter
[CI Python Linter](https://pep8ci.herokuapp.com/) 
<details>
<summary>run.py</summary>
<br>
![Validation test for run.py]()
</details>
<details>
<summary>game_art.py</summary>
<br>
![Validation test for game_art.py]()
</details>

### W3C Markup 
[W3C Markup validator](https://validator.w3.org/)
<details>
<summary>HTML test</summary>
<br>
![Validation test for html]()
</details>

### W3C CSS 
[W3C CSS Validator](https://jigsaw.w3.org/)
<details>
<summary>CSS test</summary>
<br>
![Validation test for css]()
</details>

## Bugs
Along the development of this project I came across some small bugs, but most were resolved quickly with online searching. A good thing was also to have the built in Python linter. By the end of this project, this extension really helped me learn a cleaner way to organize code and what to watch out for. 

### Fixed Bugs
#### Score is sorted as string

![Leaderboard displays number 10 at bottom](assets/readme/10_to_top.png)

- This bug was resolved by converting the returned score values into integers. Once this addition was made the Leaderboard is sorted and displayed as intended.

#### Line-too-long
- These errors were mainly resolved by splitting up the code into multiple variables.
### Unsolved
I wanted to add a background for the application, but it did not work. I tried to follow a couple recommendations I found on Slack:
  - using it's github url as a background property and as an embedded image
  - host and image on [Imgur](https://imgur.com/), but I was not able to create an account.

Since I was not able to resolve it I decided to remove the image for now and set a black background instead.   


## Technologies and resources

### Languages
Main language used to build logic and operations
- [Python](https://www.python.org/) 

Small intervention to the template with the help of
- [HTML5](https://en.wikipedia.org/wiki/HTML5)  
- [CSS](https://en.wikipedia.org/wiki/CSS)  

### Modules imported
- [os](https://docs.python.org/3/library/os.html): functions that interact with the OS
- [time](https://docs.python.org/3/library/time.html): used in typewriter function to define sleep time
- [random](https://docs.python.org/3/library/random.html): randomly sorts the questions and answers with the sample function
- [string](https://docs.python.org/3/library/string.html): functions to manipulate strings in the app
- [tabulate](https://pypi.org/project/tabulate/): print Leaderboard as pretty table
- [gspread](https://docs.gspread.org/en/v5.7.0/): allows access to Google Sheets
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html): validates credentials and grants access to Google

### Programs
- [Github](https://github.com) - version control and project repo
- [Gitpod](https://gitpod.io) - used as remote development platform to write and test code
- [Heroku](https://www.heroku.com/) - live deployment of the project
- [Figma](https://www.figma.com) - for flowchart design
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
- [Patjork](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) - generate game art
- [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - main help in debugging, linting and keeping to learning better habits quickly
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [Code Spell Checker](https://open-vsx.org/extension/streetsidesoftware/code-spell-checker) - VS Code extension 


## Deployment

The template used is the [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) provided by [Code Institute](https://codeinstitute.net/).

- New repository is created on Github from template.
- New workspace is then created on Gitpod

Custom modules are installed into application:
- Use `pip3 install <module>`
- Record all environmental requirements: `pip freeze3 > requirements. txt`

### Deploy to Heroku
- Create [Heroku](https://www.heroku.com/) account and log in
- Select `New` and click `Create new app`
- Choose **name**, **region** and `Create app`
- Navigate to `Settings`, into `Config vars` and reveal
- Enter Key: **PORT** Value: **8000**
- Enter Key: **CREDS** Value: *credentials* (content of *creds.json* in our case).
- Next got to `Buildpacks` and `Add Buildpack`
- Add *Pyhton* first, then *NodeJs*
- Navigate to `Deploy`  and choose *Github* as `Deployment method`
- Once connected to *Github* in `App connected to GitHub` find your repo name
- `Enable Automatic Deploys` if you want deploy new version after every push
- `Manual Deploys` if you want to control all deployments
- `View` link will be provided to navigate to the deployed page



## Credits & References
I researched many sites for better understanding of *Python*. I overall learned much, the ones below I used the most:
- [Python](https://www.python.org/) 
- [Stack Overflow](https://stackoverflow.com/)
  - [Typing effect](https://stackoverflow.com/questions/20302331/typing-effect-in-python) - inspiration code for typewriter
- [Real Python](https://realpython.com/)
    - [Understand idiom](https://realpython.com/if-name-main-python/#:~:text=Nesting%20code%20under%20if%20__,defined%2C%20but%20no%20code%20executes.) - understand use of __name__ == "__main__" idiom
- [PyPI](https://pypi.org/)  
    - [Tabulate](https://pypi.org/project/tabulate/) - help learn about returning data as a table
- [Delfstack](https://www.delftstack.com/)
    - [Sorting Lists](https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/) - help better understand list sorting
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
    - [Clearing screen](https://www.geeksforgeeks.org/clear-screen-python/)
    - [ASCII Uppercase](https://www.geeksforgeeks.org/python-string-ascii_uppercase/) - inspiration for labeling answers        
- [Docs Gspread](https://docs.gspread.org/en/v5.7.0/) - understand how to use **gspread** and learn more about error handling
- [W3Schools](https://www.w3schools.com)
- [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1) - great walkthrough project with lot to absorb


The questions for the quiz were created with the help of [Duckster](https://www.ducksters.com/), a platform which contains several facts on all kinds of different topics.

## Acknowledgments
- to the Slack community to answer questions even before they are asked and the great support they show us.


