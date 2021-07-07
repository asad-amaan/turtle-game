import turtle 
wn = turtle.Screen()
alex = turtle.Turtle()

print("Welcome to Alex's house ")
print("Alex is a turtle, who you can guide to draw something on the screen ")
colr = input("Enter the color of the drawing that you want : ")
alex.color(colr)
ch = "yes"
choice = "yes"
overallch = "yes"
turn = ""
direction = ""

while (overallch.lower() != "no"):
    while(choice.lower() == "yes"):
        direction = input("Do you want to move forward or backward? ")
        if (direction.lower() == "forward"):

         front = input("Enter the distance by which you want Alex to move forward : ")
         alex.forward(int(front))
        elif (direction.lower() == "backward"):
            back = input("Enter the distance by which you want Alex to move backward : ")
            alex.backward(int(back))
        else: 
            print("Invalid input")
        choice = input("Do you want to continue to move front/back? (Yes/No) ")

    
    while (ch.lower() == "yes"):
        turn = input("Do you want to move left or right? ")
        if (turn.lower() == "right"):
            ri = input("Enter by what angle do you want Alex to turn right : ")
            alex.right(int(ri))
        elif (turn.lower() == "left"):
            le = input("Enter by what angle do you want Alex go turn left : ")
            alex.left(int(le))
        else:
            print("Invalid input")
        ch = input("Do you want to continue to move left/right (Yes/No) ")
    overallch = input("Do you want to repeat the whole process again? (Yes/No)  ")