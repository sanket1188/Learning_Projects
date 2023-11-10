import turtle as t
from Food_class import Food

ALIGNMENT = "center"
FONT = ("Tahoma", 20, "normal")

class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 380)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}" , align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,-410)
        self.write("GAME OVER" , align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
    
# Add in a new function to show high score.
        

        



        