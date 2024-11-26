import random  
import time
class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
print("\033c")
riddle_itemtd = []
bosshealth_TH =  20
playerhealth_TH = 20
def tomhbossfight():
    def playerturn():
        global bosshealth_TH
        global riddle_itemtd
        if "Sword" in riddle_itemtd:
            playerroll_TH=random.randint(1, 20)
            playerroll_TH=playerroll_TH+1
            print("Your sword glows blue at the sight of the Lich. [+1 bonus to damage rolls]")
        else:
            playerroll_TH=random.randint(1, 20)
        print("rolling...")
        time.sleep(1)
        print("rolling...")
        time.sleep(1)
        print("rolling...")
        time.sleep (1)
        print("You rolled ", playerroll_TH, "and did ", playerroll_TH, "damage to the boss. Boss Health is now ", max(0, bosshealth_TH - playerroll_TH))
        bosshealth_TH = max(0, bosshealth_TH - playerroll_TH)
        time.sleep(3)
        if bosshealth_TH == 0:
            print("As you plunged the sword into the lich’s chest, The lich’s eyes widened in shock, and a chilling scream filled the cave as dark energy surged around it.") 
            time.sleep(3)
            print("The walls shook, and the shadows writhed in panic.")
            time.sleep(3)
            print("As the lich’s form began to disintegrate, it hissed...")
            time.sleep(3)
            print() 
            print(color.BOLD + color.RED + "“Y O U  W I L L  P A Y  F O R  T H I S!”" + color.END)
            print()
            time.sleep(3)
            print("...as it fades, the cave seems to return to normal, as if there was never anything there to begin with.") 
            time.sleep(3)
            print("You find yourself at the cave's entrance... ready to continue on with your day.")
            print()
            time.sleep(3)
            print(color.GREEN + r""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀
    ⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣁⣼⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠀⣠⣶⣿⣷⣆⠀⠀⠀⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀
    ⠀⢰⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣧⣾⣿⣿⣿⣿⡟⠀⠀⠀⠀⣼⣿⡟⠀⠀⣠⠀⠀⠀⠀
    ⢀⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⠟⣻⣿⣿⣿⣷⣤⠀⠀⠀⣿⣿⣃⣤⣾⣿⣀⣤⣤⡀
    ⢸⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡟⠀⢸⣿⡇⠀⠀⠀⢀⣀⣀⡀⠀⠸⣿⣿⠁⣰⣿⣿⡿⠋⢹⣿⡇⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣦⣄⠀⣿⣿⡇⠀⣼⣿⡇⠀⢀⣴⣿⣿⣿⣿⣀⣴⣿⣿⠀⠛⠻⠿⠁⠀⢸⣿⣿⣿⣿⣿⡿⠋⢻⣿⣿⠋⠉⠉⠁
    ⠘⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡇⠀⣿⣿⣧⠀⣼⣿⣿⢿⣿⣿⣿⡿⢹⣿⠀⠀⢀⣤⣶⣶⣿⣿⡟⠁⢸⣿⡇⠀⠸⣿⣏⠀⠀⠀⠀
    ⠀⢻⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⡏⠀⠘⣿⣿⣿⣿⣿⡇⠀⢻⣿⣿⣷⣿⣿⠃⠀⢿⣿⣿⠁⣼⣿⠀⣰⣿⡿⠛⢻⣿⣿⣿⠀⢸⣿⡇⠀⠀⠹⣿⣦⡀⠀⠀
    ⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢹⣿⣿⣿⣿⠃⠀⠸⣿⣿⣿⣿⣿⠀⠀⢸⣿⡏⢠⣿⣿⡆⣿⣿⠀⠀⣼⣿⣿⣿⣦⣿⣿⠉⣷⣦⣄⠹⣿⣿⣦⠀
    ⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⡿⠟⢿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠿⠆⠀⠀⠹⣿⣿⣿⣿⣆⣠⣿⣿⠃⣾⣿⣿⡇⢻⣿⣷⣿⣿⠟⢿⣿⣿⣿⣿⡇⠸⣿⣿⠀⣿⣿⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⢸⣿⣿⣿⣿⣤⣴⣿⣿⣿⡟⠀⠀⠀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠻⠀⠉⠉⠉⠀⠀⠀⠉⠛⣿⣿⣷⠀⢻⣿⣿⣿⣿⣿⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣠⣆⠀⠀⠀⠙⠛⠛⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧⡀⠉⠛⠛⠋⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠛⠉⠀⠀⢀⣴⣿⣿⡄⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣤⣄⣀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣄⠀⠀⢠⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣷⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀
            """)
            exit()
    def bossturn():
        global playerhealth_TH
        bossroll_TH=random.randint(1, 10)
        print("rolling...")
        time.sleep(1)
        print("rolling...")
        time.sleep(1)
        print("rolling...")
        time.sleep (1)
        print("Boss rolled ", bossroll_TH, "and did ", bossroll_TH, "damage to the boss. Player Health is now ", max(0, playerhealth_TH - bossroll_TH))
        playerhealth_TH = max(0, playerhealth_TH - bossroll_TH)
        time.sleep(2)
        if playerhealth_TH == 0:
            print(color.RED+"You died. Game over.")
            print()
            time.sleep(3)
            print(color.RED + r""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣶⣶⣶⣶⣾⣿⣿⣶⣶⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⡿⠿⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠻⢿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⢀⣠⣤⣶⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠶⠛⠛⠋⠉⠉⠛⠛⠳⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣨⣿⣿⣿⡿⠿⠛⠛⢿⣿⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣄⣠⣤⣶⣶⡿⠿⠟⠛⠉⠁⢀⣀⠀⠀⠘⣿⣇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣾⣿⠿⠟⠋⠉⠀⢀⣀⣴⡴⣾⣿⣿⣿⣷⡄⠀⢹⣿⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣾⣿⠿⠛⠋⠉⠀⠀⠀⢠⣶⣾⣿⣿⠿⠟⠃⢹⣿⡄⠈⣿⣧⠀⠀⣿⣧⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⢀⣀⣤⣤⣶⣾⡿⠿⠛⠛⠉⠁⢀⣤⣤⣄⠸⣿⣆⠀⠸⣿⡇⢿⣧⠀⢀⣠⠈⣿⣷⣶⣿⡏⠀⠀⠸⣿⣇⠀⠀
    ⠀⠀⠀⠀⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⣸⣏⣠⣤⣶⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣾⣿⠻⣿⣧⠹⣿⣆⠀⣿⡇⠸⣿⣿⣿⠿⠇⠸⣿⡏⢻⣿⣆⠀⠀⢿⣿⡀⠀
    ⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⣀⣠⣴⣶⣿⣿⠿⠟⠋⠉⠀⢀⣠⣤⣶⣾⣧⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⣿⣧⠘⣿⣆⣿⣿⠀⢻⣿⡄⠀⠀⣀⢻⣿⡀⠙⣿⣷⠄⠘⣿⣧⠀
    ⠀⠀⠀⢀⣀⣾⣿⣷⣾⡿⠿⠛⠋⠉⠀⠀⣤⣤⠀⢸⣿⡌⣿⣿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠸⣿⣇⠀⢸⣿⡇⠘⣿⣾⣿⠀⠈⣿⣷⣾⣿⡿⠮⠛⠃⠀⢀⣀⣠⣤⣾⣿⠄
    ⣴⣶⣾⡿⠿⠛⠛⠉⠁⠀⠀⠀⣶⣿⣆⠀⢹⣿⣧⣸⣿⣧⠸⣿⣦⣤⣶⣆⠀⠀⠀⠀⠀⠀⢻⣿⣄⢀⣿⡇⠀⠘⣿⣿⡆⠀⠘⠛⠉⠁⣀⣠⣤⣶⣾⣿⠿⠟⠛⠉⠁⠀
    ⢹⣿⣇⠀⠀⠀⣴⣿⣿⣷⡄⠀⢹⡿⣿⣆⠈⣿⣿⣿⣿⢿⣆⢻⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠃⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⠿⠟⠋⢩⣿⣿⠀⠀⠀⠀⠀⠀
    ⠀⢿⣿⡀⠀⠀⣿⣟⠈⠛⠋⠀⢸⣿⠈⣿⣆⠸⣿⣻⣿⡾⣿⡌⣿⣇⣀⣤⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣾⣿⠿⣿⠛⠉⠁⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀
    ⠀⠸⣿⣧⠀⠀⢻⣿⠀⣶⣾⣧⠘⣿⣷⣾⣿⣆⢿⣧⠉⠁⢻⣧⢹⣿⡿⠿⠛⠃⠀⢀⣀⣤⣴⣶⡾⡿⠟⠋⠛⠉⠁⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀
    ⠀⠀⢹⣿⡄⠀⠈⣿⣧⠙⠙⣿⡆⣿⣟⠉⠘⣿⣾⣿⡆⠀⠀⠛⠁⢀⣀⣠⣤⣶⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⣷⠀⠀⠘⣿⣷⣴⣿⡏⣿⡿⠀⠀⠈⠉⢀⣀⣠⣴⣶⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠸⣿⡆⠀⠀⠈⠛⠛⠋⠀⢀⣀⣤⣴⣶⣿⡿⠿⣿⣋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢻⣿⡄⢀⣀⣤⣴⣶⣿⠿⠿⠛⠋⠉⠀⠀⠀⠈⠙⠳⢦⣤⣀⣀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⣿⣿⡿⠿⠛⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""" + color.END)
            exit()
    time.sleep(2)
    print("As the door opens, you enter an ornate, yet dimly lit, hall; the air crackled with tension. You conclude that it's some kind of ancient burial chamber.") 
    time.sleep(3)
    print("Shadows clung to the walls, and the ground was littered with the remnants of past adventurers.")
    time.sleep(3)
    print("You notice the sword and shield of the knight from the first room and a book of old riddles from the stone face on the last door.")
    time.sleep(5)
    print("As you walk to the center of the room, you notice a figure standing it's skeletal form wrapped in tattered, ethereal robes.")
    time.sleep(5)
    print("Its eyes glowed with a malevolent light, piercing through the gloom.") 
    time.sleep(3)
    print()
    print(color.BOLD + color.RED + "“Y O U  D A R E  D I S T U R B  M Y  S L U M B E R, M O R T A L?”" + color.END) 
    print()
    time.sleep(5)
    print("It hissed, voice echoing with a dark resonance.") 
    time.sleep(3)
    print("Having a good look at the shadowy figure, you identify it as being a lich. With a flick of its wrist, the lich conjured a swirling mass of dark energy, tendrils of shadow reaching out toward you.")
    time.sleep(5)
    print("The air grew cold, and whispers of the damned filled the chamber. Pre-empting the cursed being’s attack, you rush in to strike the first blow!")
    time.sleep(5)
    print("The spectre from the cave entrance appears once more..")
    time.sleep(3)
    print()
    ready=input(color.BLUE+f"Are you ready {playername}? "+color.END)
    print()
    ready=ready.lower()
    while ready == "yes":
        print()
        time.sleep(2)
        print("Boss fight starting in 3")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("COMBAT INITIATED")
        time.sleep(2)
        while bosshealth_TH > 0 or playerhealth_TH > 0:
            playerturn()
            print()
            print(color.BOLD + color.RED + "“F O O L!”" + color.END)
            print()
            time.sleep(3) 
            print("the lich yelled, summoning a pair of skeletal minions that emerged from the ground, their bony fingers clawing at the air.") 
            bossturn()
            time.sleep(3)
            print("The lich raised both hands, drawing energy from the darkness around them.")
            time.sleep(3) 
            print()
            print(color.BOLD + color.RED + "“Y O U  T H I N K  Y O U  C A N  D E F E A T  M E? I  A M  E T E R N A L!”" + color.END)
            print()
            time.sleep(3)
            print("The chamber vibrated with power as the lich unleashed a blast of necrotic energy. You braced yourself, raising your sword, which shimmered with a faint light.") 
            time.sleep(3)
            print("The two forces collided, a shockwave erupting that sent dust and debris flying. You feel the sting of the dark magic.")
    while ready == "no":
        print(color.RED+"'THATS TOO BAD'"+color.END)
        print()
        time.sleep(2)
        print("Boss fight starting in 3")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("COMBAT INITIATED")
        time.sleep(2)
        while bosshealth_TH > 0 or playerhealth_TH > 0:
            playerturn()
            print(color.BOLD + color.RED + "“F O O L!”" + color.END)
            time.sleep(1) 
            print("the lich yelled, summoning a pair of skeletal minions that emerged from the ground, their bony fingers clawing at the air.") 
            bossturn()
            print("The lich raised both hands, drawing energy from the darkness around them.") 
            print()
            print(color.BOLD + color.RED + "“Y O U  T H I N K  Y O U  C A N  D E F E A T  M E? I  A M  E T E R N A L!”" + color.END)
            print()
            print("The chamber vibrated with power as the lich unleashed a blast of necrotic energy. You braced yourself, raising your sword, which shimmered with a faint light.") 
            print("The two forces collided, a shockwave erupting that sent dust and debris flying. You feel the sting of the dark magic.")
