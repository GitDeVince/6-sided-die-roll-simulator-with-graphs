import random
import matplotlib.pyplot as plt
import numpy as np

#die_1 to die_6 holds how many times an iteration of random pick from 1-6 goes. If die says it rolls a 2, it will go to die_2

die_1 =  0
die_2 = 0
die_3 = 0
die_4 = 0
die_5 = 0
die_6 = 0

def die_roll(rolls):
    global die_1
    global die_2
    global die_3
    global die_4
    global die_5
    global die_6

    if rolls < 1:
        return
    else:
        rolling = random.randint(1,6) #simple random int from 1 to 6
    
        if rolling == 1: #here on out shows that each iteration that goes to one of those is added with 1 and it repeats until variable 'rolls' is zero
            die_1 = die_1 + 1

        elif rolling == 2:
            die_2 = die_2 + 1

        elif rolling == 3:
            die_3 = die_3 + 1
    
        elif rolling == 4:
            die_4 = die_4 + 1
    
        elif rolling == 5:
            die_5 = die_5 + 1
    
        elif rolling == 6:
            die_6 = die_6 + 1

    die_roll(rolls - 1)

def show_result():
    #straight forward printing all of the results
    print("These are the results:")
    print("1 = " + str(die_1))
    print("2 = " + str(die_2))
    print("3 = " + str(die_3))
    print("4 = " + str(die_4))
    print("5 = " + str(die_5))
    print("6 = " + str(die_6))

def plotting():
    x_value = ['side 1', 'side 2', 'side 3', 'side 4', 'side 5', 'side 6'] # names for the x axis
    y_value = [die_1, die_2, die_3, die_4, die_5, die_6] # these are the values from doing the random die rolls

    plt.style.use('seaborn')
    fig = plt.figure(figsize= (10, 5))

    plt.bar( x_value, y_value, color = 'maroon')

    plt.title("Bar graph of " + f'{rolls}'  " attempts from a 6-sided Die", fontsize = 24) #I thought about doing the "f'{rolls}' as a way to make the title of the graph customizable"
    plt.xlabel("Number of attempts", fontsize = 14)
    plt.ylabel("Side of a die", fontsize = 14)

    plt.show()


print("This is a simulation of rolling a 6-sided die and graph the results.")
simulation = True #simulation is the whole big picture of operating this program
while simulation:
    rolls = int(input('Please enter how many rolls you want to do: '))

    die_roll(rolls)
    show_result()   
    plotting()

    while True:
        decision = input('Do you wish to roll again? Y/N ')
        decision = decision.capitalize()
    
        if decision == "Y":
            break
        elif decision == "N":
            simulation = False
            print("Thank you for using!")
            break
        else:
            print("Please pick either Y or N")
            continue
            