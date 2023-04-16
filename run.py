import random
from words import word_list

def new_word():
    """
    Retrieves a new randomised word from the imported word list
    """
    random_word = random.choice(word_list)
    return random_word.upper()

def game_menu():
    """
    Displays the start menu of the game. 
    The user is given three options to choose from.
    Option '1' will redirect to the rules page.
    Option '2' will redirect to game difficulty selection.
    Option '3' will exit the game entirely.
    Validates whether the user's input is '1', '2' or '3'.
    """
    game_logo = """\u001b[34m
           _________ ___ ___    _____ __________ ____  __       
          /   _____//   |   \  /  _  \ \______  \    |/ _|        
          \_____  \/    ~    \/  /_\  \|       _/      <          
          /        \    Y    /    |    \    |   \    |  \         
         /_______  /\___|_  /\____|__  /____|_  /____|__ \        
                 \/       \/         \/       \/        \/        
        ________________________________  _________  ____  __
       /  _  \__    ___/\__    ___/  _  \ \_   ___ \|    |/ _|
      /  /_\  \|    |     |    | /  /_\  \/    \  \/|      <  
     /    |    \    |     |    |/    |    \     \___|    |  \ 
     \____|__  /____|     |____|\____|__  /\______  /____|__ \ 
             \/                         \/        \/        \/
    """
    print(game_logo)
    print("Welcome! Are you ready to play?\n")
    print("Enter '1' to see game rules.")
    print("Enter '2' to play game.")
    print("Enter '3' to quit game.\n")
    exit_terminal = False
    while not exit_terminal:
        choose_option = input("Please enter '1', '2' or '3': ")
        if choose_option == "1":
            game_rules()
            break
        elif choose_option == "2":
            new_word()
            select_difficulty()
        elif choose_option == "3":
            exit_terminal = True
            exit()
        else:
            print(f"\nOops! {choose_option} is invalid.\n")

def game_rules():
    """
    Displays the rules of the game, which is listed using dashed lines.
    'Enter' key will redirect the user back to the start menu.
    Validates whether the user's input is the 'Enter' key.
    """
    rules = """
         __________ ____ ___ ____     ___________ _________
         \______   \    |   \    |    \_   _____//   _____/
          |       _/    |   /    |     |    __)_ \_____  \ 
          |    |   \    |  /|    |___  |        \/        \ 
          |____|_  /______/ |_______ \/_______  /_______  /
                 \/                 \/        \/        \/ 
    """
    print(rules)
    print("- A shark has appeared! Help the person before it attacks!")
    print("- You must solve the hidden word in order to save them.")
    print("- Each difficulty will give a different number of lives.")
    print("- Make a guess by typing any letter.")
    print("- Guesses that have already been used will be displayed.")
    print("- Each incorrect guess will bring the shark closer!")
    print("- Best of luck! They need your help now more than ever.\n")
    home_page = False
    while not home_page:
        back_to_home = input("\nPress 'Enter' key to return: ")
        if back_to_home == "":
            home_page = True
            game_menu()
        else:
            print(f"\nOops! {back_to_home} is invalid.")

def select_difficulty():
    """
    Displays various game difficulty modes that the user can attempt to beat.
    Game will begin once a choice has been made.
    Validates whether the user's input is 'E', 'M' or 'C'.
    """
    choose_art = """
   _________   ___ ___  ________   ________    ___________________
   \_   ___ \ /   |   \ \_____  \  \_____  \  /   _____|_   _____/
   /    \  \//    ~    \/   |   \  /   |   \ \_____  \ |    __)_ 
   \     \___\    Y    /    |    \/    |    \/        \|        \ 
    \______  /\___|_  /\_______  /\_______  /_______  /_______  /
           \/       \/         \/         \/        \/        \/ 
    """
    print(choose_art)
    print("Enter 'E' for Easy - 8 Lives")
    print("Enter 'M' for Moderate - 6 Lives")
    print("Enter 'C' for Challenging - 4 Lives\n")
    lives = 0
    begin_game = False
    while not begin_game:
        level_select = input("Please choose game difficulty: ").upper()
        if level_select == "E":
            lives = 8
            begin_game = True
            print("\nGame difficulty set to 'Easy'. Knock 'em dead!\n")
            break
        elif level_select == "M":
            lives = 6
            begin_game = True
            print("\nGame difficulty set to 'Moderate'. All the best!\n")
            break
        elif level_select == "C":
            lives = 4
            begin_game = True
            print("\nGame difficulty set to 'Challenging'. Use them wisely!\n")
            break
        else:
            print(f"\nOops! {level_select} is invalid.")
            print("\nInput needs to be 'E', 'M' or 'C'.\n")
    return lives

