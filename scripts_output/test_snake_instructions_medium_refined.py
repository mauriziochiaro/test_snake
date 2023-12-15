import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Flag to control the game loop
game_is_on = False

# Function to start the game
def start_game():
    global game_is_on
    game_is_on = True

# Function to stop the game and close the window
def quit_game():
    global game_is_on
    game_is_on = False
    turtle.bye()

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
    start_game()

def go_down():
    if head.direction != "up":
        head.direction = "down"
    start_game()

def go_left():
    if head.direction != "right":
        head.direction = "left"
    start_game()    

def go_right():
    if head.direction != "left":
        head.direction = "right"
    start_game()    

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
# Bind keys to start and quit functions
wn.listen()
# wn.onkeypress(start_game, "k")  # Replace "Start" with the actual start key you want to use
wn.onkeypress(quit_game, "q")      # Press 'q' to quit the game
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    try:
        wn.update()  # This will update the screen at the start of each loop iteration
        if game_is_on:
            
            # Check for collision with the border
            if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
                
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Update the score display
                scoreboard.clear()
                scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Check for collision with the food
            if head.distance(food) < 20:
                # Move the food to a random spot
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                food.goto(x,y)

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                segments.append(new_segment)

                # Increase the score
                score += 10

                if score > high_score:
                    high_score = score
                
                scoreboard.clear()
                scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # Move the end segments first in reverse order
            for index in range(len(segments)-1, 0, -1):
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)

            # Move segment 0 to where the head is
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x,y)

            move()    

            # Check for head collision with the body segments
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"
                    
                    # Hide the segments
                    for segment in segments:
                        segment.goto(1000, 1000)
                    
                    segments.clear()

                    # Reset the score
                    score = 0

                    # Update the score display
                    scoreboard.clear()
                    scoreboard.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            time.sleep(delay)
        wn.update()
    except turtle.Terminator:
        # Catch the exception and break the loop to end the program
        break