def tomdriddle():
    time.sleep(2)
    print("Before you enter the next room, you notice 6 symbols on the wall.")
    time.sleep(3)
    print(color.PURPLE+"'An arrow, a sword, a coin, a bird, an axe, and a helmet... I wonder what they mean...' "+color.END+"You whisper to yourself.")
    time.sleep(5)
    print("You make note of the symbols and proceed through the door.")
    print()
    time.sleep(3)
    print("In this room you see another ghostly visage, but not the same one you encountered at the cave entrance.")
    time.sleep(3)
    print("The spectre turns to you, a blank expression on it's face.")
    print()
    first_riddle_questiontd = "I have no wings but still fly high. In medieval tales, I conquer the sky, what am I?"
    first_riddle_correct_answertd = "an arrow"
    second_riddle_questiontd = "I have a head but never think, I have a tail but never stink. What am I?"
    second_riddle_correct_answertd = "a coin"
    third_riddle_questiontd = "I am sharp and can split stone, in medieval times, I'm always known, what am I?"
    third_riddle_correct_answertd = "an axe"
    riddle_itemtd = []
    riddle_first_attempttd = True
    while True:
        # Riddle 1
        print(color.CYAN+"In this room there are 3 riddles, you will need to guess all 3 correct to move on to the next room:"+color.END)
        print()
        time.sleep(2)
        print(color.CYAN+first_riddle_questiontd+color.END)
        time.sleep(2)
        first_riddle_answertd = input("Input your answer: ")
        first_riddle_answertd = first_riddle_answertd.lower()
        if first_riddle_answertd != first_riddle_correct_answertd:
            print()
            print(color.CYAN+"The answer is incorrect, please try again."+color.END)
            time.sleep(2)
            riddle_first_attempttd = False
            continue
        print()
        time.sleep(2)
        print(color.CYAN+"You are correct, on to riddle number 2."+color.END)
        print()
        time.sleep(2)
        # Riddle 2
        print(color.CYAN+"Now for the second riddle:"+color.END)
        print()
        time.sleep(2)
        print(color.CYAN+second_riddle_questiontd+color.END)
        time.sleep(2)
        second_riddle_answertd = input("Input your answer: ")
        second_riddle_answertd = second_riddle_answertd.lower()
        if second_riddle_answertd != second_riddle_correct_answertd:
            print()
            print(color.CYAN+"The answer is incorrect, please try again from riddle 1."+color.END)
            time.sleep(2)
            riddle_first_attempttd = False
            continue
        print()
        time.sleep(2)
        print(color.CYAN+"You are correct. You've solved the second riddle!"+color.END)
        print()
        time.sleep(2)
        # Riddle 3
        print(color.CYAN+"Now for the final riddle:"+color.END)
        print()
        time.sleep(2)
        print(color.CYAN+third_riddle_questiontd+color.END)
        time.sleep(2)
        third_riddle_answertd = input("Input your answer: ")
        third_riddle_answertd = third_riddle_answertd.lower()
        if third_riddle_answertd != third_riddle_correct_answertd:
            print()
            print(color.CYAN+"The answer is incorrect, please try again from riddle 1."+color.END)
            time.sleep(2)
            riddle_first_attempttd = False
            continue
        print()
        time.sleep(2)
        print(color.CYAN+"You are correct. You've solved all 3 riddles!"+color.END)
        time.sleep(2)
        print()
        if riddle_first_attempttd == True:
            riddle_itemtd.append("Sword")
            print (color.CYAN+"Well done, for answering all questions on the first attempt you've earned a:"+color.END,riddle_itemtd)
            time.sleep(2)
        print()
        time.sleep(3)
        tomhbossfight()
        break
