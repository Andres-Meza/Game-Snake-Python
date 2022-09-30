import turtle;
import time;
import random;

posponer = 0.1;
score = 0;
high_score = 0;

wn = turtle.Screen();
wn.title("Snake");
wn.bgcolor("black");
wn.setup(width = 600, height = 600);
wn.tracer(0)

#Cabeza Serpiente
head = turtle.Turtle();
head.speed(0);
head.shape("square");
head.color("#68FF00");
head.penup();
head.goto(0, 0);
head.direction = "stop";  # type: ignore

#Cabeza Serpiente
eat = turtle.Turtle();
eat.speed(0);
eat.shape("circle");
eat.color("red");
eat.penup();
eat.goto(0, 100);

#Cuerpo Serpiente
segment = [];

#Marcador
text = turtle.Turtle();
text.speed(0);
text.color("#fff");
text.penup();
text.hideturtle();
text.goto(0, 260);
text.write("Score: 0            High Score: 0", align = "center", font = ("Courier New", 24, "normal"));

#Funcionalidad
def up():
  head.direction = "up"; # type: ignore

def down():
  head.direction = "down"; # type: ignore

def left():
  head.direction = "left"; # type: ignore

def right():
  head.direction = "right"; # type: ignore


def move():
  if head.direction == "up":  # type: ignore
    y = head.ycor();
    head.sety(y + 20);

  if head.direction == "down":  # type: ignore
    y = head.ycor();
    head.sety(y - 20);

  if head.direction == "left":  # type: ignore
    x = head.xcor();
    head.setx(x - 20);

  if head.direction == "right":  # type: ignore
    x = head.xcor();
    head.setx(x + 20);

#Entrada del Teclado
wn.listen();
wn.onkeypress(up, "Up");
wn.onkeypress(down, "Down");
wn.onkeypress(left, "Left");
wn.onkeypress(right, "Right");

while True:
  wn.update();

  #Choques con el Borde
  if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
    #Game Over
    game = turtle.Turtle();
    game.speed(0);
    game.color("tomato");
    game.penup();
    game.hideturtle();
    game.goto(0, 0);
    game.write("GAME OVER", align = "center", font = ("Courier New", 70, "normal"));
    time.sleep(2);
    head.goto(1,1)
    head.direction = 'stop';  # type: ignore

    #Borrar el cuerpo y marcador
    for segments in segment:
      segments.goto(1000, 1000)
    segment.clear();
    game.clear();
    score = 0;
    text.clear();
    text.write("Score: {}            High Score: {}".format(score, high_score), align = "center", font = ("Courier New", 24, "normal"));



  #Comida (Al tocar cambie de lugar la comida)
  if head.distance(eat) < 20:
    x = random.randint(-280, 280);
    y = random.randint(-280, 280);
    eat.goto(x, y);

    new_segment = turtle.Turtle();
    new_segment.speed(0);
    new_segment.shape("square");
    new_segment.color("#7AC944");
    new_segment.penup();
    segment.append(new_segment);

    #Aumentrar marcador
    score += 10;

    if score > high_score:
      high_score = score;

    text.clear();
    text.write("Score: {}            High Score: {}".format(score, high_score), align = "center", font = ("Courier New", 24, "normal"));

  #Mover el Cuerpo
  total_segments = len(segment);
  for index in range(total_segments -1, 0, -1):
    x = segment[index - 1].xcor();
    y = segment[index - 1].ycor();
    segment[index].goto(x, y);

  if total_segments > 0:
    x = head.xcor();
    y = head.ycor();
    segment[0].goto(x, y);

  move();

  #Choques con el Cuerpo
  for segments in segment:
    if segments.distance(head) < 10:
      #Game Over
      game = turtle.Turtle();
      game.speed(0);
      game.color("tomato");
      game.penup();
      game.hideturtle();
      game.goto(0, 0);
      game.write("GAME OVER", align = "center", font = ("Courier New", 70, "normal"));
      time.sleep(2);
      head.goto(0, 0);
      head.direction = "stop"; # type: ignore

      for segments in segment:
        segments.goto(1000, 1000)
      segment.clear();
      game.clear();
      score = 0;
      text.clear();
      text.write("Score: {}            High Score: {}".format(score, high_score), align = "center", font = ("Courier New", 24, "normal"));

  time.sleep(posponer);
