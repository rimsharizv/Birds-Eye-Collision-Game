#!/bin/python3

######################################################
# Project: Bird's Eye Game
# This project uses Python and Turtle Graphics
# Trinket URL: https://trinket.io/python/8aa8d8d8d4
######################################################

#!/bin/python3
#imports
import turtle
import random
import math
import time

#global variables
  #setting screen of the game
s = turtle.Screen()

  #each character underneath have their attributes stored in a dictionary
  #these values would be pulled out from the dictionary in order to be used throughout the game
  
  #character player
player = {"turtle": turtle.Turtle(), "shape": "bird.png", "radius": 20, "lives": 3, "score": 0, "speed": 10}

  #harm characters (reduces life if it collides with player)
harm = {"turtle": turtle.Turtle(), "shape": "eagle.png", "radius": 20, "speed": 7}
harm2 = {"turtle": turtle.Turtle(), "shape": "cloud.png", "radius": 50, "speed": 6}

  #benefit chacters (increases score if it collides with player)
benefit = {"turtle": turtle.Turtle(), "shape": "realcoin.png", "radius": 15, "speed": 12}

  #splash screen message (title page)
startup_message = turtle.Turtle()

  #score board (board that increments score if player collides with benefit)
score_board = turtle.Turtle()

  #life board (board that displays the amount of player life left)
life_board = turtle.Turtle()

  #hiding all the turtles created so it is not displayed on splash screen
player["turtle"].hideturtle()
harm["turtle"].hideturtle()
harm2["turtle"].hideturtle()
benefit["turtle"].hideturtle()
score_board.hideturtle()
life_board.hideturtle()

  #initially setting game variables to False
game_over = False
game_start = False


#function definitions

  #collision detecting functions
def are_colliding (char_1, char_2):
  collision_detected = False
  
  dx = char_1["turtle"].xcor() - char_2["turtle"].xcor()
  dy = char_1["turtle"].ycor() - char_2["turtle"].ycor()
  distance = math.sqrt((dx * dx) + (dy * dy))

  if(distance < (char_1["radius"] + char_2["radius"])):
    collision_detected = True
  
  return collision_detected

  #key handlers
def up():
  t = player["turtle"]
  t.clear()
  current_y = t.ycor()
  new_y = current_y + player["speed"]
  t.sety(new_y)

def down():
  t = player["turtle"]
  t.clear()
  current_y = t.ycor()
  new_y = current_y - player["speed"]
  t.sety(new_y)

  #inserting harm characters on the screen
  #setting the movement from left to right
def harm_movement():
  t = harm["turtle"]
  t.clear()
  current_x = t.xcor()
  new_x = current_x - harm["speed"]
  t.setx(new_x)
  #harm character looping back to the right side with a random y position when hitting the left edge
  if harm["turtle"].xcor() <= (-250 - harm["radius"]):
   harm["turtle"].setx(250)
   #it's randomly generated between -250 to 250 throughout as the screen is 500x500
   harm["turtle"].sety(random.randint(-250,250))

def harm2_movement():
  t = harm2["turtle"]
  t.clear()
  current_x = t.xcor()
  new_x = current_x - harm2["speed"]
  t.setx(new_x)
  #harm 2 character looping back to the right side with a random y position when hitting the left edge
  if harm2["turtle"].xcor() <= (-250 - harm2["radius"]): 
   harm2["turtle"].setx(250)
   harm2["turtle"].sety(random.randint(-250,250))

  #inserting benefit character on the screen
  #setting the movement from left to right
def benefit_movement():
  t = benefit["turtle"]
  t.clear()
  current_x = t.xcor()
  new_x = current_x - benefit["speed"]
  t.setx(new_x)
  if benefit["turtle"].xcor() <= (-250 - benefit["radius"]):
   benefit["turtle"].setx(250)
   benefit["turtle"].sety(random.randint(-250,250))
  
  #player character looping back on the left side with a random x postion when hitting either the top or bottom edge of screen
def player_onscreen():
  if (player["turtle"].ycor() <= (-250 - player["radius"])):
    player["turtle"].sety(250)
  if (player["turtle"].ycor() >= (250 + player["radius"])):
    player["turtle"].sety(-250)

  #function to increase score if player collides with benefit
def increase_score():

  if are_colliding(player, benefit):
    player["score"] = player["score"] + 50 #score increments by 50
    benefit["turtle"].setx(250)
    benefit["turtle"].sety(random.randint(-250,250))
    #displays new score on score board
    score_board.clear()
    score_board.goto(-200,200)
    score_board.write("Score:",font=("times", 15, "bold"))
    score_board.goto(-130,200)
    score_board.write(player["score"],font=("times", 15, "bold"))

  #function to decrease life if player collides with either harm characters
