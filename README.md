# The Battle of Ships

![Website Application Mock Up](assets/mock-up/multi-device-mockup.png)


## [Link to Live Website](https://battleships-game-board-5c541f06f660.herokuapp.com/)

# Purpose 

"The Battle of Ships" is a digital version of the traditional Battleships game, where player can compete against an AI opponent. The game serves as an example of how to structure a game project in code, manage game state, and implement basic AI logic. It is also a great resource for those interested in learning about grid-based games, strategy development, and user interaction in software. 

- The game is built in Python as Milestone Project #3 for the Code Institute's Full Stack Software Development course.

-------

# User Experience (UX) and Design

## User Stories

- As a user, I want to understand the purpose and intention of the site and application when I run
  the program.
- As a user, I want the navigation to be intuitive and easy to understand.
- As a user, I want to be able to enter my name before I start to play the game.
- As a user, I would like to see a welcome message and my name added to the program for more engaging
  experience.
- As a user, I want my input to be validated and error checked each time, so I can re-enter my
  input/choice if it is invalid.
- As a user, I should not have to worry about capitalizing or lowercase when typing.
- As a user, I want to see the score after each turn.
- As a user, I want see the final result to see how many times I tried or computer tried to win the game.
- As a user, I want to have an opportunity to play again regardless of success or failure in the game.

## Design

### Data Model Overview

The Battleships game is built using an object-oriented approach, which organizes the game's logic into several classes: Ship, Board, and Game. Each class is designed to represent a specific aspect of the game, making the code modular, reusable, and easy to maintain.

### Key Classes and Attributes
#### 1. Ship
 - Purpose: The Ship class represents a ship in the game, including its size and current status.
##### Attributes:
 - size: The size of the ship, representing how many grid cells it occupies.
 - positions: A list of integers representing the ship's position on the grid. Each position corresponds to a cell number on the board.
##### Methods:
 - is_sunk(): Checks if the ship has been sunk, returning True if all positions have been hit (i.e., the list of positions is empty), otherwise False.

#### 2. Board
 - Purpose: The Board class represents the game board where ships are placed and where guesses (shots) are made.
##### Attributes:
 - taken_positions: A list of integers representing all the positions on the board that are occupied by ships.
 - ships: A list of Ship objects representing all the ships placed on the board.
 - hits: A list of integers representing the positions that have been hit by guesses.
 - misses: A list of integers representing the positions that have been guessed but did not hit a ship.
 - completions: A list of integers representing positions where ships have been completely sunk.
##### Methods:
 - check_ok(boat): Validates whether a ship's placement is valid, checking for overlaps, out-of-bound positions, and correct alignment.
 - add_ship(ship): Allows the player to manually add a ship to the board by specifying its positions.
 - auto_add_ship(ship): Automatically places a ship on the board by randomly selecting valid positions.
 - show_board(reveal_ships=False): Displays the board, showing hits, misses, and (optionally) the positions of ships.
 - check_shot(shot): Checks if a shot hits any ship on the board and updates the ship's status accordingly.

#### 3. Game
##### Purpose: 
 - The Game class manages the setup, progression, and conclusion of the game. It controls both the player’s and computer’s boards and tracks scores.
##### Attributes:
 - player_board: An instance of the Board class representing the player's board.
 - computer_board: An instance of the Board class representing the computer's board.
 - computer_board: An instance of the Board class representing the computer's board.
 - player_guesses: A list of integers representing the positions guessed by the player.
 - computer_guesses: A list of integers representing the positions guessed by the computer.
 - computer_tactics: A list of integers representing the computer's next strategic guesses based on previous hits.
 - player_score: An integer tracking the player's score (number of ships sunk).
 - computer_score: An integer tracking the computer's score (number of ships sunk).
##### Methods:
 - setup(): Sets up the game by placing ships on both the player's and computer's boards, either manually or automatically.
 - add_ship_for_player(ship): Prompts the player to place a ship either manually or automatically on their board.
 - show_game_boards(): Displays both the player's and computer's boards, hiding or revealing ships as appropriate.
 - get_shot(guesses): Prompts the player to input a valid guess (shot) and checks that it hasn't been guessed before.
 - computer_shot(): Generates a guess for the computer, using tactics if a previous shot hit a ship.
 - update_scores(hits, is_player): Updates the score for the player or computer based on whether a ship was hit.
 - play_turn(is_player): Executes a turn for either the player or the computer, checking for hits and updating the board.
 - calc_tactics(shot): Calculates the next set of potential shots for the computer based on the location of a previous hit.
 - check_win(board): Checks if all ships on a board have been sunk, indicating a win for the opponent.
 - ask_play_again(): Asks the player if they want to play another game after the current one ends.
 - start(): Starts the game, running through the setup and gameplay loop until a winner is determined or the player chooses to quit.

