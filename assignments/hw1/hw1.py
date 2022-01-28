"""
Name: <Elizabeth Maverick>
<ProgramName>.py

Problem: <Homework 1>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work. I discussed questions 1 and 2 with Brooke.

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)



def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter the player's made shots: "))
    shot_percentage = shots_made / total_shots * 100
    print("Shooting_percentage =", shot_percentage)

def coffee():
    # get cost of coffee per lb including shipping
    coffee_lbs = eval(input("Enter total lbs of coffee "))
    coffee_cost = coffee_lbs * (10.50 + .86) + 1.50
    # display result to user
    print("Coffee =", coffee_cost)


def kilometers_to_miles():
    kilometers = eval(input("Enter total number of kilometers "))
    miles = kilometers / 1.61
    print ("Kilometers_to_miles =", miles)



if __name__ == '__main__':
    pass
