import random
import time

row11 = "[] "
row12 = "[] "
row13 = "[] "
row21 = "[] "
row22 = "[] "
row23 = "[] "
row31 = "[] "
row32 = "[] "
row33 = "[] "

options = [11,12,13,21,22,23,31,32,33]
end = False

def checkPlayer():
    global row11, row12, row13, row21, row22, row23, row31, row32, row33, end

    if row11 == row22 == row33 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row11 == row12 == row13 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row11 == row21 == row31 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row13 == row23 == row33 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row12 == row22 == row32 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row13 == row22 == row31 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row21 == row22 == row23 == "X  ":
        print("You Won!")
        end = True
        exit()
    if row31 == row32 == row33 == "X  ":
        print("You Won!")
        end = True
        exit()
    if end == False:
        ai()

def checkComputer():
    global row11, row12, row13, row21, row22, row23, row31, row32, row33, end

    if row11 == row22 == row33 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row11 == row12 == row13 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row11 == row21 == row31 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row13 == row23 == row33 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row12 == row22 == row32 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row13 == row22 == row31 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row21 == row22 == row23 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if row31 == row32 == row33 == "O  ":
        print("Computer Won!")
        end = True
        exit()
    if end == False:
        player()
def player():
    global row11, row12, row13, row21, row22, row23, row31, row32, row33
    if end == False:
        enter = int(input("Input Where You Want To Go eg: 13 >> "))
        print("")
        if enter == 11:
            if row11 == "[] ":
                row11 = row11.replace("[]", "X ")
            else:
                print(f"'{row11}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 12:
            if row12 == "[] ":
                row12 = row12.replace("[]", "X ")
            else:
                print(f"'{row12}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 13:
            if row13 == "[] ":
                row13 = row13.replace("[]", "X ")
            else:
                print(f"'{row13}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 21:
            if row21 == "[] ":
                row21 = row21.replace("[]", "X ")
            else:
                print(f"'{row21}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 22:
            if row22 == "[] ":
                row22 = row22.replace("[]", "X ")
            else:
                print(f"'{row22}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 23:
            if row23 == "[] ":
                row23 = row23.replace("[]", "X ")
            else:
                print(f"'{row23}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 31:
            if row31 == "[] ":
                row31 = row31.replace("[]", "X ")
            else:
                print(f"'{row31}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 32:
            if row32 == "[] ":
                row32 = row32.replace("[]", "X ")
            else:
                print(f"'{row32}' Has Already Been Placed There, Try Again...\n")
                player()
        if enter == 33:
            if row33 == "[] ":
                row33 = row33.replace("[]", "X ")
            else:
                print(f"'{row33}' Has Already Been Placed There, Try Again...\n")
                player()
        while enter not in [11,12,13,21,22,23,31,32,33]:
            print("I Could Not Find Anywhere To Place With That Number... Try Again\n")
            player()
            break

        print(f"{row11}{row12}{row13}\n{row21}{row22}{row23}\n{row31}{row32}{row33}\n")
        checkPlayer()
        

def ai():
    global row11, row12, row13, row21, row22, row23, row31, row32, row33, end
    computer = random.choice([11,12,13,21,22,23,31,32,33])
    try:
        if computer == 11:
            if row11 == "[] ":
                print(f"The Ai Chose: {computer}\n")
                row11 = row11.replace("[]", "O ")
            else:
                ai()
        if computer == 12:
            if row12 == "[] ":
                print(f"The Ai Chose: {computer}")
                row12 = row12.replace("[]", "O ")
            else:
                ai()
        if computer == 13:
            if row13 == "[] ":
                print(f"The Ai Chose: {computer}")
                row13 = row13.replace("[]", "O ")
            else:
                ai()
        if computer == 21:
            if row21 == "[] ":
                print(f"The Ai Chose: {computer}")
                row21 = row21.replace("[]", "O ")
            else:
                ai()
        if computer == 22:
            if row22 == "[] ":
                print(f"The Ai Chose: {computer}")
                row22 = row22.replace("[]", "O ")
            else:
                ai()
        if computer == 23:
            if row23 == "[] ":
                print(f"The Ai Chose: {computer}")
                row23 = row23.replace("[]", "O ")
            else:
                ai()
        if computer == 31:
            if row31 == "[] ":
                print(f"The Ai Chose: {computer}")
                row31 = row31.replace("[]", "O ")
            else:
                ai()
        if computer == 32:
            if row32 == "[] ":
                print(f"The Ai Chose: {computer}")
                row32 = row32.replace("[]", "O ")
            else:
                ai()
        if computer == 33:
            if row33 == "[] ":
                print(f"The Ai Chose: {computer}")
                row33 = row33.replace("[]", "O ")
            else:
                ai()
        print(f"{row11}{row12}{row13}\n{row21}{row22}{row23}\n{row31}{row32}{row33}\n")
        checkComputer()
    except:
        if end == False:
            print("DRAW!")
            exit()
def welcome():
    print(f"""
    
    
    Welcome To Tic Tac Toe :)

    Here Is What The Grid Looks Like

\t{row11}{row12}{row13}\n\t{row21}{row22}{row23}\n\t{row31}{row32}{row33}
    
    How You Input Where You Want To Go Is Easy

    To Go Top Left All You Have To Type Is 11

    The First Digit Is For The Horizontal Row And The Second Is For The Vertical Row

    You Are 'X' And The Ai Is 'O'

    Enjoy!
    
    Note: Please Leave Feedback So I Know What To Improve Thank you! :D
    """)
    time.sleep(1)
    player()

if __name__ == "__main__":
    welcome()