### Relationships Between Classes
##### Game: 
 - The central class that interacts with both the Player and Computer boards (Board instances) and coordinates the flow of the game.
##### Board:
 - Manages the layout of ships, tracks shots (hits and misses), and interacts with the Ship class to update ship statuses.
##### Ship:
 - Represents the individual ships on the board and tracks their status based on player and computer actions.


### Flowchart Overview

- The flowchart illustrates the logic and flow of the Battleships game, from the start of the game to its conclusion. The diagram is broken down into several key sections, each representing different stages of the game:

#### 1. Start and Setup:
 - The game begins with the display of instructions, followed by the prompt for the player to enter their name.
 - If the name is valid, the player moves on to ship placement. If the name is invalid, the player is asked to re-enter it.
#### 2. Ship Placement:
 - The player is given the option to place their ships either manually or automatically.
 - The computer places its ships automatically.
 - Both placements are validated to ensure they meet the game’s criteria (e.g., no overlap, valid coordinates).
#### 3. Gameplay:
 - Once ships are placed, the game enters the main gameplay loop where the player and the computer take turns shooting at each other's ships.
 - Each shot (user or computer) is validated to ensure it targets an unused coordinate on the board.
#### 4. Result Handling:
 - Shots result in either a hit or a miss. Hits are further checked to see if they result in the sinking of a ship (completion).
 - Scores are updated accordingly: a hit increases the score, while a miss does not.
#### 5. Endgame:
 - The game checks if all ships have been sunk (after 6 ships are sunk), which determines the winner.
 - The player is then given the option to either play again or exit the game.

### Flowchart Analysis
##### Decision Points:
 - The flowchart includes multiple decision points (e.g., checking the validity of a name, ship placement, and shot accuracy), ensuring that the game progresses correctly.
##### Loops: 
 - The gameplay loop repeats until a winner is determined, reflecting the turn-based nature of the Battleships game.
##### Outcomes: 
 - The game concludes with either a win for the player or the computer, after which the player can choose to restart or exit.


![The Quest Game Flowchart](assets/flow-chart/battleships-lucichart.png)


# Features

## Existing Features

### Welcome Screen

- The main game title in ASCII text Art and a welcome message is shown when user hits the run program
  button. The welcome message is given a typewriter effect for a more game-immersive experience.
- User is provided with an overview about the game and a general idea on how to play the game.
- As it is a Python terminal based game, it is designed to be functionality-focused rather than 
  visually appealing. The structure though is designed keeping in mind the aspects of the game.

  ![welcome_screen_image](assets/welcome_screen_image.png)


### Start Game Section

- Here user is prompted whether he wants to start the game, based on choices the game proceeds. If
  user has entered 'no' he is encouraged to play the game by providing a suitable feedback.
- The user can add their name to give them a personalised welcome to the game. The user's name is
  further used in the game story for providing player with a more engaging atmosphere.

![start_game_image](assets/start_game_image.png)


### Game Steps Section

- The user is then taken through a story with different scenarios and locations with detailed
  explanation of the journey and provided choices for the user to choose from which path they want to take. Choosing different paths can lead to different outcomes.

- Each story step is detailed and well-structured to give user an engaging adventure experience.


![start_story_step](assets/play_game_image_step.png)


- The storyline is designed to keep each step interconnected and user is provided with two options to 
  choose from, based on the user choice the game paths can result in different outcomes. 


![story_steps](assets/play_game_image.png)


### Success and Failure Outcomes

- Based on user choices, there are multiple paths which can lead to either success or failure
  outcomes.
- The game is designed in such a way that user can explore multiple scenarios and locations based
  upon the choices resulting in either of the outcomes.
- At the end of the user's journey, they are presented with a final text depending on their success or
  failure in the quest.

   - Success Text for the quest:
     
     ![success_outcome_image](assets/success_outcome_image.png)

   - Failure Text for the quest:
     
     ![failure_outcome_image](assets/fail_outcome_image.png)


- At the end, regardless of success or failure user is offered to play the game again. Based on the
  choice, the game either starts from the beginning or exits with a message.

  ![play_again_image](assets/play_again_image.png)


## Future Implementations 
 
- To fix the identified bugs in the game.
- Add colours to text and imagery for visual effect.
- Expand the story for multiple levels(easy, medium and difficult) to give user more deeper and
   immersive game experience.
- Use of google doc/ sheet to keep track of the number of players, their win and lose outcomes, a 
  form of leader board to display at the end of the game. This will give me opportunity to work with google spreadsheets to perform CRUD operations.



## Testing

- Note: This game will not work on mobiles as it runs on the mock terminal. (credit: Mock terminal created by Code Institute). No accessibilty or responsivity testing was therefore needed.

