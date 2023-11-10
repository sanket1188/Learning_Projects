import turtle as t
import time
from Snake_class import Snake
from Food_class import Food
from Score_Class import Scoreboard

my_screen = t.Screen()
my_screen.setup(width=840,height=840)
my_screen.title("Sanket's Snake Game")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# This is to draw the boundary
mypen = t.Turtle()
mypen.penup()
mypen.setposition(-370,-370)
mypen.pendown()
mypen.pensize(2)
mypen.color('white')
for side in range(4):
    mypen.forward(740)
    mypen.left(90)
mypen.hideturtle()

# Listen to the keys on the screen!
my_screen.listen()

my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on == True:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

# This section will identify if the the snake ate the food or not.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.addition()
        snake.move()

# This section is to detect the collision with the boundary.
    if snake.head.xcor() > 360 or snake.head.xcor() < -360 or snake.head.ycor() > 360 or snake.head.ycor() < -360:
        scoreboard.game_over()
        game_is_on = False

# This segment is to check the collision with any part of the tail.
    for item in snake.snake_list[1:]:
        if snake.head.distance(item) < 10:
            scoreboard.game_over()
            game_is_on = False


my_screen.exitonclick()