def decrease_lives():
  if are_colliding(player, harm) or are_colliding(player, harm2):
    player["lives"] = player["lives"] - 1
    if are_colliding(player, harm2):
      harm2["turtle"].setx(250)
      harm2["turtle"].sety(random.randint(-250,250))
    else:
      harm["turtle"].setx(250)
      harm["turtle"].sety(random.randint(-250,250))
    #displays the life remaining on life board
    life_board.clear()
    life_board.goto(-80,200)
    life_board.write("Lives:",font=("times", 15, "bold"))
    life_board.goto(-10,200)
    life_board.write(player["lives"],font=("times", 20, "bold"))

  #function to initialize turtle settings
def initalize_turtle_settings():
    #initialize screen display
  s.setup(500, 500)
  s.bgpic("background.png")
  s.tracer(0)
  s.onkey(down, "Down")
  s.onkey(up, "Up")
  s.onkey(start, "Space")
    
    #initialize player position
  s.addshape(player["shape"])
  player["turtle"].shape(player["shape"])
  player["turtle"].penup()
  player["turtle"].sety(50)
  player["turtle"].setx(-180)
    
  s.listen()

    #initialize score position
  score_board.ht()
  score_board.penup()
  score_board.goto(-200,200)
  score_board.write("Score:",font=("times", 15, "bold"))
  score_board.goto(-120,200)
  score_board.write(player["score"],font=("times", 15, "bold"))

    #initialize life position
  life_board.ht()
  life_board.penup()
  life_board.goto(-80,200)
  life_board.write("Lives:",font=("times", 15, "bold"))
  life_board.goto(-10,200)
  life_board.write(player["lives"],font=("times", 15, "bold"))

    #initializw harm position
  s.addshape(harm["shape"])
  harm["turtle"].shape(harm["shape"])
  harm["turtle"].penup()
  harm["turtle"].setx(250)
  #it's randomly generated between -250 to 250 throughout as the screen is 500x500
  harm["turtle"].sety(random.randint(-250,250))

    #initalize harm2 position
  s.addshape(harm2["shape"])
  harm2["turtle"].shape(harm2["shape"])
  harm2["turtle"].penup()
  harm2["turtle"].setx(250)
  harm2["turtle"].sety(random.randint(-250,250))

    #initialize benefit position
  s.addshape(benefit["shape"])
  benefit["turtle"].shape(benefit["shape"])
  benefit["turtle"].penup()
  benefit["turtle"].setx(250)
  benefit["turtle"].sety(random.randint(-250,250))
  
  player["turtle"].hideturtle()
  harm2["turtle"].hideturtle()
  harm["turtle"].hideturtle()
  benefit["turtle"].hideturtle()
  

#function to display text on the splash screen (starting/title screen)
def start_game():
  startup_message.hideturtle()
  startup_message.penup()
  startup_message.goto(0,50)
  startup_message.color('red')
  #name of the game = 'Bird's Eye'
  startup_message.write("BIRD'S EYE", font = ("times", 40, "bold"), align = "center")
  startup_message.goto(0,0)
  startup_message.color('black')
  startup_message.write("PRESS SPACEBAR TO PLAY!", font = ("times", 30, "italic"), align = "center")
  startup_message.goto(0,-50)
  startup_message.write("HOW TO PLAY: ", font = ("times", 15, "italic"), align = "center")
  startup_message.goto(0,-70)
  startup_message.write("USE UP OR DOWN KEY TO MOVE", font = ("times", 15, "italic"), align = "center")
  startup_message.goto(0,-90)
  startup_message.write("(Collect coins to increase the score and dodge the eagle and stormy cloud!)", font = ("times", 10, "italic"), align = "center")
  s.update()

#function for the game to continously run until life = 0
def game_loop():
  global game_over
  while game_over != True:
    player["turtle"].st() #st = show turtle
    harm2["turtle"].st()
    harm["turtle"].st()
    benefit["turtle"].st()
    #calling out all functions once the game loop starts and game is not over
    harm_movement()
    harm2_movement()
    benefit_movement()
    increase_score()
    decrease_lives()
    player_onscreen()
    #setting a condition to stop the game if life <= 0
    if player["lives"] <= 0:
      game_over = True
      print("Game Over!")
    s.update()
    
  #hiding the turtle for 'Game Over' screen
  player["turtle"].hideturtle()
  harm2["turtle"].hideturtle()
  harm["turtle"].hideturtle()
  benefit["turtle"].hideturtle()
  #writing message on final screen
  startup_message.goto(0,0)
  startup_message.write("Game Over", font=("times", 45, "bold"), align="center")
  startup_message.goto(-60,-50)
  startup_message.write("Score: ", font=("times", 20, "bold"))
  startup_message.goto(30,-50)
  startup_message.write(player["score"],font=("times", 20, "bold"))
  s.update()

#function to start game
def start():
  #print("starting game")
  game_start = True
  startup_message.clear()
  life_board.goto(-80,200)
  life_board.write("Lives:",font=("times", 15, "bold"))
  life_board.goto(-10,200)
  life_board.write(player["lives"],font=("times", 15, "bold"))
  s.update()
  game_loop()

#main function
def main():
  initalize_turtle_settings()
  print("Start game by clicking spacebar")
  start_game()

main() 