### Validator Testing

 - Python code is tested using Code Institute PYTHON LINTER, with no errors. Code passed through and  
   confirmed no problems.  

  - validated run.py file:
     
     ![run_validator_testing](assets/python_validation_runpy_file.png)

  
  - validated story.py file:

    ![story_validator_testing](assets/python_validation_storypy_file.png)



### Manual Testing:

- I tested the site in my local terminal and Code Institute Heroku Terminal.
- For user testing, I passed the application link to my friends and family and received positive 
  feedback, with some points to fix.

- Input Validation:

The application is tested extensively for input validation. I have manually tested it by doing 
following:

1. Proceed further with no input or input incorrect character/number for "Are you ready to play the 
   game" prompt.
     
    - Response: Receive an error message and prompt "Are you ready to play the game"(yes/no) again.

    
    ![start_game_input_validation](assets/start_game_input_validation.png)


2. Input username with less than 3 characters/ containing special characters/ proceed without 
   entering one.  
  
    - Response: Error message is displayed based on the user action and a prompt to enter user name.


    ![username_input_validation](assets/username_input_validation.png)


3. Input incorrect choice other than 1 and 2 for "Enter your choice" prompt while playing the game  
   for different paths.

    - Response: Error message is displayed for invalid choice and user is prompted to enter the 
                choice again.


    ![play_game_input_validation](assets/play_game_input_validation.png)        


4. At the end of the game, input incorrect character/ number/ press 'enter' with no input given for 
  "Would you like to play again" prompt.

    - Response: Receive an error message and prompt to enter the choice(yes/no) again.


    ![play_again_input_validation](assets/play_again_input_validation.png)


### Functional Testing:

Functional testing for user stories is as follows:

1. Expected: As a user, I want to understand the purpose and intention of the site and application  
   when I run the program.
    - Result: When user clicks on run program, the title in ASCII art and a welcome message with
              general idea and rules is displayed.

2. Expected: As a user, I want the navigation to be intuitive and easy to understand.
    - Result: The user is provided with easy to understand options and choices to navigate throughout
              the game.

3. Expected: As a user, I want to have an option to start the game.
             As a user, I should not have to worry about capitalizing or lowercase when typing.
    - Result: User is prompted with option for starting the game. Input by user(uppercase and
              lowercase) is handled as required correctly.

4. Expected: As a user, I want to be able to enter my name before I start to play the game.
             I would like to see a welcome message and my name added to storyline for more engaging
             experience.
    - Result: User is prompted to enter name which is further used in welcome message and storyline
              for personalized experience.

5. Expected: As a user, I want my input to be validated and error checked each time, so I can 
             re-enter my input/choice if it is invalid.
    - Result: Input validation is carried out at each step where user input is required and error 
              message is displayed if it is invalid prompting user to re-enter the input/choice.

6. Expected: As a user, I want to receive the next part in the story depending on the input choices.
             As a user, I want see the final outcome of the game based on the choices made.
    - Result: User is taken further to next part of the game depending on the choices and paths taken
              and provided with final text(success or failure) at the end of the game.

7. Expected: As a user, I want to have an opportunity to play again regardless of success or failure 
             in the game.
    - Result: At the end of the game, user is given an option to play again, based on user choices,
              the game exits or start from beginning.

8. User can explore different paths and scenarios with engaging story during the game, for multiple 
   success and failure outcomes.


### Unfixed Bugs

- There is one unfortunate bug that hasn't been resolved. I have used typewriter effect for  displaying some parts of my game story text. During final stages of testing, a bug was discovered where the user can interfere with the game text while typewriter effect is printing which results in altering of the main storyline text. I was not able to trail any solution for the bug. During discussion with my mentor, he did come up with a solution. I wanted to study the solution code first before using it in my project, but with no time in hand, I decided to keep it unresolved as it is not breaking the underlying code.

![typewriter_bug_image](assets/typewriter_bug.png)

- When user inteferes with the computer typing effect, it can though result with some of the texts
  taken in by following user input and displaying the error message of invalid choice/input. The user is re-prompted to input. But the flow of the game is not disturbed at any stage due to this bug. For smooth flow of the program it is best to enjoy the typwriter effect, sit back and play the game.

![typing_effect_bug_image](assets/typing_effect_bug.png)

- No other bugs are detected, the program runs smoothly at every stage for each user input and 
  appropriate feedback as necessary.


## Tools and Technologies

