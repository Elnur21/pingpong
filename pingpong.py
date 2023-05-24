import tkinter as tk
import time
import random
xinc=0
yinc=0
left_y=0
left_x=0
right_x=0
right_y=0
player_left_score=0
player_right_score=0
window=tk.Tk()
window.title("Pin pong game")
canvas = tk.Canvas (window, bg="black" , width=700 , height =500)
player_left=canvas.create_line(20, 220,20,280, fill='green', width='3')
player_right=canvas.create_line(680, 220,680,280, fill='blue', width='3')
line_center = canvas.create_line(350,500,350,0, fill='white', dash=(5,3))
ball=canvas.create_oval(340 , 240 , 360 , 260 , fill = 'red')

player_left_score_text=canvas.create_text(175, 20, text=f"Score: {player_left_score}", fill="white")
player_right_score_text=canvas.create_text(525, 20, text=f"Score: {player_right_score}", fill="white")

def start_game_function():
    global xinc, yinc, ball, player_left, player_right, player_left_score_text, player_right_score_text
    xinc = 0
    yinc = 0
    if button_start["text"] == "Start":
      button_start["text"] = "Restart"
      
    canvas.delete(player_left)
    canvas.delete(player_right)
    canvas.delete(ball)

    ball=canvas.create_oval(340 , 240 , 360 , 260 , fill = 'red')
    player_left=canvas.create_line(20, 220,20,280, fill='green', width='3')
    player_right=canvas.create_line(680, 220,680,280, fill='blue', width='3')
    xinc= int(random.random()*5)
    yinc = int(random.random()*5)
    launch_game()

      
    

    

button_start=tk.Button(window, text = "Start" , command=start_game_function)
button_start.pack()

game_button_text="Start"
start_game=True
resume_game=False
def resume():
  global resume_game,game_button_text, left_y, right_y, xinc, yinc

  if resume_game==True:
    resume_game=False
    button_resume['text'] = 'Resume'
    left_y=0
    right_y=0
    yinc=0
    xinc=0


  else:
    yinc+=5
    xinc+=5
    resume_game=True
    button_resume['text'] ="Stop"


button_resume = tk.Button(window, text = "Stop/Resume" , command=resume)

button_close_window = tk.Button(window, text = 'Quit' , command=window.destroy)
def key_press(e):
  global left_y
  global right_y

  if e.keysym=="s":
   gamer_label.config(text="Player 1")
   left_y=0
   left_y=left_y+10
  elif e.keysym=="a":
    gamer_label.config(text="Player 1")
    left_y=0
  elif e.keysym=="w":
    gamer_label.config(text="Player 1")
    left_y=0
    left_y=left_y-10
  if e.keysym=="Down":
   gamer_label.config(text="Player 2")
   right_y=0
   right_y=right_y+10
  elif e.keysym=="Right":
    gamer_label.config(text="Player 2")
    right_y=0
  elif e.keysym=="Up":
    gamer_label.config(text="Player 2")
    right_y=0
    right_y=right_y-10

gamer_label=tk.Label(window, text= "")
win_label= tk.Label(window, text= "")

gamer_label.pack(pady= 25)
window.bind('<KeyPress>',key_press)

def launch_game():
  global player_left, player_right, ball, xinc, yinc, left_x, right_x, right_y, left_y, player_left_score, player_right_score, player_left_score_text, player_right_score_text

  win_label.config(text=" ")
  while True:
      canvas.move(ball,xinc,yinc)
      canvas.move(player_left,left_x,left_y)
      canvas.move(player_right,right_x,right_y)

      window.update()

      time.sleep(0.03)

      ball_pos = canvas.coords(ball)
      player_left_pos = canvas.coords(player_left)
      player_right_pos = canvas.coords(player_right)

      xl,yl,xr,yr = ball_pos
      x0_left,y0_left,x1_left,y1_left = player_left_pos
      x0_right,y0_right,x1_right,y1_right= player_right_pos



      if xl==x0_right-20 and (yl>=y0_right and yl<=y1_right and yr>=y0_right and yr<=y1_right):
        # print(yr,y0_right,y1_right)
        xinc = -xinc
      if xl==x0_left and (yl>=y0_left and yl<=y1_left and yr>=y0_left and yr<=y1_left):
        xinc = -xinc
      if yl < abs(yinc) or yr > 500-abs(yinc):
        yinc = -yinc

      
      if y0_left==0 or y1_left==500:
        left_y= -left_y
      if y0_right==0 or y1_right==500:
        right_y= -right_y

      if xl>680:
        win_label.config(text="Player 1 won")
        player_left_score+=1
        canvas.itemconfig(player_left_score_text, text=f"Score: {player_left_score}")
        break
      elif xl<2:
        win_label.config(text="Player 2 won")
        player_right_score+=1
        canvas.itemconfig(player_right_score_text, text=f"Score: {player_right_score}")
        break
button_resume.pack()     
canvas.pack()

win_label.pack(pady= 25)
button_close_window.pack()
window.mainloop()