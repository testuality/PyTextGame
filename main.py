# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def play_game():
    print("Welcome to my game")
    name = input("Tell me your name ")
    age =int(input("Tell me your age "))
    print("Hello ", name, ", you are ", age, " years old")

    if (age >= 18):
        print("You can play the game")
        want = input("Do you want to play? ").lower()
        if want == "yes":
            print("Let's play!!")
    elif (age >= 14):
        print("You can play with supervision")
    else:
        print("You cannot play the game")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