- [Python](https://www.python.org/) - used to develop the project (back end programming).
- [GitHub](https://github.com/) - to host the source code online.
- Codeanywhere built-in formatter to format structure for Python files in the project.
- Codeanywhere - IDE to develop the website.
- Git to provide the version control to commit and push code to the repository.
- [Am I Responsive](http://amiresponsive.blogspot.com/) to create the Mockup image in this README.
- [Heroku](https://www.heroku.com/) - to deploy the app.
- Code Institute [PYTHON LINTER](https://pep8ci.herokuapp.com/#) used to validate the python code for
  errors.
- [Draw.io](https://app.diagrams.net/) - to create flowchart for the project.
- [ASCII TEXT ART](https://fsymbols.com/) generator to create the command line title of the 
  application.
- Code Institute's Template to generate the workspace for the project.


## Imports

- sys: used for handling standard input and output streams during typewriter effect.
- time: used for controlling the timing of text output game for typewriter effect.


## Version Control

The site is developed through Codeanywhere IDE.

- Git

  Code has been pushed to repository on Github with following git commands:

    - git add . - to add files ready to commit
    - git commit -m "message" - to commit the code to local repository ready to be pushed
    - git push - final command used to push committed code to remote repo on Github


## Cloning the Repository

1. On Github navigate to the repository "gayatrig19/the-quest-adventures-game"
2. Click "Code" drop down menu - a green button shown right above the file list.
3. Copy the URL of the repository using "HTTPS", "SSH" or "Github CLI".
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type "git clone", and then paste the URL copied earlier.
7. Press enter to create local clone. A clone of the repository will now be created.

- For more details on how to clone the repository in order to create a copy for own use refer to the 
  site: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>


## Forking

1. On Github navigate to the repository "gayatrig19/the-quest-adventures-game"
2. Click "Fork" located towards top right corner on GitHub page.
3. Select "owner" for the forked repository from the dropdown menu under "owner".
4. It will create forked repo under the same name as original by default. 
   But you can type a name in "Repository name" or add a description in "Description" box.
5. Click on "Create fork". A forked repo is created.

- Forking allows you to make any changes without affecting original project. You can send the
  the suggestions by submitting a pull request. Then the Project Owner can review the pull request before accepting the suggestions and merging them.
- When you have fork to a repository, you don't have access to files locally on your device, for 
  getting access you will need to clone the forked repository.
- For more details on how to fork the repo, in order to for example suggest any changes to the 
  project you can visit:<https://docs.github.com/en/get-started/quickstart/fork-a-repo>


## Deployment

- The web application is displayed and deployed using template provided by Code Institute to test the
  code.

- The project is deployed on Heroku as follows:
1. Use: pip freeze > requirements.txt to add external libraries to deployed app.
2. Create Heroku account
3. In the top right, click 'New'
4. Click 'Create new app'
5. Give your app a name and select your region from drop down
6. Click 'Create new app'
7. Go to 'settings' tab, it's important you do it before deployment
8. Scroll down to 'config vars' section and key: PORT and value: 8000
9. Scroll down to 'Buildpacks' section
10. Click 'Add buildpack'
11. Add Python as first dependency and select 'Save changes'
12. Add node.js as a second dependency and save again (This is settings section done)
13. Select 'Deploy' tab at the top
14. Select 'Github' from 'Deployment method'
15. Type the name given to your project in Github and click 'search'
16. Scroll down and select Manual deployment method
17. You can also use Auto deployment method to allow the project to update every time you push the
    code.  
18. You can now click to view the app ready and running.

- For this project I used Manual deployment method to deploy the current state of the branch, every
  time I pushed the code from Codeanywhere.


# Credits

- [OPENAI](https://openai.com/) - used to create the storyline and plots for the game.
- The code for typewriter effect is referred from <https://github.com/Pauldwyer/Choose-your-adventure/blob/main/stories.py>
- The concept of how to use OOP in Python programming is studied from <https://www.educative.io/blog/how-to-use-oop-in-python> and <https://realpython.com/python3-object-oriented-programming/#:~:text=When%20you%20create%20an%20instance,from%20one%20instance%20to%20another.>
- The implementation of the story dictionary and iteration in the project is guided by my mentor, Ronan McClelland.
- Additional sources for implementing a game using data structures is studied from <https://medium.com/@a.hop/vocabulary-game-in-python-68932b850c49>
- Stack Overflow
- Code Institute mock terminal template to run the app.
- [ASCII TEXT ART](https://fsymbols.com/) generator to create the command line title of the 
  application.


# Acknowledgements

- I would like to express my gratitude to my mentor, Ronan McClelland, for his unwavering guidance,
  moral support, encouragement, and invaluable suggestions throughout the project. The project review
  sessions with my mentor, along with his solutions to my questions and the study materials he provided, were instrumental in the success of this project.
- I am also deeply thankful to my family and friends for their willingness to test the app and
  provide valuable feedback.
- Thank you Slack Community for answering all my questions and doubts.





