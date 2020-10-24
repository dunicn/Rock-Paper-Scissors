import random


class RockPaperScissors:

    def __init__(self):
        self.computers_option = ["scissors", "paper", "rock"]
        self.user_score = 0

    def default_game(self, user_input):
        comp_choice = random.choice(self.computers_option)
        win_case = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
        if user_input == comp_choice:
            self.user_score += 50
            print("There is a draw ({})".format(user_input))
        elif win_case[user_input] == comp_choice:
            self.user_score += 100
            print("Well done. The computer chose {} and failed".format(comp_choice))
        elif win_case[user_input] != comp_choice:
            print("Sorry, but computer chose {}".format(comp_choice))

    def complicated_game(self, option_list, user_input):
        comp_choice = random.choice(option_list)
        if user_input == comp_choice:
            self.user_score += 50
            print("There is a draw ({})".format(user_input))
        else:
            user_index = option_list.index(user_input)
            new_list = option_list[user_index + 1:] + option_list[:user_index]
            if comp_choice in new_list[:int((len(new_list) / 2))]:
                print("Sorry, but computer chose {}".format(comp_choice))
            else:
                self.user_score += 100
                print("Well done. The computer chose {} and failed".format(comp_choice))

    def final_game(self):
        user_name = str(input("Enter your name: "))
        print("Hello,", user_name)
        user_string = str(input())
        print("Okay, let's start")
        user_list = user_string.split(",")
        self.user_score = self.rating_method(user_name)
        while True:
            user_input = str(input())
            if user_input == "!exit":
                print("Bye!")
                break
            elif user_input not in self.computers_option and user_input != "!rating" and user_input not in user_list:
                print("Invalid input")
            elif user_input == "!rating":
                print("Your rating: {}".format(self.user_score))
            else:
                if user_string == "":
                    self.default_game(user_input)
                else:
                    self.complicated_game(user_list, user_input)

    def rating_method(self, name):
        rating = open("rating.txt", "r")
        user_score = 0
        for line in rating:
            if name in line:
                name_score = int(line.split()[1])
                user_score = name_score
        return user_score


test = RockPaperScissors()
test.final_game()
