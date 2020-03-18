def display_message(message, color="white"):
    print(" ")
    print(" ")
    print("\033[1;" + select_color(color) + ";40m " + message + "  \n")
    print(" ")
    print(" ")


def select_color(color):
    colors = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "purple": "35",
        "cyan": "36",
        "white": "37"
    }
    return colors[color]


def display_begining():
    print(''' 
   _____         ___.                       
  /  _  \   _____\_ |_________   ____    /\ 
 /  /_\  \ /     \| __ \_  __ \_/ __ \   \/ 
/    |    \  Y Y  \ \_\ \  | \/\  ___/   /\ 
\____|__  /__|_|  /___  /__|    \___  >  \/ 
        \/      \/    \/            \/      
________                                
\______ \ _____    _____   ____   ______
 |    |  \\__  \  /     \_/ __ \ /  ___/
 |    `   \/ __ \|  Y Y  \  ___/ \___ \ 
/_______  (____  /__|_|  /\___  >____  >
        \/     \/      \/     \/     \/ 
    ''')
    print("")
