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
    game_logo = """\u001b[34;1m
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

game_menu()