def shark_phases(lives):
    phases = [
"""
                    o  What's that in the water?
~~~~~~~~~~~~~~~~~~~/|\~~
""",
"""
   |\              \o/ SHARK!
~~ | \ ~~~~~~~~~~~~ | ~~
""",
"""
     |\            \o/ HELP!
~~~~ | \ ~~~~~~~~~~ | ~~
""",
"""
       |\          \o/ SOMEONE PLEASE!
~~~~~~ | \ ~~~~~~~~ | ~~
""",
"""
         |\        \o/ SOS!
~~~~~~~~ | \ ~~~~~~ | ~~
""",
"""
           |\      \o/ SAVE ME!
~~~~~~~~~~ | \ ~~~~ | ~~
""",
"""
             |\    \o/ OH NO!
~~~~~~~~~~~~ | \ ~~ | ~~
""",
"""
               |\   o  Goodbye cruel world...
~~~~~~~~~~~~~~ | \ /|\~~
""",
"""
                 |\  Mmm, delicious!
~~~~~~~~~~~~~~~~ | \ ~~\n
"""
    ]

def new_game(random_word, lives):
    """
    Displays the number of lives left and the shark phases graphic.
    Both of which are in accordance with the game's difficulty,
    the letters previously used and the hidden word.
    
    The correct letter will be added to the list of letters used.
    It will gradually reveal the hidden word until it is complete.
    
    The incorrectly guessed letter will be added to the list of letters used.
    The user will lose a life until the game is over or the game is won.
    
    Validates that the user's entry is a letter,
    does not include more than one letter, 
    has not previously been used and is contained in the hidden word.
    """
    hidden_word = "_" * len(random_word)
    game_over = False
    letter_used = []
    print(f"Lives remaining: {lives}")
    print("Letters used:", " ".join(letter_used))
    print(shark_phases(lives))
    print(hidden_word)
    while not game_over and lives > 0:
        guess = input("\nEnter any letter: ").upper()
        if not guess.isalpha():
            print(f"\nOops! {guess} is not a letter.")
            print("\nPlease enter a letter.")
            print(f"\nLives remaining: {lives}")
            print("Letters used:", " ".join(letter_used))
            print(shark_phases(lives))
            print(hidden_word)
            continue
        elif len(guess) != 1:
            print(f"\nOops! {guess} contains more than one letter.")
            print("\nPlease enter one letter at a time.")
            print(f"\nLives remaining: {lives}")
            print("Letters used:", " ".join(letter_used))
            print(shark_phases(lives))
            print(hidden_word)
            continue
        elif guess in letter_used:
            print(f"\nOops! {guess} has been used!")
            print("\nPlease enter a new letter.")
            print(f"\nLives remaining: {lives}")
            print("Letters used:", " ".join(letter_used))
            print(shark_phases(lives))
            print(hidden_word)
            continue
        elif guess in random_word:
            letter_used.append(guess)
            print(f"\nOutstanding work! {guess} is in the hidden word")
            hidden_word = ""
            for i in range(len(random_word)):
                if random_word[i] in letter_used:
                    hidden_word += random_word[i]
                else:
                    hidden_word += "_"
            print(f"\nLives remaining: {lives}")
            print("Letters used:", " ".join(letter_used))
            print(shark_phases(lives))
            print(hidden_word)
            if hidden_word == random_word:
                game_over = True
                print("Letters used:", " ".join(letter_used))
                print(shark_phases(lives))
                print("YOU WIN!")
                print("\nAmazing work! You're a lifesaver :)\n")
                print("Continue to End Menu")
        else:
            letter_used.append(guess)
            lives -= 1
            print(f"\nOops! {guess} is not in the hidden word.")
            print(f"\nLives remaining: {lives}")
            print("Letters used:", " ".join(letter_used))
            print(shark_phases(lives))
            print(hidden_word)
    if lives == 0:
        game_over = True
        print("GAME OVER")
        print("\nBetter luck next time :(")
        print(f"\nThe hidden word was {random_word}\n")
        print("Continue to End Menu")

game_menu()