def dice_rollmm():
    print("The dice is going to roll.")
    time.sleep(2)
    print("rolling...")
    time.sleep(2)
    mz=random.randint(1,6)
    mz1 = mz%2                  
    turns=1
    even=1
    even1=0
    if mz1==0:                    
        print(f"You rolled {mz}.")
        time.sleep(2)
        print("The door to the next room swings open.")
        print()
        time.sleep(2)
        tomdriddle()
    else:
        print(f"You rolled {mz}.")
        time.sleep(2)
        print("You lose the game.")
        time.sleep(2)
        choice=input("Do you want to roll the dice again? ")
        choice=choice.lower()
        time.sleep(2)
        if choice=="yes":
            while turns != 4:
                print("Rolling the dice again for you.")
                time.sleep(2)
                turns +=1
                even=random.randint(1,6)
                even1=even%2
                if even1==0:
                    print(f"You rolled {even}. The door to the next room swings open.")
                    print()
                    tomdriddle()
                else:
                    choice=input("Want to continue? ")
                    choice=choice.lower()
                    time.sleep(2)
                    if choice=="yes":
                        turns +=1
                        print(f"You lose the game as you rolled {even}.")
                        continue
            if turns==4:
                print(color.RED + "You lose the dice roll. Game over")
                print(color.RED + r""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣶⣶⣶⣶⣾⣿⣿⣶⣶⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⡿⠿⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠻⢿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⢀⣠⣤⣶⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠶⠛⠛⠋⠉⠉⠛⠛⠳⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣨⣿⣿⣿⡿⠿⠛⠛⢿⣿⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣄⣠⣤⣶⣶⡿⠿⠟⠛⠉⠁⢀⣀⠀⠀⠘⣿⣇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣾⣿⠿⠟⠋⠉⠀⢀⣀⣴⡴⣾⣿⣿⣿⣷⡄⠀⢹⣿⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣾⣿⠿⠛⠋⠉⠀⠀⠀⢠⣶⣾⣿⣿⠿⠟⠃⢹⣿⡄⠈⣿⣧⠀⠀⣿⣧⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⢀⣀⣤⣤⣶⣾⡿⠿⠛⠛⠉⠁⢀⣤⣤⣄⠸⣿⣆⠀⠸⣿⡇⢿⣧⠀⢀⣠⠈⣿⣷⣶⣿⡏⠀⠀⠸⣿⣇⠀⠀
    ⠀⠀⠀⠀⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⣸⣏⣠⣤⣶⣿⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣾⣿⠻⣿⣧⠹⣿⣆⠀⣿⡇⠸⣿⣿⣿⠿⠇⠸⣿⡏⢻⣿⣆⠀⠀⢿⣿⡀⠀
    ⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⣀⣠⣴⣶⣿⣿⠿⠟⠋⠉⠀⢀⣠⣤⣶⣾⣧⠀⠀⠀⠀⠀⠀⣿⣿⠀⠈⣿⣧⠘⣿⣆⣿⣿⠀⢻⣿⡄⠀⠀⣀⢻⣿⡀⠙⣿⣷⠄⠘⣿⣧⠀
    ⠀⠀⠀⢀⣀⣾⣿⣷⣾⡿⠿⠛⠋⠉⠀⠀⣤⣤⠀⢸⣿⡌⣿⣿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠸⣿⣇⠀⢸⣿⡇⠘⣿⣾⣿⠀⠈⣿⣷⣾⣿⡿⠮⠛⠃⠀⢀⣀⣠⣤⣾⣿⠄
    ⣴⣶⣾⡿⠿⠛⠛⠉⠁⠀⠀⠀⣶⣿⣆⠀⢹⣿⣧⣸⣿⣧⠸⣿⣦⣤⣶⣆⠀⠀⠀⠀⠀⠀⢻⣿⣄⢀⣿⡇⠀⠘⣿⣿⡆⠀⠘⠛⠉⠁⣀⣠⣤⣶⣾⣿⠿⠟⠛⠉⠁⠀
    ⢹⣿⣇⠀⠀⠀⣴⣿⣿⣷⡄⠀⢹⡿⣿⣆⠈⣿⣿⣿⣿⢿⣆⢻⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠃⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⠿⠟⠋⢩⣿⣿⠀⠀⠀⠀⠀⠀
    ⠀⢿⣿⡀⠀⠀⣿⣟⠈⠛⠋⠀⢸⣿⠈⣿⣆⠸⣿⣻⣿⡾⣿⡌⣿⣇⣀⣤⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣾⣿⠿⣿⠛⠉⠁⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀
    ⠀⠸⣿⣧⠀⠀⢻⣿⠀⣶⣾⣧⠘⣿⣷⣾⣿⣆⢿⣧⠉⠁⢻⣧⢹⣿⡿⠿⠛⠃⠀⢀⣀⣤⣴⣶⡾⡿⠟⠋⠛⠉⠁⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀
    ⠀⠀⢹⣿⡄⠀⠈⣿⣧⠙⠙⣿⡆⣿⣟⠉⠘⣿⣾⣿⡆⠀⠀⠛⠁⢀⣀⣠⣤⣶⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⣷⠀⠀⠘⣿⣷⣴⣿⡏⣿⡿⠀⠀⠈⠉⢀⣀⣠⣴⣶⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠸⣿⡆⠀⠀⠈⠛⠛⠋⠀⢀⣀⣤⣴⣶⣿⡿⠿⣿⣋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢻⣿⡄⢀⣀⣤⣴⣶⣿⠿⠿⠛⠋⠉⠀⠀⠀⠈⠙⠳⢦⣤⣀⣀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠈⣿⣿⡿⠿⠛⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""" + color.END)
                exit()
        else:
            return None 
print()
currentplayerws = "X"
winner = None
GameRunningws = True
def tictactoeroomws():
    print()
    time.sleep(2)
    print("As you step into the dimly lit chamber, the heavy iron door creaks shut behind you.")
    time.sleep(3)
    print("You turn, startled, and push against the door, but it was unyielding, sealed as if it had never been opened at all..")
    print()
    time.sleep(3)
    print("On the far side of the room you notice it, the only lightsource in the room, strange lines on the wall glowing unnaturally.")
    print()
    time.sleep(3)
    print("Just at that moment you hear it, a booming laughter attacking you from all directions.")
    print()
    time.sleep(3)
    print(color.RED + "You really did it! You fell right into my trap, NOW YOU MUST FIGHT ME TO THE DEATH MORTAL!")
    time.sleep(4)
    print("IN THE DEADLIEST OF ALL DUELS, A GAME OF WHITS BANNED IN THE DEMON WORLD FOR ITS BRUTALITY... A MORTAL LIKE YOU COULD NEVER HOPE TO WIN!")
    time.sleep(4)
    print("THE FEARED, THE OMINOUS...")
    print()
    time.sleep(2)
    print("TIC")
    time.sleep(1.5)
    print("TAC")
    time.sleep(1.5)
    print("TOE!!!!!!!"+color.END)
    time.sleep(1.5)
    print()
    print("*miniboss music begins*")
    print()
    time.sleep(1)
    boardws = ["-","-","-",
            "-","-","-",
            "-","-","-"]
    def printBoardws(boardws):
        print(boardws[0] + " | " + boardws[1] + " | " + boardws[2])
        print("----------")
        print(boardws[3] + " | " + boardws[4] + " | " + boardws[5])
        print("----------")
        print(boardws[6] + " | " + boardws[7] + " | " + boardws[8])
    def playerinputws(boardws):
        inp = int(input("Pick a slot 1-9 "))
        if inp >= 1 and inp <= 9 and boardws[inp-1] == "-":
            boardws[inp-1] = currentplayerws
        else:
            print("The Tic Tac Doom Demon Has taken this spot!")
        
    def checkhorizontalws(board):
        global winner
        if boardws[0] == boardws[1] == boardws[2] and boardws[0] != "-":
            winner = board[0]
            return True
        elif boardws[3] == boardws[4] == boardws[5] and boardws[3] != "-":
            winner = boardws[3]
            return True
        elif boardws[6] == boardws[7] == boardws[8] and boardws[6] != "-":
            winner = boardws[6]
            return True
    def checkvertws(boardws):
        global winner
        if boardws[0] == boardws[3] == boardws[6] and boardws[0] != "-":
            winner = boardws[0]
            return True
        elif boardws[1] == boardws[4] == boardws[7] and boardws[1] != "-":
            winner = boardws[1]
            return True
        elif boardws[2] == boardws[5] == boardws[8] and boardws[2] != "-":
            winner = boardws[2]
            return True
    def checkdiagonalws(boardws):
        global winner
        if boardws[0] == boardws[4] == boardws[8] and boardws[0] != "-":
            winner = boardws[0]
            return True
        elif boardws[2] == boardws[4] == boardws[6] and boardws[2] != "-":
            winner = boardws[2]
            return True
    def checktiews(boardws):
        if "-" not in boardws:
            printBoardws(boardws)
            print("Tie")
            print("*Clearly exhausted and flustered by your ability to survive, Tic Tac Doom collapses onto the floor")
            time.sleep(3)
            print("*You bend down and take the keys out off his eye socket and move on, deciding right there to leave this out of the chronicals.*")
            time.sleep(3)
            print("*You take the key and insert it into a suspiciously key shaped hole in the wall and a passageway opens up*")
            time.sleep(3)
            print("*you enter the passageway into the next room*")
            time.sleep(3)
            print("The next room you enter has a faint glow around it from the minerals in the cave walls. There are no torches lighting the room like last time.")
            time.sleep(3)
            print("As you look around you notice a single door. As you walk towards it,  a door handle appears")
            time.sleep(3)
            print("On the handle you spot a dice with the inscription,"+color.CYAN+"'A game of luck decides your fate, roll even and you survive, however, roll odd thrice and your fate is sealed'"+color.END)
            print()
            time.sleep(3)
            dice_rollmm()
    def checkwinws():
        if checkdiagonalws(boardws) or checkvertws(boardws) or checkhorizontalws(boardws):
            print()
            print(color.RED+"IT WAS A GOOD GAME MORTAL, WIN OR LOSE ANYONE WHO CAN PLAY THIS CURSED GAME DESERVES A SHOT AT THE BOSS!"+color.END)
            time.sleep(2)
            print("*TicTacDoom laughs maniacally* " +color.RED+"NOT LIKE YOU COULD BEAT THEM ANYWAY NYAHAHA"+color.END)
            time.sleep(3)
            print("*the mischievous demon disappears through a portal under its feet, leaving behind a key to the next room*")
            time.sleep(3)
            print("*You take the key and insert it into a suspiciously key shaped hole in the wall and a passageway opens up*")
            time.sleep(3)
            print("*You enter the passageway into the next room*")
            GameRunningws = False
            print()
            time.sleep(3)
            print("The next room you enter has a faint glow around it from the minerals in the cave walls. There are no torches lighting the room like last time.")
            time.sleep(3)
            print("As you look around you notice a single door. As you walk towards it,  a door handle appears")
            time.sleep(3)
            print("On the handle you spot a dice with the inscription,"+color.CYAN+"'A game of luck decides your fate, roll even and you survive, however, roll odd thrice and your fate is sealed'"+color.END)
            print()
            time.sleep(3)
            dice_rollmm()
    def switchPlayerws():
        global currentplayerws
        if currentplayerws == "X":
            currentplayerws = "O"
        else:
            currentplayerws = "X"
    def placeholdercomputerws(boardws):
        while currentplayerws == "O":
            positionws = random.randint(0,8)
            if boardws[positionws] == "-":
                boardws[positionws] = "O"
                switchPlayerws()
    while GameRunningws:
        printBoardws(boardws)
        playerinputws(boardws)
        checkwinws()
        checktiews(boardws)
        switchPlayerws()
        placeholdercomputerws(boardws)
        checkwinws()
        checktiews(boardws)
def room_1_ws():
    print("As you enter the cave, darkness envelops you, fading as quickly as it appeared. The room is suddenly lit by torches on all sides, and the entrance you came through is no longer there.")
    print()
    time.sleep(2)
    print("The only thing in the room is a crumbling statue of a knight. As you approach it, the statue’s eyes glow blue, and a voice echoes in your mind:")
    print()
    time.sleep(3)
    print(color.RED+"“Foolish adventurer, you were unwise to come here—and even more foolish to come alone. You will never see daylight again.”"+color.END)
    print()
    time.sleep(3)
    print("White etchings begin to appear on the statue’s shield, reading: 'To proceed through this room, you must choose the door wisely—left or right.")
    print("Just remember as you pass through adventurer, not all is as it seems'")
    print()
    time.sleep(3)
    print(f"Greetings {playername}... A choice lies before you...")
    time.sleep(2)
    room_choice_ws = input("One door glows"+color.BLUE+" blue"+color.WHITE+", the other"+color.RED+" red."+color.END+" Make your choice... if you dare... ")
    room_choice_ws = room_choice_ws.lower()
    if room_choice_ws == ("blue"):
        tictactoeroomws()
    elif room_choice_ws == ("red"):
        print("You chose the right door.")
        print()
        time.sleep(3)
        print("The next room you enter has a faint glow around it from the minerals in the cave walls. There are no torches lighting the room like last time.")
        time.sleep(3)
        print("As you look around you notice a single door. As you walk towards it,  a door handle appears")
        time.sleep(3)
        print("On the handle you spot a dice with the inscription,"+color.CYAN+"'A game of luck decides your fate, roll even and you survive, however, roll odd thrice and your fate is sealed'"+color.END)
        print()
        time.sleep(3)
        dice_rollmm()
    else:
        print("invalid choice, the statue of the Knight chuckles as his arm raises, unearthly forces taking possession of your legs, pushing you through the blue door.")
        tictactoeroomws()
print("                                                                                                                                                            ")
print("              ||||||||||   ||     ||   |||||||||       ||**** *      ||       ||   ||*      ||     |||||       |||||||||     |||||||||     ||*       ||    ****   ")
print("                  ||       ||     ||   ||              ||       *    ||       ||   || *     ||   ||     ||     ||           |         |    || *      ||   *    *  ")
print("                  ||       ||     ||   ||              ||        *   ||       ||   ||  *    ||   ||            ||          ||         ||   ||  *     ||     *     ")
print("                  ||       |||||||||   |||||||||       ||        *   ||       ||   ||   *   ||   ||   ||||||   |||||||||   |           |   ||   *    ||       *   ")
print("                  ||       ||     ||   ||              ||        *   ||       ||   ||    *  ||   ||     ||     ||          ||         ||   ||    *   ||         * ")
print("                  ||       ||     ||   ||              ||       *    ||       ||   ||     * ||   ||     ||     ||           |         |    ||     *  ||    *    * ")
print("                  ||       ||     ||   |||||||||       ||**** *       ||||||||     ||      *||     |||||       |||||||||     |||||||||     ||       *||     ****  ")
print("                   ")
print("                                                                   ||    ||       /\      /////////   |||||| ")
print("                                                                   ||    ||      /  \           *     ||     ")
print("                                                                   ||||||||     /____\        *       |||||| ")
print("                                                                   ||    ||    /      \     *         |||    ")
print("                              ||                                   ||    ||   /        \   /////////  |||||| ")
print("                              ||")
print("                              ||")
print("                              ||________________________________________________________________________________________________________________________________          ")
print("  *  *  ||||||||||||||||||||||||                                                                                                                                 =        ")
print("*      *||||||||||||||||||||||||                                                                                                                                     =    ")
print("*      *||||||||||||||||||||||||                                                                                                                                        = ")
print("*      *||||||||||||||||||||||||                                                                                                                                     =    ")  
print("  *  *  ||||||||||||||||||||||||________________________________________________________________________________________________________________________________ =        ")
print("                              ||") 
print("                              ||")
print("                              ||")
print("                              ||")
print()
time.sleep(5)
print("As you pass through a town, you hear rumors of a nearby cave that people have supposedly never returned from.")
time.sleep(3)
print("You decide it's probably just childish stories from bored townspeople.")
time.sleep(3)
print("Despite the tales, you make your way toward the cave, located just south of town through a dense forest.")
time.sleep(3)
print("As you approach, you notice that the area near the cave, unlike the rest of the forest, is eerily silent; there are no bird songs, not even a breeze rustling the trees.")
time.sleep(6)
print("Eventually, you reach the cave entrance. You pause, wondering if you should enter.")
time.sleep(3)
print()
print("But before you can think, a spectre appears before you... it is unknown whether this spectre is friend or foe.")
print()
time.sleep(3)
playername=input(color.BLUE + "What is your name.. adventurer? " + color.END)
playername=color.PURPLE+playername+color.END
time.sleep(3)
print()
print("You hesitate to give your name, but something compels you to answer."+color.PURPLE+f" 'My name is {playername}."+color.PURPLE+" Who are you?'"+color.END+" you ask the spectre, but it does not respond.")
print()
time.sleep(3)
print(color.BLUE+"Danger lies ahead. Enter at your own peril."+color.END)
time.sleep(2)
enterchoice=input(color.BLUE+"What will you choose, adventurer? Enter this cave and risk D E A T H? Or will you turn and live to see another day? "+color.END)
enterchoice=enterchoice.lower()
time.sleep(3)
if enterchoice=="enter":
    print()
    print(color.BLUE+"I tried to warn you..."+color.END)
    print()
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    print()
    time.sleep(1.5)
    room_1_ws()
else:
    print()
    print(color.BLUE+"You made the right decision... N E V E R  R E T U R N")
    print()
    exit()
