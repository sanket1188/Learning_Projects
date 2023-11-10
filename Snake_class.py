import turtle as t

INITIAL_POSITION = [(0 , 0),(-20,0),(-40,0)]

SPEED_CONSTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

        ## Another Approach to create the snake body
        # initial_position = [(0 , 0),(-20,0),(-40,0)]

        # for position in initial_position:
        #     snake = t.Turtle(shape="square")
        #     snake.color("white")
        #     snake.speed("fast")
        #     snake.goto(position)
        #     snake_list.append(snake)

        # For initial position only:

    def create_snake(self):
        x_axis = 0

        for i in range(len(INITIAL_POSITION)):
            snake = t.Turtle(shape="square")
            snake.color("white")
            snake.speed("normal")
            snake.penup()
            snake.goto(x=x_axis,y=0)
            x_axis -= 20
            self.snake_list.append(snake)

    def move(self):
        for item in range(len(self.snake_list)-1,0,-1):
            self.snake_list[item].goto(self.snake_list[item-1].xcor(),self.snake_list[item-1].ycor())
        self.snake_list[0].forward(SPEED_CONSTANT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)

    def addition(self):
        snake = t.Turtle(shape="square")
        snake.color("white")
        snake.speed("normal")
        snake.penup()
        snake.goto(x=self.snake_list[-1].xcor(),y=self.snake_list[-1].ycor())
        self.snake_list.append(snake)



